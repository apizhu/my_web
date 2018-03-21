// window.onload = function () {
// 			//var oTxt1 = document.getElementById('account');
// 			// var oTxt2 = document.getElementById('txt1');
// 			// var oTxt3 = document.getElementById('txt2');
//             //
// 			// oTxt1.style.fontSize = 12 + 'px';
//             //
// 			// oTxt3.onmousedown = oTxt2.onmousedown = function() {
// 			// 	oTxt1.style.fontSize = 0 + 'px';
// 			// };
// 		};
$(document).ready( function() {
    $('form').bind('submit',function () {  //给form标签绑定submit事件
        var i=0;
        $(".register-class input").each(function(){  //遍历input标签，判断是否有内容未填写
            var vl=$(this).val();
            var id = $(this).attr("id");
            if(vl===""){
                i = 1;
                //alert(id);
                $("p#"+id).show().css({"color":"red","font-size":"10px"});
            }
        });

        var pw1 = $("input#p1").val();
        var pw2 = $("input#p2").val();
        if (pw1 !== '' && pw2 !== '' && pw1!==pw2) {
            $('#password-tip').show();
            i = 1;
    }

        if (i===1) {  //如果有未填写的，则return false阻止提交
            return false;
        }
    });

    $(".register-class input").each(function () {
        var id = $(this).attr("id");
        //alert("id====="+id);
        $(this).mousedown(function () {
            $("p#"+id).hide();
        });
    });

    $("#p1,#p2").mousedown(function() {
        $("#password-tip").hide().css({"color":"red","font-size":"10px"});
    });

});