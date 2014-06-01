import sys
import os

import urllib.request

from celery import Celery


app = Celery('arch4chan_worker', backend='redis://localhost:6379/4', broker='redis://localhost:6379/5')

@app.task
def download_derpibooru(image_url, tag):
    if not os.path.exists(tag):
        os.makedirs(tag)
    urllib.request.urlretrieve("http:"+image_url,tag+'/'+image_url.split("/")[-1])

