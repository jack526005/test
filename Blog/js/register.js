  function register() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    if (username === "" || password === "") {
        alert("用户名和密码不能为空！");
        return false;
    }
   
    window.location.href = "login.html";
    
  }