package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class regsit extends AppCompatActivity {
    Button btn2;
    EditText ed1,ed2;
    private DatabaseHelper dbHelper;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_regsit);
        ed1=findViewById(R.id.et_username);
        ed2=findViewById(R.id.et_password);
        dbHelper = new DatabaseHelper(this);

        btn2=findViewById(R.id.btn_register);
        btn2.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                dbHelper.insertUser(ed1.toString(),ed2.toString());
                Toast.makeText(regsit.this, "注册成功", Toast.LENGTH_SHORT).show();
                Intent intent = new Intent(regsit.this, MainActivity.class);
                startActivity(intent);
            }
        });
    }
}