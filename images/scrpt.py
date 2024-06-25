import requests
import os

head = "http://210.212.217.214/r_20_twenty/"
ids = ["R20" + str(i).zfill(4) + ".jpg" for i in range(1, 1112)]

for id_ in ids:
    if not os.path.exists("./" + id_):
        res = requests.get(head + id_)
        if res.headers["Content-Type"] == "image/jpeg":
            open("./new/" + id_, "wb").write(res.content)
            print(id_)
