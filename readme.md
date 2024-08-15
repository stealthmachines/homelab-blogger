# Homelab One-Click Solution

This project provides a one-click solution for deploying a homelab that includes automated Facebook post handling, media download, and interaction with an ERC20 token-based reward system. It also includes a discovery service for network participants and a Chrome extension for easy access to the network.

## Setup Instructions

1. **Clone the repository:**
    ```bash
    git clone https://github.com/stealthmachines/homelab-blogger.git
    cd homelab-blogger
    ```

2. **Configuration:**
   - Visit `http://localhost:5000` to configure your Facebook and Ethereum settings.
   - Fill in the required fields and save the configuration.

3. **Build and Run the Services:**
    ```bash
    docker-compose up --build
    ```

4. **Accessing the Services:**
   - The backend service will be available at `http://localhost`.
   - The webform for configuration will be available at `http://localhost:5000`.
   - The discovery service will be available at `http://localhost:6000`.

5. **Install the Chrome Extension:**
   - Load the `extension` directory as an unpacked extension in Chrome.
   - Use the extension to discover and interact with other homelab participants.

6. **Enjoy your homelab!**

## Components

- **App:** Handles Facebook posts, media downloads, and ERC20 token rewards.
- **Webform:** Configures the application settings.
- **Discovery:** Allows network participants to register and discover each other.
- **Extension:** Chrome extension for network search and interaction.

Feel free to customize and extend the solution to suit your needs!
