#Written by X41
#Modified by plueschopath & Centzilius

import json
import urllib.request
import sys
import time
import pickle

from tasks import download_derpibooru

page = 1
pic = 0
key = "KEYHEREPLS"
tag = ' '.join(sys.argv[1:])
if len(sys.argv) == 1:
    print("Usage: DerpibooruDownloader.py [tag1], [tag2], [tag3], [tag4].....")
    exit()
data = ""

class DirtyProgramming:
    pass

vars = DirtyProgramming()


try:
    with open("save_vars.pickle", "rb") as f:
        v = pickle.load(f)

    vars.pics = v.__dict__['pics']

except:
    vars.pics = {}

    print('not loading save_vars.pickle ... doesn\'t exist or something like this')

while True:
    print('page: ' + str(page))
    url = "http://derpibooru.org/search.json?q=" + str(tag) + "&page=" + str(page) + "&key=" + str(key)
    try:
        json_data = urllib.request.urlopen(url).read().decode("utf-8")
        data = json.loads(json_data)['search']
        if data == []:
            page = 0
            print('end reached')
            time.sleep(3600)
        for entry in data:
            if entry['image'] not in vars.pics:
                print('new image found: '+entry['image'])
                vars.pics[entry['image']] = download_derpibooru.delay(entry['image'], tag)
                with open("save_vars.pickle", "wb") as f:
                    f.write(pickle.dumps(vars))
        page += 1
    except KeyboardInterrupt:
        print('FUCKUP')
        exit()
    except:
        print('failed... move on')

