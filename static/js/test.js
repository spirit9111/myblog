// 获得前端cookie
function getCookie(name) {
	var cookieValue = null;
	if (document.cookie && document.cookie !== '') {
		var cookies = document.cookie.split(';');
		for (var i = 0; i < cookies.length; i++) {
			var cookie = jQuery.trim(cookies[i]);
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) === (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
	// 这些HTTP方法不要求CSRF包含
	return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
	beforeSend: function (xhr, settings) {
		if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
			xhr.setRequestHeader("X-CSRFToken", csrftoken);
		}
	}
});
// 归档相关
$(function () {
	$('.div0').children('a').click(function () {
		$(this).siblings('ul').slideToggle().parent().siblings().children('ul').slideUp()
	})
})
$(function () {
	$('.div01').children('a').click(function () {
		$(this).siblings('li').slideToggle().parent().siblings().children('li').slideUp()
	})
})
$(function () {
	$('.div0').children('a').mouseenter(function () {
		$(this).css({fontSize: "32.3px", color: "red"})
	})
})
$(function () {
	$('.div0').children('a').mouseleave(function () {
		$(this).css({fontSize: "32px", color: "#337ab7"})
	})
})
$(function () {
	$('.div01').children('a').mouseenter(function () {
		$(this).css({fontSize: "26.3px", color: "red"})
	})
})
$(function () {
	$('.div01').children('a').mouseleave(function () {
		$(this).css({fontSize: "26px", color: "#337ab7"})
	})
})


