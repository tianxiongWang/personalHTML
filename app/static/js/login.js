var tittle1 = document.getElementById('tittle1');
var tittle2 = document.getElementById('tittle2');

tittle1.onclick = function () {

    document.getElementById('main1').style.display = 'block';
    document.getElementById('main2').style.display = 'none';
}

tittle2.onclick = function () {
    document.getElementById('main2').style.display = 'block';
    document.getElementById('main1').style.display = 'none';
}

// 发送短信,先验证在不在数据库
function sendMsg() {
    var xhr0 = new XMLHttpRequest();
    var phone = document.getElementById('phonenum').value
    xhr0.open('get', '/user_phone?phonenum=' + phone, true);
    xhr0.onreadystatechange = function () {
        if (xhr0.readyState == 4 && xhr0.status == 200) {
            if (xhr0.responseText == 'true') {
                document.getElementById('hidden_exist').innerText = xhr0.responseText;
                console.log(document.getElementById('hidden_exist').innerText);
                var xhr = new XMLHttpRequest();
                var phone = document.getElementById('phonenum').value
                xhr.open('get', '/sendMsg?phone=' + phone, true);
                xhr.onreadystatechange = function () {
                    if (xhr.readyState == 4 && xhr.status == 200) {
                        document.getElementById("hidden_msg").innerText = xhr.responseText;
                        alert("验证码已发到号码为" + phone + "的手机");
                    }
                }
                xhr.send(null);
            } else {
                alert('该手机号未绑定账号!');
            }
        }
    }
    xhr0.send(null);
}
// 直接在前端验证，通过了方能提交数据
function message() {
    console.log(document.getElementById('hidden_exist').innerText);
    console.log(document.getElementById('hidden_msg').innerText);
    var condition1 = (document.getElementById("hidden_msg").innerText == document.getElementById('Msgidenty').value);
    var condition2 = (document.getElementById('hidden_exist').innerText == 'true');
    console.log(condition1);
    console.log(condition2);
    if (condition2) {
        return true;
    }
    alert('手机号码未注册或验证码错误')
    return false;
}