$(document).ready(function () {

    $('form').bind('submit', function() {
        //alert('BBBBB');
        var in_name = $('#input_name').val();
        var in_pwd = $('#input_pwd').val();
        if (in_name ==='' || in_pwd ==='') {
            //alert('请填写内容!!!!!!!!');
            $('p#tips').text('请填写内容!!!!!!').show().css({"color":"red","font-size":"10px"});
            return false
        }
    });
   // alert('AAAAAA')
    var value = $('p#tips').text();
    //alert(value);
    if(value === '') {
       $('p#tips').hide();
    }
    else{
       $('p#tips').show().css({"color":"red","font-size":"10px"});
    }

    $("#input_name,#input_pwd").mousedown(function() {
        $("p#tips").hide();
    });
});
