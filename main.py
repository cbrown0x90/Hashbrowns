import sample
import secret
from tumblpy import Tumblpy

client = secret.main();

post = sample.main()
client.post('post', 'http://xxxt1ll14mw4nxxx.tumblr.com/', params={'type':'text', 'body':post})
