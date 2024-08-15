from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        facebook_page_id = request.form.get('facebook_page_id')
        access_token = request.form.get('access_token')
        erc20_contract_address = request.form.get('erc20_contract_address')
        erc20_contract_abi = request.form.get('erc20_contract_abi')
        ethereum_provider = request.form.get('ethereum_provider')
        from_address = request.form.get('from_address')
        private_key = request.form.get('private_key')
        to_address = request.form.get('to_address')
        reward_amount = request.form.get('reward_amount')

        with open('/app/config.env', 'w') as f:
            f.write(f"FACEBOOK_PAGE_ID={facebook_page_id}\n")
            f.write(f"ACCESS_TOKEN={access_token}\n")
            f.write(f"ERC20_CONTRACT_ADDRESS={erc20_contract_address}\n")
            f.write(f"ERC20_CONTRACT_ABI={erc20_contract_abi}\n")
            f.write(f"ETH_PROVIDER={ethereum_provider}\n")
            f.write(f"FROM_ADDRESS={from_address}\n")
            f.write(f"PRIVATE_KEY={private_key}\n")
            f.write(f"TO_ADDRESS={to_address}\n")
            f.write(f"REWARD_AMOUNT={reward_amount}\n")

        return "Configuration saved successfully! You can now run the Docker container."

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
