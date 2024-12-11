package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.ListView;

public class songlist extends AppCompatActivity {
    ListView listView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_songlist);
        listView=findViewById(R.id.list);
        ArrayAdapter arrayAdapterr=new ArrayAdapter(getApplicationContext(),R.layout.list_item,getResources().getStringArray(R.array.songlist));
        listView.setAdapter(arrayAdapterr);
    }
}