var myToken;
socket = io();
socket.emit('getToken');

function rebackSocket(){
	socket.emit('reback', {"token" : myToken});
}

socket.on('receiveToken', function(data) {
	guest = 'Token';
    myToken = data;
	console.log(data);

	duration = 1;			// 資料將被保留1小時
	today = new Date();
	expireDate = new Date();
	expireDate.setTime(today.getTime()+1000*60*60*2*duration);	// 設定時間為兩小時後
	count = getCookie(guest);
	console.log(count);

	if (count == null){
		setCookie(guest ,myToken ,expireDate);
		message = "歡迎 尊貴的用戶"
	} else {
		myToken = count;
		message = "您正在使用中"
	}
	console.log(message);
	console.log("（您在本頁所留下的資料記錄在名為「"+myToken+"」的小餅乾，將會被保留"+2*duration+"小時。）");
	socket.emit('uid', myToken);
});


//設定cookie
function setCookie(name, value) {
	var argv = setCookie.arguments;
	var argc = setCookie.arguments.length;
	var expires = (argc > 2) ? argv[2] : null;
	var path = (argc > 3) ? argv[3] : null;
	var domain = (argc > 4) ? argv[4] : null;
	var secure = (argc > 5) ? argv[5] : null;

	document.cookie = escape(name) + "=" + escape(value) +
	((expires == null) ? "" : ("; expires=" + expires.toGMTString())) +
	((path == null) ? "" : ("; path=" + path)) +
	((domain == null) ? "" : ("; domain=" + domain)) +
	((secure == null) ? "" : ("; secure=" + secure));
}

//依照name搜尋cookie
function getCookie(name) {
	var arg = escape(name) + "=";
	var nameLen = arg.length;
	var cookieLen = document.cookie.length;
	var i = 0;
   
	while (i < cookieLen) {
		var j = i + nameLen;
		if (document.cookie.substring(i, j) == arg)
			return getCookieValueByIndex(j);
		i = document.cookie.indexOf(" ", i) + 1;
		if (i == 0) break;
	}
	return null;
}
