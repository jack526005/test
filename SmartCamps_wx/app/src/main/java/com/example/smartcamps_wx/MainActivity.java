package com.example.smartcamps_wx;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {
    Button btn1;
    Button btn2;
    EditText ed1,ed2;
    SharedPreferences preferences;
    static final String KEY1="userName",KEY2="userPass";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        btn1=findViewById(R.id.btn_register);
        btn2=findViewById(R.id.btn_login);
        ed1=findViewById(R.id.et_account);
        ed2=findViewById(R.id.et_password);
        preferences=getSharedPreferences("userinfo",AppCompatActivity.MODE_PRIVATE);
        btn1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent=new Intent(MainActivity.this,Register.class);
                startActivity(intent);

            }
        });
        btn2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                String truename=preferences.getString(KEY1,"error");
                String truepwd=preferences.getString(KEY2,"error");
                String name=ed1.getText().toString();
                String pwd=ed2.getText().toString();
                if (truename.equals(name)&&truepwd.equals(pwd)){
                    System.out.println("正确登录");
                    Intent intent=new Intent(MainActivity.this,Home.class);
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