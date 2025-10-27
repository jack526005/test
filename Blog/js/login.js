    function login() {
        var username = $("#username").val().trim();
        var password = $("#password").val().trim();

        if (username === "" || password === "") {
            alert("用户名和密码不能为空！");
            return false; 
        }
        window.location.href = "index.html";


    
    }