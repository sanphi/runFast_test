import sys
import os
import json
import requests
import yaml
sys.path.append("../../lib/common")
import QSCommon

################################################################################
###↓↓↓######################   Http request 通用方法   ###################↓↓↓###
################################################################################
# 请求url最后一个切片的接口名


def getInterfaceName(url, interfaceName=""):
    # 判断当前测试的接口名
    if interfaceName == "":
        interfaceName = url.split('/')[-1]
        # interfaceName = sys._getframe().f_code.co_name
    else:
        interfaceName = interfaceName
    return interfaceName


# 是否打印日志
def printLogs(url, interfaceName="", res="", logs=0, datas=""):
    # emoji_pattern = re.compile(
    # u"(\ud83d[\ude00-\ude4f])|"  # emoticons
    # u"(\ud83c[\udf00-\uffff])|"  # symbols & pictographs (1 of 2)
    # u"(\ud83d[\u0000-\uddff])|"  # symbols & pictographs (2 of 2)
    # u"(\ud83d[\ude80-\udeff])|"  # transport & map symbols
    # u"(\ud83c[\udde0-\uddff])"  # flags (iOS)
    # "+", flags=re.UNICODE)
    # remove_emoji= emoji_pattern.sub(r'', res.text)
    # 是否打印log。默认打印
    if 0 == logs:
        if datas != "":
            QSCommon.printUrl("")
            QSCommon.printUrl('---> ' + '【' + interfaceName + ' request' +
                              '】:  ' + url + '        ' + 'Request Data: ' + datas)
            QSCommon.printLog('<--- ' + '【' + interfaceName + ' response' + '】:  ' + str(res.text.replace(u'\xa9 ', u' ').replace(
                u'\U0001f1e8', u' ').replace(u'\U0001f618', u' ').replace(u'\U0001f1f3', u' ').replace(u'\U0001f64f', u' ')))
        else:
            QSCommon.printUrl("")
            QSCommon.printUrl('---> ' + '【' + interfaceName +
                              ' request' + '】:  ' + url)
            QSCommon.printLog('<--- ' + '【' + interfaceName + ' response' + '】:  ' + str(res.text.replace(u'\xa9 ', u' ').replace(
                u'\U0001f1e8', u' ').replace(u'\U0001f618', u' ').replace(u'\U0001f1f3', u' ').replace(u'\U0001f64f', u' ')))


################################################################################
###↓↓↓######################   Http request 模 块   ######################↓↓↓###
################################################################################

# http get
# 入参：interfaceName默认取的url的最后一个切片。如果最后切片是拼接的需要手动传入
# 入参：printLogs是打印url和响应消息体。默认打印。可以传0以外的其他数关闭打印
# 适用于所有get方法
def get(url, headers="", params="", timeout=5, interfaceName="", logs=0):
    res = requests.get(url, headers=headers, params=params, timeout=timeout)
    # 判断当前测试的接口名
    interName = getInterfaceName(url, interfaceName)
    # 是否打印log。默认打印
    printLogs(url, interName, res, logs, str(params))
    return res

# http post
# 入参：interfaceName默认取的url的最后一个切片。如果最后切片是拼接的需要手动传入
# 入参：printLogs是打印url和响应消息体。默认打印。可以传0以外的其他数关闭打印
# 适用于所有post方法


def post(url, headers="", datas="", timeout=50, interfaceName="", logs=0):
    res = requests.post(url, headers=headers, data=datas, timeout=timeout)
    # 判断当前测试的接口名
    interName = getInterfaceName(url, interfaceName)
    # 是否打印log。默认打印
    printLogs(url, interName, res, logs, datas)
    return res

# http put
# 入参：interfaceName默认取的url的最后一个切片。如果最后切片是拼接的需要手动传入
# 入参：printLogs是打印url和响应消息体。默认打印。可以传0以外的其他数关闭打印
# 适用于所有put方法


def put(url, headers="", datas="", timeout=5, interfaceName="", logs=0):
    res = requests.put(url, headers=headers, data=datas, timeout=timeout)
    # 判断当前测试的接口名
    interName = getInterfaceName(url, interfaceName)
    # 是否打印log。默认打印
    printLogs(url, interName, res, logs, datas)
    return res

# http delete
# 入参：interfaceName默认取的url的最后一个切片。如果最后切片是拼接的需要手动传入
# 入参：printLogs是打印url和响应消息体。默认打印。可以传0以外的其他数关闭打印
# 适用于所有delete方法


def delete(url, headers="", datas="", timeout=5, interfaceName="", logs=0):
    res = requests.delete(url, headers=headers, data=datas, timeout=timeout)
    # 判断当前测试的接口名
    interName = getInterfaceName(url, interfaceName)
    # 是否打印log。默认打印
    printLogs(url, interName, res, logs, datas)
    return res
