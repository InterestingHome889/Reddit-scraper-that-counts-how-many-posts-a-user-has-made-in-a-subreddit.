Hello! I created a Reddit scraper with ChatGPT that counts how many posts a user has made in a specific subreddit over a given time frame. The results are saved to a CSV file (Excel), making it easy to analyze user activity in any subreddit you’re interested in. This code works on Python 3.7+.

How to use it:

1. To set up Reddit API access go to [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps) to register your application on Reddit’s developer platform. Click on 'Create App', select 'script', then choose a name for your app. The description can be something simple like 'A script to scrape and analyze user activity in specific subreddits.' You can set the redirect URL to http://localhost as it is the default. Once your app is created, note down the client_id and client_secret, as you’ll use these in the script.  
client_id is located right under the app name, client_secret is at the same page noted with 'secret'. Your user_agent is a string you define in your code to identify your app, formatted like this: "platform:AppName:version (by u/YourRedditUsername)". For example, if your app is called "RedditScraper" and your Reddit username is JohnDoe, you would set it like this: "windows:RedditScraper:v1.0 (by u/JohnDoe)".

2. Install Python 3.7 or later, then install the required Reddit libraries. Open Command Prompt as administrator on Windows or Terminal on Mac and Linux, and type:  
`pip install pandas praw`  
If you encounter a permissions error use sudo:  
`sudo pip install pandas praw`  
After that verify their installation:  
`python -m pip show praw pandas` OR `python3 -m pip show praw pandas`

3. Download or copy and paste the code that is in `reddit_scraper.py`

4. Replace the placeholders with your actual credentials:  
`client_id = 'your_client_id'`  
`client_secret = 'your_client_secret'`  
`user_agent = 'your_user_agent'`  
Set the subreddit name you want to scrape. For example, if you want to scrape posts from r/learnpython, replace 'subreddit' with 'learnpython'.  
The script will fetch the latest 100 posts from the chosen subreddit. To adjust that, you can change the 'limit=100' in the following line to fetch more or fewer posts:  
`for submission in reddit.subreddit(subreddit_name).new(limit=100): # Fetching 100 posts`  
You can modify the time by changing 'timedelta(days=30)' to a different number of days, depending on how far back you want to get user posts:  
`time_window = datetime.utcnow() - timedelta(days=30) # Set the time range`

5. The code goes through the posts, counts how many times each user has posted in the last 30 days (or how many days you set), and saves this data to a CSV (Excel) file named after the subreddit. For example, if you’re scraping learnpython, the file will be named `learnpython_user_post_counts.csv`

Keep in mind that scraping too many posts in a short period of time could result in your account being flagged or banned by Reddit, ideally to NO MORE than 100–200 posts per request. It's important to set reasonable limits to avoid any issues with Reddit's API or community guidelines.

## Disclaimer

This script is for educational purposes only. By using this script, you agree that you are responsible for adhering to Reddit's terms of service and API usage guidelines. **Do not scrape or interact with Reddit in a manner that violates its terms of service**. Excessive scraping or misuse of the Reddit API could lead to your account being banned.

Please use this script responsibly and avoid making requests that could overload Reddit’s servers.

