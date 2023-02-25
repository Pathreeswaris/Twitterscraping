PROJECT OVERVIEW
The goal of this project is to scrape and analyze tweets related to a specific topic using Twitter API, GetOldTweets3, and MongoDB Atlas. The main steps of the project include:

Scrape tweets using Twitter API:
Connect to Twitter API using Tweepy
Scrape tweets from a specific user account
Store the scraped tweets in a Pandas dataframe
Store scraped tweets in MongoDB Atlas:
Connect to MongoDB Atlas using PyMongo
Insert scraped tweets into a MongoDB collection
Scrape tweets using GetOldTweets3:
Scrape tweets based on a specific keyword and date range
Store the scraped tweets in a Pandas dataframe
Load tweets from MongoDB Atlas using PyMongo:
Connect to MongoDB Atlas using PyMongo
Retrieve tweets from a MongoDB collection and store them in a Pandas dataframe
Visualize and analyze the scraped tweets:
Use Streamlit to create a web-based dashboard to analyze and *visualize the scraped tweets
Display the number of tweets scraped
Display the scraped tweets in a table format
Plot the top hashtags used in the scraped tweets
Plot the number of tweets scraped per day This project leverages several technologies and tools to scrape, store, and analyze tweets. The use of Twitter API and GetOldTweets3 allows for the scraping of large amounts of tweets, while MongoDB Atlas provides a scalable and efficient way to store and manage the scraped data. The use of Streamlit enables the creation of a user-friendly dashboard that allows for easy analysis and visualization of the scraped tweets.
In summary, this project aims to provide a way to scrape and analyze tweets related to a specific topic using a combination of various technologies and tools. It can be further extended to include additional features such as sentiment analysis and predictive modeling to provide deeper insights into the scraped tweets.
