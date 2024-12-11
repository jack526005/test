package com.example.myapplication;

import android.content.Intent;
import android.database.sqlite.SQLiteDatabase;
import android.media.MediaPlayer;
import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;

import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import com.example.myapplication.R;

import java.io.IOException;

public class MainActivity extends AppCompatActivity {

    private MediaPlayer mediaPlayer;

    Button btn_rg;
    Button btn_in;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);


        btn_rg=findViewById(R.id.btn_register);
        btn_in=findViewById(R.id.btn_login);
        btn_rg.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(MainActivity.this, regsit.class);
                startActivity(intent);


            }
        });


        btn_in.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent1=new Intent(MainActivity.this,musu.class);
                startActivity(intent1);
            }
        });


    }
}