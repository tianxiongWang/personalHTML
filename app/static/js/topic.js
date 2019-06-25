function sb() {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function () {
        if (xhr.readyState = 4 && xhr.status == 200) {
            var Receive = xhr.responseText;
            if (Receive == 'NOT OK') {
                alert('未登录不能写评论');
                event.preventDefault();
            }
            else {
                var content = editor.document.getBody().getHtml();
                if (content == "<p><br></p>") {
                    alert('留言不能为空');
                    event.preventDefault();
                } else {
                    return true;
                }
            }
        }
    }
    xhr.open('get', '/getSession_user', false);
    xhr.send(null);
}