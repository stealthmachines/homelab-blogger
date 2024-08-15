import os
import requests
import json
from datetime import datetime
from urllib.parse import urlparse
from dotenv import load_dotenv
from web3 import Web3

# Load environment variables
load_dotenv('/app/config.env')

# Configuration from environment variables
facebook_page_id = os.getenv('FACEBOOK_PAGE_ID')
access_token = os.getenv('ACCESS_TOKEN')
local_store_file = 'facebook_posts.json'
media_directory = 'facebook_media'

erc20_contract_address = os.getenv('ERC20_CONTRACT_ADDRESS')
erc20_contract_abi = json.loads(os.getenv('ERC20_CONTRACT_ABI'))
ethereum_provider = os.getenv('ETH_PROVIDER')
from_address = os.getenv('FROM_ADDRESS')
private_key = os.getenv('PRIVATE_KEY')
to_address = os.getenv('TO_ADDRESS')
reward_amount = int(os.getenv('REWARD_AMOUNT'))

# Initialize Web3
w3 = Web3(Web3.HTTPProvider(ethereum_provider))
contract = w3.eth.contract(address=erc20_contract_address, abi=erc20_contract_abi)

# Ensure media directory exists
os.makedirs(media_directory, exist_ok=True)

def load_local_posts():
    if os.path.exists(local_store_file):
        with open(local_store_file, 'r') as file:
            return json.load(file)
    return []

def save_local_posts(posts):
    with open(local_store_file, 'w') as file:
        json.dump(posts, file, indent=4)

def download_media(url, local_filename):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(local_filename, 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Downloaded media: {local_filename}")
    else:
        print(f"Failed to download media from {url}")

def transfer_tokens(amount):
    nonce = w3.eth.getTransactionCount(from_address)
    txn = contract.functions.transfer(to_address, amount).buildTransaction({
        'chainId': 1, # Mainnet chain ID or testnet ID
        'gas': 2000000,
        'gasPrice': w3.toWei('5', 'gwei'),
        'nonce': nonce
    })

    signed_txn = w3.eth.account.sign_transaction(txn, private_key=private_key)
    txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    print(f"Tokens transferred: {txn_hash.hex()}")

# Step 1: Load local posts
local_posts = load_local_posts()
latest_local_post_time = None

if local_posts:
    latest_local_post_time = max(
        datetime.strptime(post['created_time'], "%Y-%m-%dT%H:%M:%S%z") for post in local_posts
    )

# Step 2: Fetch new posts from Facebook
fb_graph_url = f'https://graph.facebook.com/v12.0/{facebook_page_id}/posts'
params = {
    'access_token': access_token,
    'fields': 'message,created_time,link,permalink_url,attachments{media_type,media_url}',
    'limit': 100
}

new_posts = []
while True:
    response = requests.get(fb_graph_url, params=params)
    data = response.json()
    
    for post in data.get('data', []):
        post_time = datetime.strptime(post['created_time'], "%Y-%m-%dT%H:%M:%S%z")
        if not latest_local_post_time or post_time > latest_local_post_time:
            if 'attachments' in post:
                attachments = post['attachments']['data']
                for attachment in attachments:
                    media_type = attachment.get('media_type')
                    media_url = attachment.get('media_url')

                    if media_type in ['photo', 'video']:
                        parsed_url = urlparse(media_url)
                        file_name = os.path.basename(parsed_url.path)
                        local_file_path = os.path.join(media_directory, file_name)

                        download_media(media_url, local_file_path)

                        post['message'] = post['message'].replace(media_url, local_file_path)

            new_posts.append(post)
        else:
            break

    if 'paging' in data and 'next' in data['paging'] and not new_posts:
        fb_graph_url = data['paging']['next']
    else:
        break

if new_posts:
    print(f"Found {len(new_posts)} new posts.")
    local_posts.extend(new_posts)
    save_local_posts(local_posts)
    
    # Reward contribution with tokens
    transfer_tokens(reward_amount)
else:
    print("No new posts found.")

# Step 4: Post to your blog
blog_api_url = 'https://yourblog.com/wp-json/wp/v2/posts'
headers = {
    'Authorization': 'Bearer YOUR_BLOG_API_TOKEN',
    'Content-Type': 'application/json'
}

for post in new_posts:
    post_title = post.get('message', '')[:50]
    post_content = post.get('message', '')
    post_link = post.get('permalink_url', '')

    blog_post_data = {
        'title': post_title,
        'content': f"{post_content}\n\nRead more on Facebook: {post_link}",
        'status': 'publish'
    }
    
    response = requests.post(blog_api_url, headers=headers, data=json.dumps(blog_post_data))
    if response.status_code == 201:
        print(f"Post published: {post_title}")
    else:
        print(f"Failed to publish post: {response.status_code}")
