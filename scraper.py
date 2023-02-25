import GetOldTweets3 as got
def scrape_tweets(keyword, start_date, end_date, tweet_count):
    # Scrape tweets using GetOldTweets3
    tweets = got.manager.TweetCriteria().setQuerySearch(keyword)\
                                        .setSince(start_date.strftime("%Y-%m-%d"))\
                                        .setUntil(end_date.strftime("%Y-%m-%d"))\
                                        .setMaxTweets(tweet_count)\
                                        .setLang("en")\
                                        .setEmoji("unicode")\
                                        .setUsername("username")\
                                        .setTopTweets(False)\
                                        .setNear("")\
                                        .setWithin("15mi")\
                                        .setSinceId(0)\
                                        .setMaxId(0)\
                                        .setRefreshCursor(0)\
                                        .setEmoji("unicode")\
                                        .setTweetType("recent")\
                                        .setLangDetection(False)\
                                        .setProxy("")

    # Create a list of dictionaries to store the scraped tweets
    tweets_list = []
    for tweet in got.manager.TweetManager.getTweets(tweets):
        tweet_dict = {'id': tweet.id,
                      'date': tweet.date,
                      'text': tweet.text,
                      'hashtags': tweet.hashtags,
                      'username': tweet.username,
                      'retweets': tweet.retweets,
                      'favorites': tweet.favorites,
                      'mentions': tweet.mentions,
                      'permalink': tweet.permalink}
        tweets_list.append(tweet_dict)
    return tweets_list