package com.example.smartcamps_wx;

import androidx.appcompat.app.AppCompatActivity;

import android.app.AlertDialog;
import android.app.DatePickerDialog;

import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.DatePicker;
import android.widget.EditText;
import android.widget.RadioButton;
import android.widget.RadioGroup;


public class Register extends AppCompatActivity {
    Button btn_set;
    Button btn_login;
    EditText edbirth,edname,edid,edpwd;
    RadioGroup rg;
    RadioButton rb_male,rb_female;
    String msg,sex;
    static final String KEY1="userID",KEY2="userPass",KEY3="useryhm",KEY4="userbirth",KEY5="userSex";
    SharedPreferences preferences;
    SharedPreferences.Editor editor;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);
        btn_set = findViewById(R.id.set);
        edbirth=findViewById(R.id.birth);
        edname=findViewById(R.id.et_username);
        edid=findViewById(R.id.ID);
        edpwd=findViewById(R.id.et_password);
        rg=findViewById(R.id.rg1);
        rb_male=findViewById(R.id.sex_m);
        rb_female=findViewById(R.id.sex_f);
        btn_login=findViewById(R.id.btn_register);
        preferences=getSharedPreferences("userinfo",AppCompatActivity.MODE_PRIVATE);
        editor=preferences.edit();

        DatePickerDialog.OnDateSetListener mDateSetListener = new DatePickerDialog.OnDateSetListener() {
            @Override
            public void onDateSet(DatePicker view, int year, int monthOfYear, int dayOfMonth) {

                String date = year + "-" + (monthOfYear + 1) + "-" + dayOfMonth;
                edbirth.setText(date);



            }
        };


        btn_set.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                new DatePickerDialog(Register.this, mDateSetListener, 2024, 11, 11).show();
            }
        });


        rg.setOnCheckedChangeListener(new RadioGroup.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(RadioGroup radioGroup, int i) {
                sex="";
                if (rg.getCheckedRadioButtonId()==R.id.sex_m){
                    sex+=rb_male.getText().toString();

                }
                if (rg.getCheckedRadioButtonId()==R.id.sex_f){
                    sex+=rb_female.getText().toString();

                }
            }
        });


        btn_login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                msg="";
                msg+="姓名："+edname.getText().toString()+"\n";
                msg+="性别："+sex+"\n";
                msg+="生日："+edbirth.getText().toString()+"\n";
                msg+="账号："+edid.getText().toString()+"\n";
                msg+="密码："+edpwd.getText().toString()+"\n";



                System.out.println(msg);
                AlertDialog.Builder builder = new AlertDialog.Builder(Register.this);
                builder.setTitle("注册界面");
                builder.setMessage(msg);
                builder.setPositiveButton("注册", new DialogInterface.OnClickListener() {
                    @Override
                    public void onClick(DialogInterface dialog, int which) {
                        editor.putString(KEY1,edid.getText().toString());
                        editor.putString(KEY2,edpwd.getText().toString());
                        editor.putString(KEY3,edname.getText().toString());
                        editor.putString(KEY4,edbirth.getText().toString());
                        editor.putString(KEY5,sex);
                        if (editor.commit()){
                            System.out.println("11111111");
                            Intent intent = new Intent(Register.this, MainActivity.class);
                            startActivity(intent);
                        }
                    }
                });

                builder.setNegativeButton("取消", null);
                AlertDialog dialog = builder.create();
                dialog.show();




            }
        });
    }
}