#!/usr/bin/env python
# coding=utf-8
from pocs.web.weaver.main import *
from pocs.web.seeyon.main import *
from pocs.web.CVE_2021_22205 import CVE_2021_22205
from pocs.web.ueditor_1433_parsing_vulnerabilitly import ueditor_1433_Parsing_vulnerability
from pocs.web.CVE_2021_21972 import CVE_2021_21972
from pocs.web.CVE_2021_40870 import CVE_2021_40870

def web(url):
    print('\n[+] 正在加载 常见Web漏洞 poc检测模块......')
    poclist = []
    poclist = poclist + weaver(url)
    poclist = poclist + seeyon(url)
    poclist = poclist + [
        'CVE_2021_22205("{0}")'.format(url),
        'CVE_2021_21972("{0}")'.format(url),
        'ueditor_1433_Parsing_vulnerability("{0}")'.format(url),
        'CVE_2021_40870("{0}")'.format(url),
    ]


    return poclist
