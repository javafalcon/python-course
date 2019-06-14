from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
def getHTMLText(url,coding='gbk'):
    try:
        r = requests.get(url,timeout=30)
        print(r)
        r.raise_for_status()
        r.encoding = coding
        return r.text
    except:
        return ""


def downloadImageFile(imgUrl, destUrl, fname=''):
    local_filename = imgUrl.split('/')[-1]
    print('Download Image File={}'.format(local_filename))
    try:
        r = requests.get(imgUrl, stream=True)
        r.raise_for_status()

        if len(fname) == 0:
            fname = local_filename
        print('fname={}'.format(fname))
        with open(destUrl + "/" + fname, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()
            f.close()
        return r.status_code
    except:
        return r.status_code


