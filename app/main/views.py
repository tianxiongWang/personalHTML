from flask import render_template
from flask import session
from . import main
from ..import db
from ..models import *
from flask import request
from flask import redirect
import datetime
import time

# coding:utf-8   #强制使用utf-8编码格式
import smtplib  # 加载smtplib模块
from email.mime.text import MIMEText
from email.utils import formataddr
my_sender = '276721023@qq.com'  # 发件人邮箱账号，为了后面易于维护，所以写成了变量


def mail(uemail, content):
    msg = MIMEText(content, 'plain', 'utf-8')
    # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    msg['From'] = formataddr(["王天雄", my_sender])
    msg['To'] = formataddr(["亲爱的朋友", uemail])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
    msg['Subject'] = "您的账号密码"  # 邮件的主题，也可以说是标题
    server = smtplib.SMTP("smtp.qq.com", 25)  # 发件人邮箱中的SMTP服务器，端口是25
    server.login(my_sender, "bnnketyiwmxvbghi")  # 括号中对应的是发件人邮箱账号、邮箱密码
    # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
    server.sendmail(my_sender, [uemail, ], msg.as_string())
    server.quit()  # 这句是关闭连接的意思


@main.route('/')
def index():
    categories = db.session.query(Category).all()
    topics_1 = db.session.query(Topic).order_by(Topic.time.desc()).all()
    topics_2 = db.session.query(Topic).filter_by(
        category_id=1).order_by(Topic.time.desc()).limit(5)
    topics_3 = db.session.query(Topic).filter_by(
        category_id=2).order_by(Topic.time.desc()).limit(5)
    if 'uid' in session and 'uname' in session:
        user = db.session.query(User).filter_by(id=session.get('uid')).first()
    return render_template('index.html', params=locals())


@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        categories = db.session.query(Category).all()
        return render_template('register.html', params=locals())
    else:
        uname = request.form.get('uname')
        upwd = request.form.get('upwd')
        uemail = request.form.get('uemail')
        uphone = int(request.form.get('uphone'))
        content = '''您的账号:%s\n您的密码:%s\n请牢记，若发生遗失，请与我联系\n联系方式:我的主页下方''' % (
            uname, upwd)
        mail(uemail, content)
        user = User()
        user.username = uname
        user.password = upwd
        user.email = uemail
        user.phonenum = uphone
        db.session.add(user)
        db.session.commit()
        session['uid'] = user.id
        session['uname'] = user.username
        return redirect('/')


@main.route('/login')
def login():
    if 'uid' in session and 'uname' in session:
        return redirect('/')
    else:
        categories = db.session.query(Category).all()
        return render_template('login.html', params=locals())


@main.route('/loginPhone', methods=['POST'])
def loginPhone():
    phone = request.form.get('phonenum')
    user = db.session.query(User).filter_by(phonenum=phone).first()
    if user:
        session['uid'] = user.id
        session['uname'] = user.username
    return redirect('/')


@main.route('/loginUsername', methods=['POST'])
def logUsername():
    categories = db.session.query(Category).all()
    loginName = request.form.get('uname')
    loginPwd = request.form.get('upwd')
    user = db.session.query(User).filter_by(
        username=loginName, password=loginPwd).first()
    if user:
        session['uid'] = user.id
        session['uname'] = user.username
        return redirect('/')
    else:
        errMsg = '用户名或密码错误'
    return render_template('login.html', params=locals(), errMsg=errMsg)


@main.route('/logout')
def logout():
    del session['uid']
    del session['uname']
    return redirect('/')


