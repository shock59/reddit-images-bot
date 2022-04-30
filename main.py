import praw, json, datetime

configFile = open("config.json", "r")
config = configFile.read()
config = json.loads(config)
configFile.close()

def main():
    reddit = praw.Reddit(
        client_id=config["creds"]["id"],
        client_secret=config["creds"]["secret"],
        user_agent=config["creds"]["user_agent"],
    )

    prevImagesFile = open("prevImages.txt", "r")
    prevImages = prevImagesFile.read().split("\n")
    prevImagesFile.close()
    prevImagesFile = open("prevImages.txt", "a")

    dt = datetime.datetime.now()
    timeString = dt.strftime("%Y-%m-%d")

    for category in config["categories"]:

        # Loop through subreddits and posts in the subreddit
        for subreddit in config["categories"][category]["subreddits"]:
            for submission in reddit.subreddit(subreddit["name"]).hot():

                # Get only image posts, that also aren't stickied or nsfw if required
                if submission.stickied and not subreddit["pins"]:
                    continue
                if submission.over_18 and not subreddit["nsfw"]:
                    continue

                url = submission.url  
                if url.endswith(".jpg") or url.endswith(".jpeg") or url.endswith(".png"):
                    if not url in prevImages:
                        prevImagesFile.write(url + "\n")
                        imageData = {
                            "url": url,
                            "original": "https://www.reddit.com" + submission.permalink,
                            "author": submission.author.name
                        }
                        imageData = json.dumps(imageData)
                        imageFile = open("images/" + category + "/" + timeString + ".json", "w")
                        imageFile.write(imageData)
                        break

    prevImagesFile.close()

if __name__ == "__main__":
    main()