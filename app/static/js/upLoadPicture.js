function sb() {
    var xhr = new XMLHttpRequest();
    xhr.open('get', '/getSession', false);
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var content = xhr.responseText;
            if (content == 'NOT OK') {
                alert('只有站长登录方能上传');
                event.preventDefault();
            } else {
                return true;
            }
        }
    }
    xhr.send(null);
}