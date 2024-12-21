package com.example.smartcamps_wx;

import static com.example.smartcamps_wx.Register.KEY1;
import static com.example.smartcamps_wx.Register.KEY2;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class Login extends AppCompatActivity {
    Button btn_Login;
    EditText ed_ID,ed_pass;
    SharedPreferences preferences;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);

        btn_Login=findViewById(R.id.btn_login);
        ed_ID=findViewById(R.id.et_account);
        ed_pass=findViewById(R.id.et_password);
        preferences=getSharedPreferences("userinfo",AppCompatActivity.MODE_PRIVATE);
        btn_Login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String truename=preferences.getString(KEY1,"error");
                String truepwd=preferences.getString(KEY2,"error");
                String name=ed_ID.getText().toString();
                String pwd=ed_pass.getText().toString();
                if (truename.equals(name)&&truepwd.equals(pwd)){
                    System.out.println("正确登录");
                    Intent intent=new Intent(Login.this,Home.class);
                    startActivity(intent);
                }
                else{
                    System.out.println("账号和密码错误");
                    Toast.makeText(getApplicationContext(), "账号密码错误", Toast.LENGTH_SHORT).show();

                }
            }
        });



    }
}