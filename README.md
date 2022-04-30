# reddit-images-bot

A customisable bot to scrape images from subreddits. Built using Python 3 and [PRAW](https://github.com/praw-dev/praw). It can be configured to collect a custom amount of images from multiple groups of subreddits at once and saves the links in JSON files in the `images` directory.

## Setup and configuration

You will need [Reddit API credentials](https://www.reddit.com/prefs/apps) as well Python 3 installed. You will also need PRAW, which you can install from pip using `pip install praw`.
Then clone or [download](https://github.com/shock59/reddit-images-bot/archive/refs/heads/main.zip) the repository and create a `config.json` file.

Add your Reddit credentials:
```json
{
  "creds": {
    "id": "your id",
    "secret": "your secret",
    "user_agent": "your user agent"
  }
}
```
Add categories:
```json
{
  "creds": { ... }

  "categories": {
    "category name": {
      "number": 1 , // Number of images to get
      "subreddits": [
        {
          "name": "subreddit name",
          "nsfw": false, // Allow fetching NSFW or pinned posts (true/false)
          "pins": false
        }
      ]
    }
  }
}
```

Create an `images` directory and subdirectories with the same name as all your categories. Also create a blank `prevImages.txt` file

## Todo

- Improve README
- Automatically create directories and `prevImages.txt`
- Logs
- More customisation options