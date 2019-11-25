package com.project.khajit_app.activity.ui.other_profile

import androidx.lifecycle.ViewModelProviders
import android.os.Bundle
import android.text.method.ScrollingMovementMethod
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.*
import androidx.fragment.app.FragmentManager

import com.project.khajit_app.R
import com.project.khajit_app.activity.ListViewAdapter
import com.project.khajit_app.activity.OtherListViewAdapter
import com.project.khajit_app.activity.ui.followlist.FollowListFragment
import com.project.khajit_app.activity.ui.notificationdetails.notificationDetailFragment
import com.project.khajit_app.api.RetrofitClient
import com.project.khajit_app.data.models.FollowModel
import com.project.khajit_app.data.models.GeneralFollowModel
import com.project.khajit_app.data.models.GeneralFollowModel2
import com.project.khajit_app.data.models.GenericUserModel
import com.project.khajit_app.global.User
import interfaces.fragmentOperationsInterface
import retrofit2.Call
import retrofit2.Callback
import retrofit2.Response

class OtherUserProfile : Fragment(), fragmentOperationsInterface {
    var containerId : ViewGroup? = null

    private lateinit var viewModel: OtherUserProfileViewModel
    private lateinit var other_nameBox: TextView
    private lateinit var other_titleBox: TextView
    private lateinit var other_aboutBox: TextView
    private lateinit var other_followingBox: TextView
    private lateinit var other_followerBox: TextView
    private lateinit var other_traderImage: ImageView

    private lateinit var other_followerButton: Button
    private lateinit var other_followingButton: Button



    var equipments = arrayOf(
        "Android", "IPhone", "WindowsMobile", "Blackberry", "WebOS", "Ubuntu", "Windows7", "Max OS X", "Max OS X", "Max OS X")
    var rates = arrayOf(
        "%73", "%73", "%73", "%73", "%73", "%73", "%73", "%73", "%73", "%73")

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View? {
        super.onCreate(savedInstanceState)

        viewModel =
            ViewModelProviders.of(this).get(OtherUserProfileViewModel::class.java)
        val root = inflater.inflate(R.layout.other_user_profile_fragment, container, false)
        containerId = container

        var other_id = arguments?.getInt("id").toString()

        other_nameBox = root.findViewById(R.id.other_user_real_name) as TextView
        other_titleBox = root.findViewById(R.id.other_user_title) as TextView
        other_aboutBox = root.findViewById(R.id.other_text_bio) as TextView
        other_followingBox = root.findViewById(R.id.other_following_number) as TextView
        other_followerBox = root.findViewById(R.id.other_follower_number) as TextView
        other_traderImage = root.findViewById(R.id.other_trader_image) as ImageView
        other_followerButton = root.findViewById(R.id.other_follower_button) as Button
        other_followingButton = root.findViewById(R.id.other_following_button) as Button

        var public = false
        var isFollowing = false

        // This will be used for further methods in order to set prediction rates
        var lview =  root.findViewById(R.id.other_list_prediction_name) as ListView
        var ladapter = OtherListViewAdapter(this, equipments, rates)
        lview.adapter = ladapter


        RetrofitClient.instance.getInfo(other_id).enqueue(object :
            Callback<GenericUserModel> {
            override fun onResponse(
                call: Call<GenericUserModel>,
                response: Response<GenericUserModel>
            ) {
                println(response.toString())
                if(response.code() == 200 ){
                    if(response.body()?.detail != null){
                        println("PROBLEM")
                    }else{
                        other_nameBox.text = response.body()?.first_name + " " + response.body()?.last_name
                        other_titleBox.text = response.body()?.title
                        other_aboutBox.text = response.body()?.biography
                        public = response.body()?.is_public!!
                        var isTrader = response.body()?.groups?.get(0).equals("trader")

                        if(isTrader == true) {
                            other_traderImage.alpha = 1F
                        }
                    }
                }else{

                }
            }
            override fun onFailure(call: Call<GenericUserModel>, t: Throwable) {

            }
        })

        RetrofitClient.instance.followerListID(other_id).enqueue(object :
            Callback<GeneralFollowModel2> {
            override fun onResponse(
                call: Call<GeneralFollowModel2>,
                response: Response<GeneralFollowModel2>
            ) {
                println(response.toString())
                if(response.code() == 200 ){
                    if(response.body()?.detail != null){
                        println("NOT CHANGED")
                    }else{
                        var count = response.body()?.list?.count()!!.toString()
                        other_followerBox.text = count
                    }
                }else{

                }
            }
            override fun onFailure(call: Call<GeneralFollowModel2>, t: Throwable) {

            }
        })

        RetrofitClient.instance.followingListID(other_id).enqueue(object :
            Callback<GeneralFollowModel> {
            override fun onResponse(
                call: Call<GeneralFollowModel>,
                response: Response<GeneralFollowModel>
            ) {
                println(response.toString())
                if(response.code() == 200 ){
                    if(response.body()?.detail != null){
                        println("NOT CHANGED")

                    }else{
                        var count = response.body()?.list?.count()!!.toString()
                        other_followingBox.text = count
                    }
                }else{

                }
            }
            override fun onFailure(call: Call<GeneralFollowModel>, t: Throwable) {

            }
        })


        other_followerButton.setOnClickListener { root ->
            followList(root, "follower", other_id.toInt())
        }

        other_followingButton.setOnClickListener { root ->
            followList(root, "following", other_id.toInt())
        }

        return root
    }


    fun followList(view: View, request: String, other_id: Int) {
        val parentActivityManager : FragmentManager = activity?.supportFragmentManager as FragmentManager


        fragmentTransaction(
            parentActivityManager,
            FollowListFragment.newInstance(request, other_id),
            (containerId!!.id),
            true,
            true,
            false
        )
    }

    companion object {
        fun newInstance(id: Int): OtherUserProfile {
            val fragmentUser = OtherUserProfile()
            val args = Bundle()
            args.putSerializable("id",id)
            fragmentUser.arguments = args
            return fragmentUser
        }

    }
}
