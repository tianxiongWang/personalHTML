function show() {
    document.getElementById('msgtext').value = '';
}

function showvalue() {
    if (document.getElementById('msgtext').value == '') {
        document.getElementById('msgtext').value = "请输入短信验证码";
    }
}

function identy_user() {
    var pattern = /^[a-zA-Z0-9_-]{6,30}/;
    text = document.getElementById('username').value;
    var xhr = new XMLHttpRequest()
    xhr.open('GET', href = "/user_server?username=" + text, true)
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            user_server = xhr.responseText;
            if (pattern.test(text) && user_server == 'true') {
                var userText = document.getElementById('userText');
                userText.innerText = '此用户名合法可用!';
                userText.style.color = 'green';
            } else {
                var userText = document.getElementById('userText');
                userText.innerText = '该用户名长度不合要求或已存在';
                userText.style.color = 'red';
            }
        }
    }
    xhr.send(null);
}

function identy_password() {
    var pattern = /^[a-zA-Z0-9_-]{8,30}/;
    text = document.getElementById('upwd').value;
    if (pattern.test(text)) {
        document.getElementById('upwdText').innerText = '密码长度合格'
        document.getElementById('upwdText').style.color = 'green';
    } else {
        document.getElementById('upwdText').innerText = '密码长度不符合要求'
        document.getElementById('upwdText').style.color = 'red';
    }
}

function identy_email() {
    pattern = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/;
    text = document.getElementById('uemail').value;
    textLength = document.getElementById('uemail').value.length;
    if (textLength == 0) {
        document.getElementById('emailText').innerText = '请输入电子邮箱';
        document.getElementById('emailText').style.color = 'red';
    } else if (!pattern.test(text)) {
        document.getElementById('emailText').innerText = '请输入正确的电子邮箱';
        document.getElementById('emailText').style.color = 'red';
    } else {
        document.getElementById('emailText').innerText = '电子邮箱合法';
        document.getElementById('emailText').style.color = 'green';
    }
}

var a = 0;

function sendMsg() {
    var xhr = new XMLHttpRequest();
    var phoneNum = document.getElementById('uphone').value;
    xhr.open('GET', '/sendMsg?phone=' + phoneNum, true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            a = xhr.responseText;
            alert("验证码已发到号码为" + phoneNum + "的手机");
        }
    }
    xhr.send(null);
}

var form = document.getElementById('form');
form.onsubmit = function () {
    var pattern_user = /^[a-zA-Z0-9_-]{6,30}/;
    // 正则匹配是否满足六位账号的要求
    var condition1 = pattern_user.test(document.getElementById('username').value);
    var xhr = new XMLHttpRequest();
    username = document.getElementById('username').value;
    xhr.open('GET', href = "/user_server?username=" + username, true);
    // 查询数据库中是否有这个账号
    if (document.getElementById('username').value == '该用户名长度不合要求或已存在') {
        var condition2 = false;
    } else {
        var condition2 = true;
    }

    // 正则匹配密码位数是否满足要求
    var pattern_pwd = /^[a-zA-Z0-9_-]{8,30}/;
    var condition3 = pattern_pwd.test(document.getElementById('upwd').value);

    // 正则匹配电子邮箱
    var pattern_email = /^([a-zA-Z0-9_-])+@([a-zA-Z0-9_-])+(.[a-zA-Z0-9_-])+/;
    condition4 = pattern_email.test(document.getElementById('uemail').value);
    // 验证码是否正确
    condition5 = (document.getElementById('msgtext').value == String(a));
    console.log(typeof (condition1));
    console.log(typeof (condition2));
    console.log(typeof (condition3));
    console.log(typeof (condition4));
    console.log(typeof (condition5));
    console.log(condition1);
    console.log(condition2);
    console.log(condition3);
    console.log(condition4);
    console.log(condition5);
    condition = condition1 && condition2 && condition3 && condition4 && condition5;
    if (condition) {
        alert('恭喜您完成注册，现在跳转回主页并自动登录...');
    } else {
        alert('信息没填完整哦!');
    }
    return (condition);
}