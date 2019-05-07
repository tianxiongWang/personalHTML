function click() {
    document.getElementById("write").disabled = true;
}

function sb() {
    var content = editor.document.getBody().getText();
    if (content.length > 1) {
        return true;
    } else {
        alert('留言至少两个字符哦!')

    }
}