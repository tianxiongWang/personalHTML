function sb() {
    var content = editor.document.getBody().getHtml();
    if (content == "<p><br></p>"){
        alert('留言不能为空');
        return false;
    }
    return true;
}