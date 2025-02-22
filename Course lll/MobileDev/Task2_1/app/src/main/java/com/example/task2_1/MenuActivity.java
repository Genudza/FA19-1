package com.example.task2_1;

import android.content.Intent;
import android.view.Menu;
import android.view.MenuItem;

import androidx.appcompat.app.AppCompatActivity;

public class MenuActivity extends AppCompatActivity {


    // создание меню из XML
    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.mymenu, menu);
        return super.onCreateOptionsMenu(menu);
    }

    // обработка нажатий
    @Override
    public boolean onOptionsItemSelected(MenuItem item) {


        Intent intent;
        switch (item.getTitle().toString()) {
            case "Activity 1":
                intent = new Intent(this, MainActivity.class);
                startActivity(intent);
                break;
            case "Activity 2":
                intent = new Intent(this, ActivityTwo.class);
                startActivity(intent);
                break;
            case "Activity 3":
                intent = new Intent(this, ActivityThree.class);
                startActivity(intent);
                break;
            case "Activity 4":
                intent = new Intent(this, ActivityFour.class);
                startActivity(intent);
                break;
            default:
                break;
        }
        return true;
    }
}
