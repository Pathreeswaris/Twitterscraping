import os
import pandas as pd
import pymongo
import streamlit as st
from datetime import date
import GetOldTweets3 as got
from scraper import scrape_tweets
from database import insert_to_mongo

def main():
    st.set_page_config(page_title='Twitter Analysis', layout='wide')
    st.title('Twitter Analysis')

    # Scrape tweets using GetOldTweets3
    st.header('Scrape tweets using GetOldTweets3')
    keyword = st.text_input('Enter the keyword:', 'Youtube')
    start_date = st.date_input('Enter the start date:', value=pd.to_datetime('2019-01-01').date())
    end_date = st.date_input('Enter the end date:', value=pd.to_datetime('today').date())
    tweet_count = st.number_input('Enter the number of tweets to scrape:', value=100)
    if st.button('Scrape tweets'):
        tweets_list = scrape_tweets(keyword, start_date, end_date, tweet_count)
        df = pd.DataFrame(tweets_list)
        st.write('Number of rows:', df.shape[0])
        st.dataframe(df)

    # Load tweets from MongoDB Atlas using PyMongo
    st.header('Load tweets from MongoDB Atlas using PyMongo')
    docs = insert_to_mongo()
    df_mongo = pd.DataFrame(docs)
    if not df_mongo.empty:
        st.write('Number of rows:', df_mongo.shape[0])
        st.dataframe(df_mongo)
    else:
        st.write('No tweets found in the database')