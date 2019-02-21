package com.example.shiru.seethelight;

import android.content.ClipData;
import android.content.ClipboardManager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.webkit.WebView;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.example.shiru.seethelight.R;

import static android.content.Context.CLIPBOARD_SERVICE;

public class MainActivity extends AppCompatActivity {

    Button btn_copy,btn_paste;
    TextView txttext;
    TextView ettext;
    ClipboardManager clipboardManager;
    WebView myWebView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //btn_copy = findViewById(R.id.btn_copy);
        btn_paste = findViewById(R.id.btn_paste);
        txttext = findViewById(R.id.textDisplay);
        ettext = findViewById(R.id.textWrite);
        myWebView = findViewById(R.id.mywebview);

        clipboardManager = (ClipboardManager) getSystemService(CLIPBOARD_SERVICE);


        if(!clipboardManager.hasPrimaryClip())
        {
            btn_paste.setEnabled(false);

        }

     /*   btn_copy.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                String text = ettext.getText().toString();

                if(!text.equals( ""))
                {
                   // ClipData clipData = ClipData.newPlainText("text", text);
                    //clipboardManager.setPrimaryClip(clipData);


                    ClipData clipData = ClipData.newPlainText("text", text);
                    clipboardManager.setPrimaryClip(clipData);




                    Toast.makeText(MainActivity.this,"Copied",Toast.LENGTH_SHORT ).show();
                    btn_paste.setEnabled(true);
                }
            }
        });*/


        btn_paste.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                ClipData clipData = clipboardManager.getPrimaryClip();
                ClipData.Item item = clipData.getItemAt(0);
git
                myWebView.loadUrl("https://see-the-light.herokuapp.com/news/get?link="+ item.getText().toString());

                // txttext.setText(item.getText().toString());

                Toast.makeText(MainActivity.this,"Pasted",Toast.LENGTH_SHORT).show();

            }
        });

    }
}
