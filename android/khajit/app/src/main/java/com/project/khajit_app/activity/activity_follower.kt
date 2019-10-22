package com.project.khajit_app.activity

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.view.Menu
import android.view.MenuItem
import android.widget.Button
import android.widget.FrameLayout
import android.widget.ListView
import android.widget.Toast
import androidx.fragment.app.Fragment
import com.google.android.material.bottomnavigation.BottomNavigationView
import com.project.khajit_app.R
import com.project.khajit_app.activity.ui.equipment.EquipmentFragment
import com.project.khajit_app.activity.ui.home.HomeFragment
import com.project.khajit_app.activity.ui.mailbox.MailboxFragment
import com.project.khajit_app.activity.ui.notifications.NotificationsFragment
import com.project.khajit_app.activity.ui.search.SearchFragment
import com.project.khajit_app.activity.ui.settings.SettingsFragment
import com.project.khajit_app.api.RetrofitClient
import com.project.khajit_app.data.models.FollowerModel
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

class activity_follower : AppCompatActivity() {

    private var list_usernames = arrayListOf<String>()
    private var list_ids = arrayListOf<Int>()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_followcommon)

        val btn = findViewById<Button>(R.id.button_flw)
        btn.text = "Follower List"

        RetrofitClient.instance.followerList().enqueue(object :
            Callback<List<FollowerModel>> {
            override fun onResponse(
                call: Call<List<FollowerModel>>,
                response: Response<List<FollowerModel>>
            ) {
                println(response.toString())
                if(response.code() == 200 ){

                    list_usernames.clear()
                    list_ids.clear()
                    var size = response.body()?.size
                    for (a in 1..size!!) {
                        list_usernames.add(response.body()?.get(a-1)!!.follower.username)
                        list_ids.add(response.body()?.get(a-1)!!.follower.id)
                    }
                    // This will be used for further methods in order to set prediction rates
                    var lview =  findViewById<ListView>(R.id.list_users_follow) as ListView
                    var ladapter = FollowerViewAdapter(this@activity_follower, list_usernames)
                    lview.adapter = ladapter

                }else{
                    Log.d("error message:", response.message())
                }
            }
            override fun onFailure(call: Call<List<FollowerModel>>, t: Throwable) {
                Toast.makeText(applicationContext,t.message, Toast.LENGTH_LONG).show()
            }
        })
    }

}
