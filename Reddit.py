import praw

reddit = praw.Reddit(client_id='fYRWm5jkNOpIWA', client_secret='zKi7IdnZZ-5xDxw_jc-HBZpEjN0HZQ', user_agent='RedBat')

hot_posts = reddit.subreddit('wallstreetbets').new(limit=10)

for post in hot_posts:
    print(post.url)
    print(post.title)
    print(post.selftext)