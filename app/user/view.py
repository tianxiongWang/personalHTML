from flask import render_template
from . import user
from ..import db
from ..models import *
from flask import request
from qcloudsms_py import SmsSingleSender
from qcloudsms_py.httpclient import HTTPError
from flask import session
import random

appid = 1400196770
appkey = 'e3387667a9038617df14ecaabaa7ef10'
phone_numbers = ["13961252501"]
template_id = 314627
sms_sign = "王雄的爱好记录与分享"
ssender = SmsSingleSender(appid, appkey)


@user.route('/user_server', methods=['GET', 'POST'])
def user_server():
    username = request.args.get('username')
    Exist = db.session.query(User).filter_by(username=username).first()
    if(Exist is None):
        return 'true'
    return 'false'


@user.route('/user_phone')
def user_phone():
    phone = request.args.get('phonenum')
    Exist = db.session.query(User).filter_by(phonenum=phone).first()
    if(Exist):
        return 'true'
    return 'false'


@user.route('/sendMsg')
def sendMsg():
    phone_numbers = [request.args.get('phone')]
    L = [random.randrange(0, 10) for i in range(6)]
    s = ''
    for i in L:
        s += str(i)
    params = [s]
    try:
        result = ssender.send_with_param(
            86, phone_numbers[0], template_id, params, sign=sms_sign, extend="", ext="")
    except HTTPError as e:
        pass
    except Exception as e:
        pass
    return s

@user.route('/getSession')
def getSession():
    if 'uid' in session and 'uname' in session:
        if session.get('uname') == 'wangxiong':
            return 'OK'
    else:
        return 'NOT OK' 
