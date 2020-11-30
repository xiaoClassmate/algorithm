var input_count = 0;
var d = new Date();
var t = d.getTime();
var counter = -1;

//按"新增一筆目標金額"，增加目標金額進資料庫，並跳出新增成功視窗
function addThreshold(threshold) {
	if(input_count < 5) {
		input_count++;
		var id = input_count;
		var threshold = document.getElementById("threshold").value;
		firebase.database().ref('addThreshold/'+ myToken).child(input_count).set({
			id: input_count,
			threshold: parseInt(threshold,10)
		})
		.then(function() {
			Swal.fire({
				icon: 'success',
				title: '目標金額新增成功',
				showConfirmButton: false,
				timer: 1200
			});
		});
		resetThr();
	}
	else if(input_count = 5){
		Swal.fire({
			  icon: 'error',
			  title: '目標金額已達上限'
			})
	}
}
//使新增目標金額視窗的輸入框在新增後維持空白
function resetThr() {
	document.getElementById("form_2").reset();
}
//按"刪除一筆目標金額"，刪除資料庫目標金額最末的資料
function deleteThreshold(id) {
	var thr = firebase.database().ref('addThreshold/'+ myToken).child(input_count);
	thr.remove()
	.then(function() {
		input_count--;
	});
	document.getElementById("cardThreshold").innerHTML='';
	readThreshold();
}
//從資料庫讀取目標金額，並以card逐個顯示
function readThreshold() {
	var threshold = firebase.database().ref("addThreshold").child(myToken);
	threshold.on("child_added",function(data){
		var thresholdValue = data.val();

		document.getElementById("cardThreshold").innerHTML+=
		`
			<div class="mycard md-3 relative" id="${thresholdValue.id}">
				<div class="row">
					<div class="col-xs-9"><p class="card-text left">目標金額: ${thresholdValue.threshold}元</p></div>
				</div>
			</div>
		`
	});
}
//顯示時間
function ShowTime() {
	document.getElementById('showbox').innerHTML = d.getFullYear() + "/" + (d.getMonth()+1) + "/" + d.getDate() + "/&nbsp" + d.getHours() + ":" + d.getMinutes();
}
//按"新增商品"，增加商品詳細資訊進資料庫，並跳出新增成功視窗
function addList(img, name, price,number) {
	counter++;
	var NuPrice = document.getElementById("price").value;
	var Nunumber = document.getElementById("number").value;
	var img =document.getElementById("img").value;
	var name =document.getElementById("name").value;
	if(name || img){
		if(NuPrice && Nunumber){
			firebase.database().ref(myToken + "_add/").child(counter).set({
				id: counter,
				img: img,
				name: name,
				price: parseInt(NuPrice,10),
				number: parseInt(Nunumber,10)
			})
			.then(function() {
				Swal.fire({
					icon: 'success',
					title: '商品新增成功',
					showConfirmButton: false,
					timer: 1200
				});
			});
		} else {
			alert("missing must information");
		}
	} else {
		alert("missing must information");
	}
	reset();
}
//按編輯鍵更新商品卡片資訊
function updateGoods(id, img, name, price, number) {
	var goods = firebase.database().ref(myToken + "_add/");
	goods.on("child_added",function(data){
		var goodsValue = data.val();
		document.getElementById("card_" + goodsValue.id).addEventListener("submit",(e)=>
		{
			e.preventDefault();
		});
		document.getElementById("send_2").addEventListener("click",(e)=>
		{
			updateGoods2(
				id,
				document.getElementById("img_2").value,
				document.getElementById("name_2").value,
				document.getElementById("price_2").value,
				document.getElementById("number_2").value);
		});
		document.getElementById("img_2").value = img;
		document.getElementById("name_2").value = name;
		document.getElementById("price_2").value = price;
		document.getElementById("number_2").value = number;
	});
}
function updateGoods2(id, img, name, price, number) {
	var NuPrice = document.getElementById("price_2").value;
	var Nunumber = document.getElementById("number_2").value;
	var img =document.getElementById("img_2").value;
	var name =document.getElementById("name_2").value;
	if(name || img){
		if(NuPrice && Nunumber){
			firebase.database().ref(myToken + "_add/").child(id).set({
				id: id,
				img: img,
				name: name,
				price: parseInt(NuPrice,10),
				number: parseInt(Nunumber,10)
			});
		}
	}
	document.getElementById("cardSection").innerHTML='';
	readGoods();
}
//使新增商品視窗的輸入框在新增商品後維持空白
function reset() {
	document.getElementById("form").reset();
}
//按刪除鍵刪除商品卡片
function deleteGoods(id) {
	var goods = firebase.database().ref(myToken + "_add/" + id);
	goods.remove();
	document.getElementById("cardSection").innerHTML='';
	readGoods();
}
//從資料庫讀取商品內容，並以card逐個顯示，並有更新、刪除功能
function readGoods() {
	var goods = firebase.database().ref(myToken + "_add/");
	goods.on("child_added",function(data){
		var goodsValue = data.val();
		console.log(goodsValue);
		document.getElementById("cardSection").innerHTML+=
		`
			<div class="mycard md-3 relative" id="${goodsValue.id}">
				<div class="">
					<div class="col-xs-4">
						<img src="" style="width:100%" class="">
					</div>
					<div class="col-xs-8">
						<div class="row">
							<div class="col-xs-9"><p class="card-text left">商品: ${goodsValue.name}</p></div>
							<div class="col-xs-3">
								<svg id="updateGoods" onclick="updateGoods('${goodsValue.id}','${goodsValue.img}','${goodsValue.name}','${goodsValue.price}','${goodsValue.number}')" data-toggle="collapse" data-target="#card_${goodsValue.id}" aria-expanded="false" aria-controls="card_${goodsValue.id}" width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-pencil-square" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
									<path d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456l-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"/>
									<path fill-rule="evenodd" d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"/>
								</svg>
							</div>
						</div>
						<p class="card-text left" id="price_p">價格: ${goodsValue.price}元</p>
						<div class="row">
							<div class="col-xs-9"><p class="card-text left">數量: ${goodsValue.number}個</p></div>
							<div class="col-xs-3">
								<svg id="deleteGoods" onclick="deleteGoods('${goodsValue.id}')" width="1em" height="1em" viewBox="0 0 16 16" class="bi bi-trash" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
									<path d="M5.5 5.5A.5.5 0 0 1 6 6v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm2.5 0a.5.5 0 0 1 .5.5v6a.5.5 0 0 1-1 0V6a.5.5 0 0 1 .5-.5zm3 .5a.5.5 0 0 0-1 0v6a.5.5 0 0 0 1 0V6z"/>
									<path fill-rule="evenodd" d="M14.5 3a1 1 0 0 1-1 1H13v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V4h-.5a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1H6a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1h3.5a1 1 0 0 1 1 1v1zM4.118 4L4 4.059V13a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1V4.059L11.882 4H4.118zM2.5 3V2h11v1h-11z"/>
								</svg>
							</div>
						</div>
					</div>
				</div>
				<div class="collapse" id="card_${goodsValue.id}">
					<div>
						<div class="card card-body">
							<form class="inp" id="">
								<label class="word">商品圖片:</label>
								<input type="file" class="" id="img_2">
								<input type="button" class="" value="新增圖片" id="imgClick" onclick="img.click()">
								<br>
								<img class="img" src="" alt="">
								<label class="word">商品名稱:</label>
								<input type="text" class="" placeholder="請輸入商品名稱" id="name_2">
								<label class="word">商品價格:</label>
								<input type="text" class="" placeholder="請輸入商品價格" id="price_2">
								<label class="word">購買數量:</label>
								<input type="text" class="" placeholder="請輸入購買數量" id="number_2">
							</form>
						</div>
					</div>
					<div class="modal-footer">
						<button type="submit" id="cancel_2" data-toggle="collapse" data-target="#card_${goodsValue.id}" aria-expanded="false" aria-controls="card_${goodsValue.id}">取消</button>
						<button type="submit" id="send_2">完成</button>
					</div>
				</div>
			</div>
		`
	});
}
//預計用來顯示演算結果
function () {
	`
		<div class="mycard_2 md-3 relative">
			<p class="card-text left" id="">目標金額: 元</p>
		</div>
		<div class="mycard md-3 relative">
			<div class="">
				<div class="col-xs-4">
					<img src="" style="width:100%" class="">
				</div>
				<div class="col-xs-8">
					<div class="row">
						<div class="col-xs-9"><p class="card-text left">商品: </p></div>
					</div>
					<p class="card-text left" id="price_p">價格: 元</p>
					<div class="row">
						<div class="col-xs-9"><p class="card-text left">數量: 個</p></div>
					</div>
				</div>
			</div>
		</div>
	`
}