## How to
The following procedure shows how to install this project on a Linux web server running Ubuntu 14.04. The following instructions work behind a firewall so long as the web server has access to your GitLab and Mattermost instances. 

To install this project using a Linux-based web server, you will need a Linux/Ubuntu 14.04 web server supporting Python 2.7 or a compatible version. Other compatible operating systems and Python versions should also work. 

Here's how to start:

1. **Set up this project to run on your web server**
 1. Set up a **Linux Ubuntu 14.04** server either on your own machine or on a hosted service, like AWS.
 2. **SSH** into the machine, or just open your terminal if you're installing locally
 3. Confirm **Python 2.7** or a compatible version is installed by running:
    - `python --version` If it's not installed you can find it [here](https://www.python.org/downloads/)
 4. Install **pip** and other essentials
    - `sudo apt-get install python-pip python-dev build-essential`
 5. Clone this GitHub repo with
    - `git clone https://github.com/numberly/mattermost-integration-giphy.git`
    - `cd mattermost-integration-giphy`
 6. Install integration requirements
    - `sudo python setup.py install`

2. **Set up your Mattermost outgoing webhooks**
 1. Log in to your Mattermost account. Click the three dot menu at the top of the left-hand side and go to **Account Settings** > **Integrations** > **Outgoing Webhooks**
 2. Under *Add a new outgoing webhook*, leave the *Channel* unselected and enter `gif:` into *Trigger Words*. You may select a channel if you only want this integration to be available in a specified channel
 3. Paste your Web Server domain into *Callback URLs*, making sure to add `http://` to the beginning and `/new_post` to the end so it looks similar to `http://<your-web-server-domain>/new_post` and click **Add**
 4. Copy the *Token* from your newly created webhook that appears under the *Existing outgoing webhooks* section

3. **Set up your Mattermost slash command**
 1. Log in to your Mattermost account. Click the three dot menu at the top of the left-hand side and go to **Account Settings** > **Integrations** > **Slash Commands**
 2. Under *Add a new command*, enter `/gif` into **Command Trigger Word**
 3. Paste your Web Server domain into *Callback URLs*, making sure to add `http://` to the beginning
 4. Select `POST` method
 5. (optional) Choose a username and icon url
 6. (optional) Check the autocomplete checkbox, add `[KEYWORD]` as the hint, `Returns a GIF from Giphy based on the keyword` as the description and `Get a GIF from Giphy` as the descriptive label
 7. Copy the *Token* from your newly created slash command that appears under the *Existing commands* section

4. **Run the server with the correct configuration**
 1. Back on SSH or your terminal, add the following lines to your `~/.bash_profile`
    - `export MATTERMOST_GIPHY_TOKEN=<your-token-here>` This is the token you copied in the last section
    - `export MATTERMOST_GIPHY_HOST=<your-host>` or `export HOST=<your-host>` The host you want the integration (defaults to 0.0.0.0)
    - `export MATTERMOST_GIPHY_PORT=<your-port-number>` or `export PORT=<you-port-number>` The port number you want the integration to listen on (defaults to 5000)
 2. Source your bash profile
    - `source ~/.bash_profile`
 3. Run the server
    - `python run.py`

That's it! You should be able to type `gif: hello` or `/gif hello` into any channel and see a GIF from Giphy's translate service.


## Production setup
If you'd like to use this integration in a production envrionment, it is strongly recommended that you get a production Giphy API key from [here](http://api.giphy.com/submit). Once you have that you can configure the integration to use it:

1. Stop the process currently running the integration
1. Add the following lines to your `~/.bash_profile` or `~/.bashrc` 
   - `export GIPHY_API_KEY=<your-api-key-here>` With your Giphy API key
2. Source your bash profile
   - `source ~/.bash_profile` or `source ~/.bashrc`
3. Run the server again
   - `python run.py`
