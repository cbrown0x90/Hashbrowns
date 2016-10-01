import re
from robobrowser import RoboBrowser

browser = RoboBrowser(history=True)
browser.open('http://emowire.com/forums')

boards = browser.select('div.forum_title a')

for board in boards:
    browser.follow_link(board)
    posts = browser.select('div.forum_topics_title a')
    for post in posts:
        browser.follow_link(post)
        text = browser.select('div.forum_topic_posts_info_body')
        for tag in text:
            print(tag.text.strip())
        browser.back()
    browser.back()

#print(out)
