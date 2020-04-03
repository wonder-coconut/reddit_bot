import praw

#reddit api login
reddit = praw.Reddit(client_id='HW6AYqkTBgEgyQ',
                     client_secret=getToken(),
                     username='myfoot_mytutor',
                     password='03Rishab',
                     user_agent='myfootmytutor by u/wonder_coconut')

def getToken():
    tokenFile = open('/home/wondercoconut/python3/botshit/token.txt','r')
    tokentxt = tokenFile.read()
    Token = tokentxt.split('\n')
    return Token[1]

subreddit = reddit.subreddit('prosperolickmyfeet')

key1 = 'no u'
key2 = 'crackerjack'

f=1
for comment in subreddit.stream.comments():
    if key1 in comment.body:
        comment.reply("no u")
        f=0

if f:
    for comment in subreddit.stream.comments():
        if key2 in comment.body:
            comment.reply('my feet are bigger than yours')

