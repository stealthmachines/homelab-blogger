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


Here's a summary of the one-click homelab solution:

1. Application Structure
/homelab: Root directory containing the main services.
/app: Handles Facebook post management, media download, and ERC20 token rewards.
/webform: Provides a web interface for configuring application settings.
/discovery: A service for network participants to register and discover each other.
/extension: A Chrome extension for users to discover and interact with other homelab participants.
2. Key Components
Backend Application (app.py): Automates Facebook post handling, downloads media, and manages token rewards.
Web Form (app.py): Allows users to input configuration details via a simple HTML form.
Discovery Service (discovery_service.py): Registers and lists active nodes in the homelab network.
Chrome Extension: Provides a UI for discovering and interacting with other network nodes.
3. Deployment
Docker Compose: Manages the deployment of all services with a single command (docker-compose up --build).
Configuration: Accessible via a web form at http://localhost:5000.
Discovery: Active nodes can be found at http://localhost:6000/nodes.
Extension: Chrome extension allows easy network interaction.
4. Files and Configuration
Dockerfiles: Each service has its own Dockerfile for setting up the environment.
Configuration (config.env): Stores environment variables for Facebook and Ethereum settings.
HTML Templates: Used for the web form and extension UI.
This setup enables users to easily deploy, configure, and join a homelab network, where instances can automatically discover and interact with each other using a search engine homepage.

Feel free to customize and extend the solution to suit your needs!
