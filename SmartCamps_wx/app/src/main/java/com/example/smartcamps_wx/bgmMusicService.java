package com.example.smartcamps_wx;

import android.app.Service;
import android.content.Intent;
import android.media.MediaPlayer;
import android.os.IBinder;

public class bgmMusicService extends Service {
    MediaPlayer mp;
    public bgmMusicService() {
    }

    @Override
    public IBinder onBind(Intent intent) {
        // TODO: Return the communication channel to the service.
        throw new UnsupportedOperationException("Not yet implemented");
    }
    public void onCreate() {

        super.onCreate();

        mp=MediaPlayer.create(getApplicationContext(),R.raw.youjing);
        System.out.println("onCreate()...");
    }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        if (mp!=null){
            mp.stop();
        }

        mp=MediaPlayer.create(getApplicationContext(),R.raw.youjing);
        mp.start();
        System.out.println("onStartCommand().....");
        return super.onStartCommand(intent, flags, startId);
    }

    @Override
    public void onDestroy() {
        super.onDestroy();
        mp.stop();
        System.out.println("onDestroy()....");
    }
}