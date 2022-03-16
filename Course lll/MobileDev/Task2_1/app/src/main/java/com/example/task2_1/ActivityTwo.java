package com.example.task2_1;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.TextView;
import android.widget.Toast;

public class ActivityTwo extends AppCompatActivity {
    TextView textView;
    String value;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_two);

        Bundle extra = getIntent().getExtras();
        textView = findViewById(R.id.textView1);

        if (extra != null){
            value = extra.getString("data");
            textView.setText(value);
        }
    }

    public boolean onCreateOptionsMenu(Menu menu) {
        getMenuInflater().inflate(R.menu.mymenu, menu);
        return super.onCreateOptionsMenu(menu);
    }

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