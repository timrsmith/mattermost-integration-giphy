## How to
To install this project using Heroku, you will need: 

1. A Heroku account, available for free from [Heroku.com](http://heroku.com)
2. A GitHub account, available for free from [GitHub.com](http://github.com)

Here's how to start:

1. **Create a copy of this project to manipulate**
  1. Log in to your GitHub account. Go to the [Github repository of this project](https://github.com/numberly/mattermost-integration-giphy/) click **Fork** in the top-right corner to create a copy of this project that you can control and manipulate

2. **Deploy your project copy to Heroku**
  1. Go to your [Heroku Dashboard](https://dashboard.heroku.com/apps) and click **+** in the top-right corner then **Create New App** 
  2. Give your app a unqiue name (like `mattermost-giphy-[YOUR_GITHUB_USERNAME]`), select your region and click **Create App**
  2. Heroku directs you to the *Deploy* tab of the dashboard for your new app, select **GitHub** as your connection option, then click **Connect to GitHub** at the bottom of the screen to authorize Herkou to access your GitHub account
  3. In the pop up window, click **Authorize Application** to allow Heroku to access your accounts repositories. This step does not apply if you've already connected your GitHub account to Heroku. 
  4. On your Heroku dashboard, select your GitHub account in the first drop-down, type `mattermost-integration-giphy` in the *repo-name* field, then click **Search** and then the **Connect** button once Heroku finds your repository
  4. Scroll to the bottom of the new page. Under the *Manual Deploy* section, make sure the **master** branch is selected then click **Deploy Branch**. After a few seconds you'll see a confirmation that the app has been deployed
  5. At the top of your app dashboard, click on the **Settings** tab and scroll down to the *Domains* section. Copy the URL below *Heroku Domain* (we'll refer to this as `http://<your-heroku-domain>/` and we'll need it in the next step)
  6. Leave your Heroku interface open as we'll come back to it to finish the setup

3. **Connect your project to your Mattermost account for outgoing webhooks**
 1. Log in to your Mattermost account. Click the three dot menu at the top of the left-hand side and go to **Account Settings** > **Integrations** > **Outgoing Webhooks**
 2. Under *Add a new outgoing webhook*, leave the *Channel* unselected and enter `gif:` into **Trigger Words**. You may select a channel if you only want this integration to be available in a specified channel
 3. Paste your Heroku domain into *Callback URLs*, making sure to add `http://` to the beginning and `/new_post` to the end so it looks similar to `http://myapp.heroku.com/new_post` and click **Add**
 4. Copy the *Token* from your newly created webhook that appears under the *Existing outgoing webhooks* section
 5. Go back to your Heroku app dashboard under the *Settings* tab. Under the *Config Variables* section, click **Reveal Config Vars**
 6. Type `MATTERMOST_GIPHY_TOKEN` as the *KEY* and paste in the token you copied as the *VALUE*, and click **Add**

4. **Connect your project to your Mattermost account for slash commands**
 1. Log in to your Mattermost account. Click the three dot menu at the top of the left-hand side and go to **Account Settings** > **Integrations** > **Slash Commands**
 2. Under *Add a new command*, enter `/gif` into **Command Trigger Word**
 3. Paste your Heroku domain into *Callback URLs*, making sure to add `http://` to the beginning
 4. Select `POST` method
 5. (optional) Choose a username and icon url
 6. (optional) Check the autocomplete checkbox, add `[KEYWORD]` as the hint, `Returns a GIF from Giphy based on the keyword` as the description and `Get a GIF from Giphy` as the descriptive label
 7. Copy the *Token* from your newly created slash command that appears under the *Existing commands* section
 8. Go back to your Heroku app dashboard under the *Settings* tab. Under the *Config Variables* section, click **Reveal Config Vars**
 9. Type `MATTERMOST_GIPHY_TOKEN` as the *KEY* and paste in the token you copied as the *VALUE*, and click **Add**

That's it! Waiting a few minutes for the Heroku process to restart you should be able to type `gif: hello` or `/gif hello` into any channel and see a GIF from Giphy's translate service.


## Production setup:
If you'd like to use this integration in a production envrionment, it is strongly recommended that you get a production Giphy API key from [here](http://api.giphy.com/submit). Once you have that you can configure the integration to use it:

1. Go to your [Heroku Dashboard](https://dashboard.heroku.com/apps) and click on your app
2. Click the **Settings** tab. Under the *Config Variables* section, click **Reveal Config Vars**
3. For *KEY* type in `GIPHY_API_KEY` and for *VALUE* paste in your Giphy API key, then click **Add**
4. Wait a minute for the Heroku process to restart
