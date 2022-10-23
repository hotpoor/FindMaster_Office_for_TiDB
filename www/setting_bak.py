#!/bin/env python
#coding=utf-8
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/vendor/')
#os.chdir(os.path.dirname(os.path.abspath(__file__)))

import logging
import uuid
from version import version_num

settings = {
    "static_path": os.path.join(os.path.dirname(__file__),"static"),
    "demos_path": os.path.join(os.path.dirname(__file__),"demos"),
    "cookie_secret": "hotpoorinchina",
    "cookie_domain": "",
    "QiniuAccessKey": "",
    "QiniuSecretKey": "",
    "QQMailSecretKey":"",
    "QQMailSecretKey1":"",
    "MPWeixinJSMP":[],
    "MPWeixinAppDefault":"office",
    "MPWeixinApps":[],
    "MPWeixinInfo":{
        "office":{
            "MPWeixinID":"",
            "MPWeixinAppID":"",
            "MPWeixinAppSecret":"",
            "ShopNumber":"",
            "ShopNumberKey":"",
            "ShopNumberKeyV3":"",
            "accessToken":"",
            "ticket":"",
            "accessTokenTimer":0,
            "ca_certs":"",
            "client_key":"",
            "client_cert":"",
            "name":"",
            "MPWeixinTemplateHollowNotice":"",
        },
    },
    "AlipayApps":[],
    "AlipayInfo":{
        "office":{
            "AlipayAppID":"",
            "AlipayPrivateKey":"",
            "AlipayPublicKey":"",
            "AlipayAppPublicKey":"",
            "AlipayPrivateKeyFile":"",
            "AlipayPublicKeyFile":"",
            "AlipayAppPublicKeyFile":"",
        },
    },
    "AgoraAppID":"",
    "AgoraAppCertificate":"",
    "BaiduYuyinAppID": "",
    "BaiduYuyinAPIKey": "",
    "BaiduYuyinSecretKey":"",
    "debug": True,
    # "debug": False,
    "wss_port":8100,
    "LoginCode":"automove",
    "developers":[
        "",#夏力维邮箱1020517891@qq.com
    ],
    "uri_mapping":{
        "/"                 :"",#首页
        "/mobile"           :"",#手机端首页
        "/register"         :"",
        "/login"            :"",
        "/forget_pwd"       :"",
        "/support"          :"",
    },
    # "msh_hollow":"",
    # "msh_hollow_data":"",
    # "msh_login_scan":"",
    "store_ground":"",
    "store_search":"",
    "store_hollow":"",
    "stripe_public_key":"",
    "stripe_api_key":"",
    "stripe_public_key_test":"",
    "stripe_api_key_test":"",
    "stripe_webhook_secret_test":"",
    "stripe_webhook_secret":"",
    "stripe_account_default":"",
    "version":version_num,
    "base_ca_tax_id":"",
    "base_ca_company":"",
    "search_type":["title","desc","tags","doms","product_title","product_desc","sequence"],
    "search_no_str":" !\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~！？｡＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘'‛“”„‟…‧﹏.",
}

try:
    import torndb as database
    conn = database.Connection("127.0.0.1:4000", "office", "root", "")
    conn1 = database.Connection("127.0.0.1:4000", "office1", "root", "")
    conn2 = database.Connection("127.0.0.1:4000", "office2", "root", "")
    ring = [conn1, conn2]
except:
    pass
