package com.zyb.info

import android.app.ActivityManager
import android.os.Bundle
import android.os.Environment
import android.os.StatFs
import android.util.Log
import androidx.appcompat.app.AppCompatActivity
import androidx.navigation.NavController
import androidx.navigation.findNavController
import androidx.navigation.ui.AppBarConfiguration
import androidx.navigation.ui.setupActionBarWithNavController
import kotlinx.android.synthetic.main.account_icon_layout.*
import kotlinx.android.synthetic.main.contact_icon_layout.*
import kotlinx.android.synthetic.main.explore_icon_layout.*
import kotlinx.android.synthetic.main.message_icon_layout.*
import java.text.DecimalFormat


class MainActivity : AppCompatActivity() {
    private lateinit var navController: NavController
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        val manager = getSystemService(ACTIVITY_SERVICE) as ActivityManager
        val infoval = ActivityManager.MemoryInfo()
        manager.getMemoryInfo(infoval)
        Log.v("系统内存信息", bytesToHuman(infoval.availMem).toString()) //系统内存信息

        val statFs = StatFs(Environment.getDataDirectory().path) //调用该类来获取磁盘信息（而getDataDirectory就是内部存储）
        val tcounts = statFs.blockCountLong //总共的block数            3196073
        val counts = statFs.availableBlocksLong//获取可用的block数   3029039
        val size = statFs.blockSizeLong //每格所占的大小，一般是4KB==    4096
        val availROMSize = counts * size //可用内部存储大小               12406943744
        Log.v("可用内部存储大小 ", bytesToHuman(availROMSize).toString())
        val totalROMSize = tcounts * size //内部存储总大小                13091115008
        Log.v("内部存储总大小  ", bytesToHuman(totalROMSize).toString())
        val statFs1 = StatFs(getExternalFilesDir(null)?.path) //调用该类来获取磁盘信息（而getExternalStorageDirectory就是外置存储）
        val tcounts1 = statFs1.blockCountLong//总共的block数             3196073
        val counts1 = statFs1.availableBlocksLong //获取可用的block数    3029039
        val size1 = statFs1.blockSizeLong //每格所占的大小，一般是4KB==     4096
        val availROMSize1 = counts1 * size1 //可用内部存储大小               12406943744
        Log.v("可用外置存储大小  ", bytesToHuman(availROMSize1).toString())
        val totalROMSize1 = tcounts1 * size1 //内部存储总大小                13091115008
        Log.v("可用外置存储总大小        ", bytesToHuman(totalROMSize1).toString())
        val totalROMSize2 = tcounts1 * size1 //内部存储总大小

        val destinationMap = mapOf(
                R.id.messageFragment to messageMotionLayout,
                R.id.contactFragment to contactMotionLayout,
                R.id.exploreFragment to exploreMotionLayout,
                R.id.accountFragment to accountMotionLayout
        )
        navController = findNavController(R.id.fragment)
        setupActionBarWithNavController(
                navController,
                AppBarConfiguration(destinationMap.keys)
        )

        destinationMap.forEach { map ->
            map.value.setOnClickListener { navController.navigate(map.key) }
        }

        navController.addOnDestinationChangedListener { controller, destination, arguments ->
            controller.popBackStack()
            destinationMap.values.forEach { it.progress = 0.001f }
            destinationMap[destination.id]?.transitionToEnd()
        }


    }
    fun floatForm (d:Long): String {
        return DecimalFormat("#.##").format(d)
    }
    fun bytesToHuman (size:Long):String {
        val kb:Long = 1 * 1024
        val mb:Long = kb * 1024
        val gb:Long = mb * 1024
        val tb:Long = gb * 1024
        val pb:Long = tb * 1024
        val eb:Long = pb * 1024
        if (size < kb) return floatForm( size ) + " byte";
        if (size in kb until mb) return floatForm(size / kb) + " Kb";
        if (size in mb until gb) return floatForm(size / mb) + " Mb";
        if (size in gb until tb) return floatForm(size / gb) + " Gb";
        if (size in tb until pb) return floatForm(size / tb) + " Tb";
        if (size in pb until eb) return floatForm(size / pb) + " Pb";
        if (size >= eb) return floatForm(size / eb) + " Eb"; return "???"; }
}