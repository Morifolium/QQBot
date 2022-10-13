from cgitb import small
from email import message
import json

import requests
import re
import random

"下面这个函数用来判断信息开头的几个字是否为关键词"
"如果是关键词则触发对应功能，群号默认为空"


def keyword(message, uid, gid=None):
    if message[0:2] == "色图":
        return setu(uid, gid, message[2:])
        pass
    elif message[0:2] == "萝莉":
        return loli(uid, gid)
    """
    if message[0:3] == "余悉越":
        return yxy(uid, gid)
    if message[0:3] == "陈金宝":
        return cjb(uid, gid)
    """


# api的POST方法貌似没有做好
def setu(uid, gid, message):
    if gid != None:
        message = message.split(" ")
        tag = []
        for i in message:
            if len(i) > 0:
                tag.append(i)
        v2_url = "https://api.lolicon.app/setu/v2"
        setu_json = requests.post(url=v2_url, data={"tag": tag})
        setu_url = setu_json.json()["data"][0]["urls"]["original"]
        requests.post(
            url="http://127.0.0.1:5700/send_group_msg",
            data={"group_id": gid, "message": r"[CQ:image,file=" + setu_url + r"]"},
        )


def new_setu(uid, gid, message):
    if gid != None:
        message = message.split(" ")
        tags = ""
        for i in message:
            if len(i) > 0:
                tags = tags + ("tag=" + i + "&")
        v2_url = "https://api.lolicon.app/setu/v2?" + tags
        setu_json = requests.get(url=v2_url)
        setu_url = setu_json.json()["data"][0]["urls"]["original"]
        requests.post(
            url="http://127.0.0.1:5700/send_group_msg",
            data={"group_id": gid, "message": r"[CQ:image,file=" + setu_url + r"]"},
        )


def loli(uid, gid):
    if gid != None:
        url = "https://api.lolicon.app/setu/v2?tag=萝莉&size=small"
        text = requests.get(url)
        setu = text.json()["data"][0]["urls"]["small"]
        requests.post(
            url="http://127.0.0.1:5700/send_group_msg",
            data={"group_id": gid, "message": r"[CQ:image,file=" + setu + r"]"},
        )


def yxy(uid, gid):

    url = "https://shengapi.cn/api/bizi.php?msg=2"
    if gid != None:  # 如果是群聊信息
        requests.post(
            url="http://127.0.0.1:5700/send_group_msg",
            data={"group_id": gid, "message": "余悉越无敌"},
        )
        """
        text = requests.get(url)
        setu = str(text.text)[5:-1]
        requests.post(
            url="http://127.0.0.1:5700/send_group_msg",
            data={
                "group_id": gid,
                "message": r"[CQ:image,file=" + setu + r"]",
            },
        )"""
    else:  # 如果是私聊信息
        requests.get(
            url="http://127.0.0.1:5700/send_private_msg",
            data={"user_id": uid, "message": "余悉越无敌"},
        )


def cjb(uid, gid):
    if gid != None:  # 如果是群聊信息
        url = "https://api.lolicon.app/setu/v2?tag=萝莉|少女&tag=白丝|黑丝"
        text = requests.get(url)
        setu = text.json()["data"][0]["urls"]["original"]
        requests.post(
            url="http://127.0.0.1:5700/send_group_msg",
            data={"group_id": gid, "message": r"[CQ:image,file=" + setu + r"]"},
        )
