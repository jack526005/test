/*package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.media.MediaPlayer;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

import java.lang.reflect.Array;

public class musu extends AppCompatActivity {
    Button btn3;
    MediaPlayer mediaPlayer;
    boolean isPlaying=false;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_musu);
        btn3=findViewById(R.id.play_pause_button);
        mediaPlayer = MediaPlayer.create(this, R.raw.music);



        btn3.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
               /* if (mediaPlayer!= null) {
                    mediaPlayer.start();
                }*/

                /*if (!isPlaying) {
                    mediaPlayer.start();
                    btn3.setText("暂停");
                    isPlaying = true;
                } else {
                    mediaPlayer.pause();
                    btn3.setText("播放");
                    isPlaying = false;
                }
            }
        });



    }


    }*/





/*package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;


import android.media.MediaPlayer;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;



public class musu extends AppCompatActivity {
    Button prevButton;
    Button playPauseButton;
    Button nextButton;
    MediaPlayer mediaPlayer;
    boolean isPlaying = false;
    private int[] musicResources = {R.raw.music, R.raw.music_2, R.raw.music_3}; // 根据实际音乐文件添加资源ID
    private int currentMusicIndex = 0;
    private TextView songTitleTextView;
    private TextView singerNameTextView;
    private ImageView songCoverImageView;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_musu);

        // 找到各个视图控件
        prevButton = findViewById(R.id.prev_button);
        playPauseButton = findViewById(R.id.play_pause_button);
        nextButton = findViewById(R.id.next_button);
        songTitleTextView = findViewById(R.id.song_title_text);
        singerNameTextView = findViewById(R.id.singer_name_text);
        songCoverImageView = findViewById(R.id.song_cover_image);

        // 初始化MediaPlayer，播放第一首音乐
        mediaPlayer = MediaPlayer.create(this, musicResources[currentMusicIndex]);

        // 设置播放/暂停按钮的点击监听器
        playPauseButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (!isPlaying) {
                    mediaPlayer.start();
                    playPauseButton.setText("暂停");
                    isPlaying = true;
                } else {
                    mediaPlayer.pause();
                    playPauseButton.setText("播放");
                    isPlaying = false;
                }
            }
        });

        // 设置上一首按钮的点击监听器
        prevButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                changeToPrevMusic();
            }
        });

        // 设置下一首按钮的点击监听器
        nextButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                changeToNextMusic();
            }
        });
    }

    // 切换到上一首音乐的方法
    private void changeToPrevMusic() {

        if (mediaPlayer!= null) {
            mediaPlayer.stop();
            mediaPlayer.release();
        }
        currentMusicIndex--;
        if (currentMusicIndex < 0) {
            currentMusicIndex = musicResources.length - 1;
        }
        mediaPlayer = MediaPlayer.create(this, musicResources[currentMusicIndex]);
        mediaPlayer.start();
    }

    // 切换到下一首音乐的方法
    private void changeToNextMusic() {

        if (mediaPlayer!= null) {
            mediaPlayer.stop();
            mediaPlayer.release();
        }
        currentMusicIndex++;
        if (currentMusicIndex >= musicResources.length) {
            currentMusicIndex = 0;
        }
        mediaPlayer = MediaPlayer.create(this, musicResources[currentMusicIndex]);
        mediaPlayer.start();


    }





    @Override
    protected void onDestroy() {
        super.onDestroy();
        if (mediaPlayer!= null) {
            mediaPlayer.release();
        }
    }
}*/



package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.view.menu.MenuBuilder;

