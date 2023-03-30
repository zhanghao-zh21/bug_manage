# -*- coding:utf-8 -*-
import random

from django.http import JsonResponse
# Create your views here.
from django.shortcuts import HttpResponse, render

from Web.utils.ModelForm import *
from Web.utils.tencent.send_SMS import send_sms_single
from django.conf import settings


def send_sms(request):
    ''' 发送短信
        ?tpl=login -> 1744670
        ?tpl=register -> 1744672
        ?tpl=re_password -> 1744669
    '''
    form = SendSmsForm(request, data=request.GET)
    # 只是校验手机号:不能为空,格式是否正确
    if form.is_valid():
        return JsonResponse({'status': True})
    return JsonResponse({'status': False, 'error': form.errors})


def register(request):
    ''' 注册 '''
    form = RegisterModelForm()
    return render(request, 'register.html', {'form': form})
