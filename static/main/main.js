window.onload = function() {
	readGoods();
	// readGoods_2();
	readThreshold();
	ShowTime();
	Resize();
}
//調整內容的底高
function Resize() {
	$("body").css("margin-top",$(".navbar-fixed-top").height());
	$("body").css("margin-bottom",$(".navbar_2").height());
}
//跳到遊客頁面
function visitor() {
	window.location.assign("guest");
}
//跳到會員頁面
function index() {
	window.location.assign("index");
}
//跳到註冊頁面
function reg() {
	window.location.assign("reg");
}
//跳到登入頁面
function sign() {
	window.location.assign("sign");
}
//導覽列動畫
const $menu = $('#myCarousel');
$menu.on('show.bs.collapse', function () {
	$menu.addClass('menu-show');
});
$menu.on('hide.bs.collapse', function () {
	$menu.removeClass('menu-show');
});