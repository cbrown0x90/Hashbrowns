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
browser.open('http://www.emopuddle.com/')

boards = browser.select('td.col_c_forum a')
boards = boards[6:]
boards = boards[:-1]
del boards[3]
#print(boards)

for board in boards:
    browser.follow_link(board)
    while True:
        nextPage = browser.select('li.next a')
        posts = browser.select('a[class="topic_title"]')
        #posts = browser.select('td.col_f_content a')
        for post in posts:
            #print(post)
            #print(post['title'])
            if is_ascii(post['title']):
            #print(post)
                browser.follow_link(post)
                while True:
                    nextPostPage = browser.select('li.next a')
                    text = browser.select('div.entry-content')
                #print(nextPage)
                    for tag in text:
                        if (is_ascii(tag.text.strip())):
                            print(remove_html_markup(tag.text.strip()))
                        else:
                            continue
                    if not nextPostPage:
                        break
                    browser.follow_link(nextPostPage[0])

        if not nextPage:
            break
        browser.follow_link(nextPage[0])
