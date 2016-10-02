#!/bin/env python

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

browser = RoboBrowser(history=True, parser='html.parser')
browser.open('https://7chan.org/x/catalog.html')

while True:
    posts = browser.select('td a')
    print("We found %d threads" % len(posts))
    for post in posts:
        browser.follow_link(post)
        text = browser.select('p.message')[0]
        for tag in text:
            if type(tag.string) != type(None) and is_ascii(tag.string.strip()):
                print(remove_html_markup(tag.string.strip()))
            else:
                continue
