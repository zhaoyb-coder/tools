package com.zyb.info;

import android.app.Activity;
import android.app.ActivityManager;
import android.content.Context;
import android.util.Log;

public class PhoneInfo extends Activity {

    public void getInfo(){
        ActivityManager manager = (ActivityManager) getSystemService(Context.ACTIVITY_SERVICE);
//        val manager = getSystemService(ACTIVITY_SERVICE) as ActivityManager
////        ActivityManager manager = (ActivityManager) getSystemService(Context.ACTIVITY_SERVICE);
////
////        ActivityManager.MemoryInfo info = new ActivityManager.MemoryInfo();
//        val info = ActivityManager.MemoryInfo();
//        manager.getMemoryInfo(info);
//        Log.v("PhoneInfo", String.valueOf(info.availMem));
        Log.v("PhoneInfo", "java------");
    }
}
