var reToken =0;

//Email/Pwd註冊
function register(){
    var account = document.getElementById("account");
    var pwd = document.getElementById("pwd");
    var registerSmtBtn = document.getElementById("registerSmtBtn");

    registerSmtBtn.addEventListener("click",function(){
        console.log(account.value);
        reToken = myToken;
        myToken = account.value;
        firebase.auth().createUserWithEmailAndPassword(account.value, pwd.value).catch(
            function(error) {
                // Handle Errors here.
                var errorCode = error.code;
                var errorMsg = error.message;
                myToken = reToken;
                reToken = 0;
                console.log(errorMsg);
        });
    },false);
}
//登入
function login(){
    var accountL = document.getElementById("accountL");
    var pwdL = document.getElementById("pwdL");
    var loginSmtBtn = document.getElementById("loginSmtBtn");

    loginSmtBtn.addEventListener("click",function(){
            console.log(accountL.value);
            firebase.auth().signInWithEmailAndPassword(accountL.value, pwdL.value)
            .then(u => {
                // 登入成功
                reToken = myToken;
                myToken = u.uid;
                // expireDate = new Date();
                // expireDate.setTime(today.getTime()+1000*60*60*2*24) //一天
                setCookie('Token' ,myToken);
                window.location.assign("index");
            }).catch(
                function(error) {
                    // Handle Errors here.
                    var errorCode = error.code;
                    var errorMessage = error.message;
                    myToken = reToken;
                    reToken = 0;
                    console.log(myToken);
                    console.log(errorCode);
                    console.log(errorMessage);
            })
        },false);
}

//登出
function signout(){
    var signoutSmtBtn = document.getElementById("signoutSmtBtn");
    signoutSmtBtn.addEventListener("click",function(){
        firebase.auth().onAuthStateChanged(function(user) {
            if(user){
                var email =user.email;
                var expDate = new Date();
                expDate.setTime(expDate.getTime()-1);   // 設定 Cookie 的失效時間比目前時間還早
                document.cookie = escape('Token') + "=; expires=" + expDate.toGMTString(); // 重新設定 Cookie
                console.log("User sign out!" + email);
                window.location.assign("guest"); //返回遊客介面
            } else {
                console.log("User sign out error!");
            }
        })
    },false);
}


//維持登入
// firebase.auth().setPersistence(firebase.auth.Auth.Persistence.LOCAL)
//   .then(function() {
//     // 現在，現有和將來的Auth狀態僅保留在當前會話中。 即使用戶忘記註銷，關閉窗口也會清除任何現有狀態。
//     // ...
//     // 新的登錄將與會話持久性保持一致。
//     return firebase.auth().signInWithEmailAndPassword(accountL.value, pwdL.value);
//   })
//   .catch(function(error) {
//     // Handle Errors here.
//     var errorCode = error.code;
//     var errorMessage = error.message;
// });