$(document).ready(function () {
   // alert('AAAAAA')
    $('form').bind('submit', function() {
        var value = $('input#search-content').val();
        // alert(value);
        if(value === ''){
            alert('请输入查找内容');
            return false;
        }
        else {
            return true;
        }

    });
});
