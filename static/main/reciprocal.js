//顯示時間
var RemainTime = 1000*60*60*2;//倒數2小時

!function MyCounter(){
	//確認是否登入
	if (reToken == 0) {
		if(RemainTime<=0){
			//刪除在users/ada子集合下的內容
			console.log(myToken);
			firebase.database().ref(myToken).remove()
				.then(function() {
					console.log("Remove succeeded.")
					RemainTime == "商品已刪除完畢";
				})
				.catch(function(error) {
					console.log("Remove failed: " + error.message)
				});
			//倒數完成
		} else {
			var EXRemainTime = Math.floor(RemainTime/60000);
			console.log("剩餘"+(EXRemainTime) +"分鐘");
			setTimeout(MyCounter,1000);
		}
		RemainTime-=1000; 
	} else {		
		document.getElementById('showbox').innerHTML = "歡迎登入會員"
	}
}();

setInterval(function ShowTime(){
	document.getElementById('showbox').innerHTML = RemainTime/1000+"秒"
})