import android.content.Intent;
import android.media.MediaPlayer;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class musu extends AppCompatActivity {
    Button mybtn;
    Button prevButton;
    Button playPauseButton;
    Button nextButton;
    Button localButton;
    Button MainButton;
    MediaPlayer mediaPlayer;
    boolean isPlaying = false;
    private int[] musicResources = {R.raw.music, R.raw.music_2, R.raw.music_3}; // 根据实际音乐文件添加资源ID
    private int currentMusicIndex = 0;
    private TextView songTitleTextView;
    private TextView singerNameTextView;
    private ImageView songCoverImageView;
    private List<Map<String, String>> musicInfoList = new ArrayList<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_musu);

        // 找到各个视图控件
        prevButton = findViewById(R.id.prev_button);
        playPauseButton = findViewById(R.id.play_pause_button);
        nextButton = findViewById(R.id.next_button);
        localButton=findViewById(R.id.local_button);
        mybtn=findViewById(R.id.my_button);

        songTitleTextView = findViewById(R.id.song_title_text);
        singerNameTextView = findViewById(R.id.singer_name_text);
        songCoverImageView = findViewById(R.id.song_cover_image);

        // 初始化歌曲信息列表
        initMusicInfoList();

        // 初始化MediaPlayer，播放第一首音乐
        mediaPlayer = MediaPlayer.create(this, musicResources[currentMusicIndex]);

        // 设置播放/暂停按钮的点击监听器
        playPauseButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (!isPlaying) {
                    mediaPlayer.start();
                    playPauseButton.setText("暂停");
                    isPlaying = true;
                } else {
                    mediaPlayer.pause();
                    playPauseButton.setText("播放");
                    isPlaying = false;
                }
            }
        });
        mybtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(musu.this, my.class);
                startActivity(intent);
            }
        });

        // 设置上一首按钮的点击监听器
        prevButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                changeToPrevMusic();
            }
        });

        // 设置下一首按钮的点击监听器
        nextButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                changeToNextMusic();
            }
        });
        localButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(musu.this, songlist.class);
                startActivity(intent);

            }
        });

    }

    // 切换到上一首音乐的方法
    private void changeToPrevMusic() {
        currentMusicIndex--;
        if (currentMusicIndex < 0) {
            currentMusicIndex = musicResources.length - 1;
        }
        resetMediaPlayer(currentMusicIndex);
        updateMusicInfoUI();
    }

    // 切换到下一首音乐的方法
    private void changeToNextMusic() {
        currentMusicIndex++;
        if (currentMusicIndex >= musicResources.length) {
            currentMusicIndex = 0;
        }
        resetMediaPlayer(currentMusicIndex);
        updateMusicInfoUI();
    }

    // 初始化歌曲信息列表的方法
    private void initMusicInfoList() {
        Map<String, String> music1Info = new HashMap<>();
        music1Info.put("songName", "双笙");
        music1Info.put("singer", "陈元汐");
        music1Info.put("resourceId", "R.raw.music");
        musicInfoList.add(music1Info);

        Map<String, String> music2Info = new HashMap<>();
        music2Info.put("songName", "坏女孩");
        music2Info.put("singer", "Veena/Reyna");
        music2Info.put("resourceId", "R.raw.music_2");
        musicInfoList.add(music2Info);

        Map<String, String> music3Info = new HashMap<>();
        music3Info.put("songName", "春泥");
        music3Info.put("singer", "一个球");
        music3Info.put("resourceId", "R.raw.music_3");
        musicInfoList.add(music3Info);
    }

    // 重置MediaPlayer的方法，用于释放旧资源并创建新的播放资源
    private void resetMediaPlayer(int newIndex) {
        if (mediaPlayer!= null) {
            mediaPlayer.stop();
            mediaPlayer.release();
        }
        mediaPlayer = MediaPlayer.create(this, musicResources[newIndex]);
        mediaPlayer.start();
    }

    // 根据索引获取音乐资源ID的方法
    private int getMusicResourceId(int index) {
        Map<String, String> musicInfo = musicInfoList.get(index);
        if (musicInfo!= null) {
            String resourceIdStr = musicInfo.get("resourceId");
            if (resourceIdStr!= null) {
                return getResources().getIdentifier(resourceIdStr.substring(2, resourceIdStr.length() - 1), "raw", getPackageName());
            }
        }
        return -1; // 如果出现问题，返回一个默认值或者抛出异常，这里返回-1作为示意
    }

    // 更新界面显示歌曲名和歌手名的方法
    private void updateMusicInfoUI() {
        String songName = musicInfoList.get(currentMusicIndex).get("songName");
        String singerName = musicInfoList.get(currentMusicIndex).get("singer");
        songTitleTextView.setText(songName);
        singerNameTextView.setText(singerName);
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        if (mediaPlayer!= null) {
            mediaPlayer.release();
        }
    }

}
