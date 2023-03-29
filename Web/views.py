import random

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
    tpl = request.GET.get('tpl')
    template_id = settings.TENCENT_SMS_TEMPLATE.get(tpl)
    if not template_id:
        return HttpResponse("模板不存在")
    code = random.randrange(1000, 9999)
    res = send_sms_single('18225078646', template_id, [code, ])
    if res['result'] == 0:
        return HttpResponse('成功')
    else:
        HttpResponse(res['errmsg'])


def register(request):
    form = RegisterModelForm()
    return render(request, 'register.html', {'form': form})
