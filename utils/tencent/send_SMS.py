# -*- coding:utf-8 -*-
import ssl

from qcloudsms_py import SmsMultiSender, SmsSingleSender
from qcloudsms_py.httpclient import HTTPError


def send_sms_single(phone_num, template_id, template_param_list):
    '''
    单条发送短信
    :param phone_num: 手机号
    :param template_id: 腾讯云短信模板ID
    :param template_param_list: 短信模板所需参数列表
    :return:
    '''
    appid = 1400806681  # 自己应用ID
    appkey = "3d294abac9985e560daf2a50b05a3b2e"
    sms_sign = "来时即是归处公众号"
    sender = SmsSingleSender(appid, appkey)
    try:
        response = sender.send_with_param(86, phone_num, template_id, template_param_list, sign=sms_sign)
    except HTTPError as e:
        response = {'result': 1000, 'errmsg': "网络异常,发送失败"}
    return response


def send_sms_multi(phone_num_list, template_id, template_param_list):
    '''
    批量发送短信
    :param phone_num_list: 手机号列表
    :param template_id: 腾讯云短信模板ID
    :param template_param_list: 短信模板所需参数列表
    :return:
    '''
    appid = 1400806681  # 自己应用ID
    appkey = "3d294abac9985e560daf2a50b05a3b2e"
    sms_sign = "来时即是归处公众号"
    sender = SmsMultiSender(appid, appkey)
    try:
        response = sender.send_with_param(86, phone_num_list, template_id, template_param_list, sign=sms_sign)
    except HTTPError as e:
        response = {'result': 1000, 'errmsg': "网络异常,发送失败"}
    return response


if __name__ == '__main__':
    result1 = send_sms_single('18225078646', 1744672, [666, ])
    print(result1)

