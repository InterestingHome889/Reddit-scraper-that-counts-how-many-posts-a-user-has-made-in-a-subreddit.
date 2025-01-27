import praw
import pandas as pd
from datetime import datetime, timedelta

# Your Reddit API credentials (replace with your actual credentials)
client_id = 'your_client_id'         # Your client_id from Reddit
client_secret = 'your_client_secret'  # Your client_secret from Reddit
user_agent = 'your_user_agent'  # Your user agent string. Make sure your user_agent is unique and clearly describes your application (e.g., 'windows:YourAppName:v1.0 (by )').

# Initialize Reddit instance
reddit = praw.Reddit(
    client_id=client_id,
    client_secret=client_secret,
    user_agent=user_agent
)

# Choose the subreddit you want to scrape (e.g., 'learnpython')
subreddit_name = 'subreddit'  # Change to the subreddit of your choice

# Define the time window (30 days ago)
time_window = datetime.utcnow() - timedelta(days=30)  # Changed to 30 days

# Initialize a dictionary to keep track of post counts per user
user_post_count = {}

# Fetch the new posts from the subreddit
for submission in reddit.subreddit(subreddit_name).new(limit=100):  # Fetching 100 posts
    # Check if the post was created within the last 30 days
    post_time = datetime.utcfromtimestamp(submission.created_utc)
    if post_time > time_window:
        user = submission.author.name if submission.author else None
        if user:
            # Count the posts per user
            if user not in user_post_count:
                user_post_count[user] = 1
            else:
                user_post_count[user] += 1

# Convert the dictionary to a list of tuples for creating a DataFrame
user_data = [(user, count) for user, count in user_post_count.items()]

# Create a DataFrame
df = pd.DataFrame(user_data, columns=["Username", "Post Count"])

# Save the data to a CSV file
df.to_csv(f"{subreddit_name}_user_post_counts.csv", index=False)

# Print the DataFrame to the console
print(df)
