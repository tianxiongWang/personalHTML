// 轮播图的动画效果
var timer = setInterval(chart, 3000)
var i = 1

function chart() {
	var pic = document.getElementById('bigPicture');
	var ul = document.getElementById('bigPictureNavUl');
	for (var j = 0; j < 3; j++) {
		pic.children[j].style.display = 'none';
		ul.children[j].style.background = 'white';
	}
	pic.children[i].style.display = 'inline-block';
	ul.children[i].style.background = 'green';
	i++;
	if (i > 2) {
		i = 0;
	}
}
// 新闻栏的动态事件:鼠标移入，展现不同的新闻模块
var newselect = document.getElementById('newselect');
newselect.children[0].onmouseover = function () {
	document.getElementById('newsRightBottom1').style.display = 'block';
	document.getElementById('newsRightBottom2').style.display = 'none';
	document.getElementById('newsRightBottom3').style.display = 'none';
}
newselect.children[1].onmouseover = function () {
	document.getElementById('newsRightBottom1').style.display = 'none';
	document.getElementById('newsRightBottom2').style.display = 'block';
	document.getElementById('newsRightBottom3').style.display = 'none';
}
newselect.children[2].onmouseover = function () {
	document.getElementById('newsRightBottom1').style.display = 'none';
	document.getElementById('newsRightBottom2').style.display = 'none';
	document.getElementById('newsRightBottom3').style.display = 'block';
}
newselect.children[0].onmouseout = function () {
	document.getElementById('newsRightBottom1').style.display = 'block';
	document.getElementById('newsRightBottom2').style.display = 'none';
	document.getElementById('newsRightBottom3').style.display = 'none';
}
newselect.children[1].onmouseout = function () {
	document.getElementById('newsRightBottom1').style.display = 'none';
	document.getElementById('newsRightBottom2').style.display = 'block';
	document.getElementById('newsRightBottom3').style.display = 'none';
}
newselect.children[2].onmouseout = function () {
	document.getElementById('newsRightBottom1').style.display = 'none';
	document.getElementById('newsRightBottom2').style.display = 'none';
	document.getElementById('newsRightBottom3').style.display = 'block';
}

function go() {
	var xhr = new XMLHttpRequest();
	xhr.open('get', '/getSession', true);
	xhr.onreadystatechange = function () {
		if (xhr.readyState == 4 && xhr.status == 200) {
			response = xhr.responseText;
			if (response == 'OK') {
				window.location.href = "http://www.wangxiong.club/writetopic";
			} else {
				alert('只有站长登陆后才能写日志哦');
			}
		}
	}
	xhr.send(null);
}