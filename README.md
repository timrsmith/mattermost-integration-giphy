# Giphy Integration Service for Mattermost
This integrations service is used to enable an external search engine ([Giphy](https://en.wikipedia.org/wiki/Giphy)) to be queried based on commands issued in a Mattermost channel using Mattermost [outgoing webhooks](https://github.com/mattermost/platform/blob/master/doc/integrations/webhooks/Outgoing-Webhooks.md). 

Once installed, users can type `gif: keyword` to send a query to the Giphy search engine and return with a post containing one non-deterministic search result from the Giphy database of animated GIF files matching `keyword`. The animation will appear below in the posted message. 

Powered by [Giphy](http://giphy.com/).

## Project Goal
The goal of this project is to provide a fully-functional template on which the Mattermost community can create their own integration services. Community members are invited to fork this repo to add improvements and to create new integrations. 

To have your work included on the [Mattermost integrations page](http://www.mattermost.org/community-applications/), please mail info@mattermost.com or tweet to [@MattermostHQ](https://twitter.com/mattermosthq). 

## Requirements
To run this integration you need:

1. A **web server** supporting Python 2.7 or compatible versions.
2. A **[Mattermost account](http://www.mattermost.org/)** [where outgoing webhooks are enabled](https://github.com/mattermost/platform/blob/master/doc/integrations/webhooks/Outgoing-Webhooks.md#enabling-outgoing-webhooks)

Many web server options will work, below we provide instructions for [**Heroku**](HEROKU.md) and a general [**Linux/Ubuntu**](LINUX.md) server.

### Heroku-based Install
[**Here**](HEROKU.md)

### Linux/Ubuntu 14.04 Web Server Install
[**Here**](LINUX.md)
