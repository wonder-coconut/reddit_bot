import praw

#reddit api login
reddit = praw.Reddit(client_id='HW6AYqkTBgEgyQ',
                     client_secret='8u6ws5p6dKEPx63F-PmBwYt-e-k',
                     username='myfoot_mytutor',
                     password='03Rishab',
                     user_agent='myfootmytutor by u/wonder_coconut')

subreddit = reddit.subreddit('prosperolickmyfeet')

keyphrase = 'crackerjack'

for comment in subreddit.stream.comments():
    if keyphrase in comment.body:
        comment.reply("my feet are bigger than yours")