//发送短信
$(function () {
	$('#sms').click(function () {
		// alert('sms')
		var mobile = $('#re_mobile').val()
		$.ajax({
			url: '/register/sendtomes?mobile=' + mobile,
			type: 'get',
			contentType: 'application/json',
			dataType: 'json',
			success: function (data) {
				alert(data.error)
			},
			error: function () {
				alert(data.error)
			}
		});
	})
})
//切换回复
$('.switch').click(function () {
	$(this).parent('p').siblings().children('form').toggleClass('innershow')
	// alert('弹出输入框')

})
//回复文章
$('.reply').click(function (event) {
	//阻止跳转
	event.preventDefault();
	var comment_id = $(this).parent('div').attr('comment_id') //默认没有父评论
	var article_id = $(this).parent('div').attr('article_id');
	var content = $(this).parent('div').siblings('.textarea').val();
	if (!content) {
		alert('请输入评论内容');
		return
	}

	var params = {
		'article_id': article_id,
		'content': content,
		'comment_id': comment_id
	};

	$.ajax({
		url: 'http://127.0.0.1:8000/comment',
		type: 'post',
		data: params,
		dataType: 'json',
		// contentType: 'application/json',
		headers: {
			"X-CSRFToken": getCookie("csrf_token")
		},
		success: function (resp) {
			console.log(resp.error)
			// alert(resp.error);
			// alert('success')
			//
			if (resp.error == 'OK') {
				// alert('返回评论数据,拼接字符串!')
				window.location.reload()
			}
			else {
				//简单显示,未做处理
				alert(resp.error)
			}
		},
	});
});
//回复评论
$('#comment-submit').click(function (event) {
	//阻止跳转
	event.preventDefault();
	var comment_id = '' //默认没有父评论
	var article_id = $('.articleid').val();
	var content = $('.textarea').val();
	if (!content) {
		alert('请输入评论内容');
		return
	}

	var params = {
		'article_id': article_id,
		'content': content,
		'comment_id': comment_id
	};

	$.ajax({
		url: 'http://127.0.0.1:8000/comment',
		type: 'post',
		data: params,
		dataType: 'json',
		// contentType: 'application/json',
		headers: {
			"X-CSRFToken": getCookie("csrf_token")
		},
		success: function (resp) {
			console.log(resp.error)
			// alert(resp.error);
			// alert('success')
			//
			if (resp.error == 'OK') {
				// alert('返回评论数据,拼接字符串!')
				window.location.reload()
			}
			else {
				//简单显示,未做处理
				alert(resp.error)
			}
		},
	});
});
//登录
$('#login_mobile').blur(function () {
	var mobile = $("#login_mobile").val()
	// var password = $(".login_form #password").val()

	if (!mobile) {
		$("#login-mobile-err").show();
	}
	if (mobile) {
		$("#login-mobile-err").hide();
	}

})
$('#login_password').blur(function () {
	var password = $("#login_password").val()
	// var password = $(".login_form #password").val()

	if (!password) {
		$("#login-password-err").show();
	}
	if (password) {
		$("#login-password-err").hide();
	}
})
$('#login_submit').click(function (event) {
	//阻止跳转
	event.preventDefault();
	var password = $("#login_password").val()
	var mobile = $("#login_mobile").val()
	if (password && mobile) {
		var params = {
			'mobile': mobile,
			'password': password,
		};

		$.ajax({
			url: 'http://127.0.0.1:8000/login/',
			type: 'post',
			data: params,
			// contentType: 'application/json',
			dataType: 'json',
			headers: {
				"X-CSRFToken": getCookie("csrf_token")
			},
			success: function (resp) {
				if (resp.error == 'OK') {
					//刷新当前页,跳转首页
					window.location.reload()
				}
				else {
					//简单显示,未做处理
					alert(resp.error)
				}
			},
		});
	}
});
//注册
$('#re_mobile').blur(function () {
	var mobile = $("#re_mobile").val()

	if (!mobile) {
		$("#login-password-err00").show();
	}
	if (mobile) {
		if (mobile.length != 11) {
			$("#login-password-err00").html('手机号错误')
			$("#login-password-err00").show();
			return
		}
		$("#login-password-err00").hide();
	}
})
$('#re_username').blur(function () {
	var username = $("#re_username").val()

	if (!username) {
		$("#login-password-err01").show();
	}
	if (username) {
		if (username.length < 5 || username.length > 11) {
			$("#login-password-err01").html('用户名长度为5-11位')
			$("#login-password-err01").show();
			return
		}
		$("#login-password-err01").hide();
	}
})
$('#re_password').blur(function () {
	var password = $("#re_password").val()

	if (!password) {
		$("#login-password-err02").show();
	}
	if (password) {
		if (password.length < 7 || password.length > 14) {
			$("#login-password-err02").html('密码长度为8-14位')
			$("#login-password-err02").show();
			return
		}
		$("#login-password-err02").hide();
	}
})
$('#re_password2').blur(function () {
	var password = $("#re_password").val()
	var password2 = $("#re_password2").val()
	if (password.length != password2.length) {
		$("#login-password-err03").html('两次密码不一致')
		$("#login-password-err03").show();
		return
	}
	$("#login-password-err03").hide()
})
$('#re_code').blur(function () {
	var sms_code = $("#re_code").val()

	if (!sms_code) {
		$("#login-password-err04").show();
	}
	if (sms_code) {
		if (sms_code.length != 6) {
			$("#login-password-err04").html('验证码长度为6位')
			$("#login-password-err04").show();
			return
		}
		$("#login-password-err04").hide();
	}
})

$('#re_submit').click(function (event) {
	//阻止跳转
	event.preventDefault();
	var mobile = $("#re_mobile").val()
	var username = $("#re_username").val()
	var password = $("#re_password").val()
	var password2 = $("#re_password2").val()
	var sms_code = $("#re_code").val()
	if (mobile && username && password && password2 && sms_code) {
		var params = {
			'mobile': mobile,
			'username': username,
			'password': password,
			'password2': password2,
			'sms_code': sms_code,
		};

		$.ajax({
			url: 'http://127.0.0.1:8000/register',
			type: 'post',
			data: params,
			dataType: 'json',
			headers: {
				"X-CSRFToken": getCookie("csrf_token")
			},
			success: function (resp) {
				console.log(resp.error)
				if (resp.error == 'OK') {
					//刷新当前页,跳转首页
					window.location.reload()
				}
				else {
					//简单显示,未做处理
					alert(resp.error)
				}
			},
		});
	}
});