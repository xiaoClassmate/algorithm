<!DOCTYPE html>
<html lang="en">
<head>
    <!-- bootstrap.css -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css">
    
    <meta charset="UTF-8">
    <title>Hello</title>
</head>
<body>
    <!-- firebase.js -->
    <script src="https://www.gstatic.com/firebasejs/7.2.0/firebase-app.js"></script>
    <script src="https://www.gstatic.com/firebasejs/7.2.0/firebase-database.js"></script>

    <!-- firebase-config -->
    <script>
        var firebaseConfig = {
            apiKey: "AIzaSyCDuyQEcT7FbDI8kJkQ4TzP0Un3F4BwC3A",
            authDomain: "industriouswoman-myg36t91.firebaseapp.com",
            databaseURL: "https://industriouswoman-myg36t91.firebaseio.com",
            projectId: "industriouswoman-myg36t91",
            storageBucket: "industriouswoman-myg36t91.appspot.com",
            messagingSenderId: "902295424134",
            appId: "1:902295424134:web:7876cc39ae5fd3a0ea9507",
            measurementId: "G-DXZ0LF42BC"
        };

        firebase.initializeApp(firebaseConfig);

        function writeData(){
            firebase.database().ref("goods/").push({
                name: document.getElementById("goodsName").value,
                price: document.getElementById("goodsPrice").value,
                number: document.getElementById("goodsNumber").value
            });
        }
    </script>

    <!-- add goods form -->
    <div class="container" style="margin-top: 10%">
        <div class="row">
            <form id="form">
                <div class="form-group">
                    name:<input type="text" class="form-control" id="goodsName">
                    price:<input type="text" class="form-control" id="goodsPrice">
                    number:<input type="text" class="form-control" id="goodsNumber">
                </div>
                    <button id="createGoods" onclick="writeData()" class="btn btn-success">新增物品</button>
            </form>
        </div>
    </div>

    <!-- bootstrap.js -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js"></script>
</body>
</html>

