package com.example.smartcamps_wx;

import static com.example.smartcamps_wx.Register.KEY3;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.widget.CompoundButton;
import android.widget.Switch;
import android.widget.TextView;

import com.example.smartcamps_wx.R;
import com.example.smartcamps_wx.bgmMusicService;

public class Home extends AppCompatActivity {
    Switch switch_music;
    TextView textView;
    //static final String KEY3="useryhm";
    SharedPreferences preferences;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);
        textView=findViewById(R.id.name);
        preferences=getSharedPreferences("userinfo",AppCompatActivity.MODE_PRIVATE);

            String name=textView.getText().toString();
            name+=preferences.getString(KEY3,"error");
            textView.setText(name);


        switch_music=findViewById(R.id.s_music);
        switch_music.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton compoundButton, boolean b) {
                if (b){

                    System.out.println("1111111111111111111111111");
                    Intent intent=new Intent(Home.this, bgmMusicService.class);
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