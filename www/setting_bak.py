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
        "e083424676854751ad3d590172539b18",#夏力维邮箱1020517891@qq.com
    ],
    "uri_mapping":{
        "/"                 :"1a1bff508d054e7ab5ea70623399701f",#首页
        "/mobile"           :"1a1bff508d054e7ab5ea70623399701f",#手机端首页
        "/register"         :"f72eabff7f2c42daa6cc65d778457f2b",
        "/login"            :"390b8a1df61e4723a9d75b8b80093110",
        "/forget_pwd"       :"8d571e3cde494804bf5b72afcb00f400",
        "/support"          :"862f586713e945e88273e79e9714e462",
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
    import torndb3 as database
    conn = database.Connection("127.0.0.1:4000", "office", "root", "")
    conn1 = database.Connection("127.0.0.1:4000", "office1", "root", "")
    conn2 = database.Connection("127.0.0.1:4000", "office2", "root", "")
    ring = [conn1, conn2]
except:
    pass


