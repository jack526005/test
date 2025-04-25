const xhr=new XMLHttpRequest();//原生AJAX请求对象
//xhr.open("GET","https://yesno.wtf/api");
xhr.open("GET","https://v2.api-m.com/api/meinv");

//xhr.open("GET","https://v.api.aa1.cn/api/tiangou/");
//xhr.open("GET","https://v.api.aa1.cn/api/api-wenan-aiqing/index.php?type=json");
//xhr.open("GET","https://api.mhimg.cn/api/Box_office")
xhr.send()
xhr.onreadystatechange=function(){
  if(xhr.readyState==4 && xhr.status==200){
    console.log(xhr.responseText);//返回的json字符串
    const response=JSON.parse(xhr.responseText);
    console.log(response);
    let src=document.getElementById('sr');
    src.src=response.data;

    
  }
}
