import praw
import time
import datetime
import pandas as pd

str_subdir = 'Files/New/'
df_all_posts = pd.read_csv('posts.csv')
features = ['Title', 
            'Score', 
            'Id', 
            'Subreddit', 
            'URL', 
            'Is_Original_Content', 
            'Num_comments', 
            'Flair', 
            #'Selftext', 
            'Author',
            'Created']

obj_reddit = praw.Reddit(client_id='fYRWm5jkNOpIWA', client_secret='zKi7IdnZZ-5xDxw_jc-HBZpEjN0HZQ', user_agent='RedBat')
int_count = 1

while True:
    list_posts = [] 
    obj_subredit = obj_reddit.subreddit('wallstreetbets')
    for post in obj_subredit.new():
        list_posts.append([post.title.encode('utf8'), 
                          post.score, 
                          post.id, 
                          post.subreddit, 
                          post.url, 
                          post.is_original_content, 
                          post.num_comments, 
                          post.link_flair_text, 
                          #post.selftext, 
                          post.author,
                          datetime.datetime.utcfromtimestamp(post.created)])
        #print(type(post.selftext))
        file_post = open(str_subdir + post.id + ".txt", 'wb')
        file_post.write(post.selftext.encode('utf8')) 
        file_post.close()
    df_new_posts = pd.DataFrame(list_posts, columns=features)
    df_all_posts = pd.concat([df_all_posts, df_new_posts]).drop_duplicates().reset_index(drop=True)
    df_all_posts.to_csv('posts.csv')
    print('Running! Exectued once at: ' + datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    int_count += 1
    if(int_count>9):
        break
    time.sleep(60)
    