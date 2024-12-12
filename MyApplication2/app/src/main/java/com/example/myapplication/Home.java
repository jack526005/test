package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.widget.CompoundButton;
import android.widget.Switch;

public class Home extends AppCompatActivity {
    Switch switch_music;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);
        switch_music=findViewById(R.id.s_music);
        switch_music.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton compoundButton, boolean b) {
                if (b){

                    System.out.println("1111111111111111111111111");
                    Intent intent=new Intent(Home.this,bgmMusicService.class);
                    startService(intent);
                }
                else{

                    System.out.println("00000000000000000000000000");
                    Intent intent=new Intent(Home.this,bgmMusicService.class);
                    stopService(intent);
                }
            }
        });


    }
}