@main.route('/board')
def board():
    if not request.args.get('page'):
        categories = db.session.query(Category).all()
        boards = db.session.query(Board).order_by(Board.date.desc()).limit(5)
        numbers = db.session.query(Board).count()
        pages = numbers // 5 if numbers % 5 == 0 else numbers // 5 + 1
        pagenext = 1
        pagelast = pages - 1
        user = db.session.query(User).filter_by(
            id=session.get('uid'), username=session.get('uname')).first()
        if request.args.get('errMsg'):
            errMsg = request.args.get('errMsg')
        return render_template('board.html', params=locals())
    else:
        page = request.args.get('page')
        if int(page) >= 1:
            pageback = int(page) - 1
        else:
            pageback = 0
        categories = db.session.query(Category).all()
        boards = db.session.query(Board).order_by(
            Board.date.desc()).limit(5).offset(int(page)*5).all()
        numbers = db.session.query(Board).count()
        pages = numbers // 5 if numbers % 5 == 0 else numbers // 5 + 1
        if int(page) < pages - 1:
            pagenext = int(page) + 1
        else:
            pagenext = pages - 1
        pagelast = pages - 1
        user = db.session.query(User).filter_by(
            id=session.get('uid'), username=session.get('uname')).first()
        return render_template('board.html', params=locals())


@main.route('/writeBoard', methods=['GET', 'POST'])
def writeBoard():
    if request.method == 'GET':
        categories = db.session.query(Category).all()
        boards = db.session.query(Board).all()
        if 'uid' in session and 'uname' in session:
            user = db.session.query(User).filter_by(
                id=session.get('uid'), username=session.get('uname')).first()
            return render_template('writeBoard.html', params=locals())
        else:
            errMsg = '未登录'
            # 用GET方法传参，交给/board去处理这个错误信息
            return redirect('/board?errMsg=%s' % errMsg)
    else:
        board = Board()
        board.text = request.form.get('input')
        board.user_id = session.get('uid')
        board.date = time.localtime()
        print(board.date)
        db.session.add(board)
        return redirect('/board')


@main.route('/writetopic', methods=['GET', 'POST'])
def writetopic():
    if request.method == 'GET':
        categories = db.session.query(Category).all()
        if 'uid' in session and 'uname' in session:
            user = db.session.query(User).filter_by(
                id=session.get('uid')).first()
        return render_template('writetopic.html', params=locals())
    else:
        tittle = request.form.get('tittle')
        content = request.form.get('content')
        category_id = int(request.form.get('category'))
        category = db.session.query(Category).filter_by(id=category_id).first()
        now = time.localtime()
        topic = Topic()
        topic.tittle = tittle
        topic.text = content
        topic.time = now
        topic.category = category
        db.session.add(topic)
        return redirect('/')


@main.route('/topics')
def topics():
    if request.args.get('categoryid') == '1':
        categoryid = request.args.get('categoryid')
        page = 0
        try:
            page = int(request.args.get('page'))
        except:
            pass
        pages = len(db.session.query(Topic).filter_by(category_id=1).all()) // 10 + 1
        categories = db.session.query(Category).all()
        if 'uid' in session and 'uname' in session:
            user = db.session.query(User).filter_by(
                id=session.get('uid')).first()
        topics = db.session.query(Topic).filter_by(
            category_id=1).order_by(Topic.time.desc()).limit(10).offset(10 * page)
        return render_template('topics.html', params=locals())
    if request.args.get('categoryid') == '2':
        categoryid = request.args.get('categoryid')
        page = 0
        try:
            page = int(request.args.get('page'))
        except:
            pass
        pages = len(db.session.query(Topic).filter_by(category_id=2).all()) // 10 + 1
        categories = db.session.query(Category).all()
        if 'uid' in session and 'uname' in session:
            user = db.session.query(User).filter_by(
                id=session.get('uid')).first()
        topics = db.session.query(Topic).filter_by(
            category_id=2).order_by(Topic.time.desc()).limit(10).offset(10 * page)
        return render_template('topics.html', params=locals())
    if request.args.get('categoryid') == '0':
        categoryid = request.args.get('categoryid')
        page = 0
        try:
            page = int(request.args.get('page'))
        except:
            pass
        pages = len(db.session.query(Topic).all()) // 10 + 1
        categories = db.session.query(Category).all()
        if 'uid' in session and 'uname' in session:
            user = db.session.query(User).filter_by(
                id=session.get('uid')).first()
        topics = db.session.query(Topic).order_by(Topic.time.desc()).limit(10).offset(10 * page)
        return render_template('topics.html', params=locals())


@main.route('/topic')
def topic():
    return 'this is topic page!'

@main.route('/play')
def play():
    return render_template('贪吃蛇.html')