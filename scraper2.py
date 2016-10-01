import re
from robobrowser import RoboBrowser

def is_ascii(s):
    return all(ord(c) < 128 for c in s)

def remove_html_markup(s):
    tag = False
    quote = False
    out = ""

    for c in s:
            if c == '<' and not quote:
                tag = True
            elif c == '>' and not quote:
                tag = False
            elif (c == '"' or c == "'") and tag:
                 quote = not quote
            elif not tag:
                out = out + c

    return out

browser = RoboBrowser(history=True)
browser.open('http://emowire.com/forums')

boards = browser.select('div.forum_title a')

for board in boards:
    browser.follow_link(board)
    posts = browser.select('div.forum_topics_title a')
    print(posts)
    for post in posts:
        browser.follow_link(post)
        text = browser.select('div.forum_topic_posts_info_body')
        for tag in text:
            if (is_ascii(tag.text.strip())):
                print(remove_html_markup(tag.text.strip()))
            else:
                 continue
        
        browser.back()
    browser.back()

#print(out)
