package com.example.shiru.seethelight;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.webkit.WebView;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ProgressBar;
import android.widget.Toast;

import java.io.BufferedOutputStream;
import java.io.IOException;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.SocketTimeoutException;
import java.net.URL;

public class MainActivity extends AppCompatActivity {

    EditText etName ;

    WebView myWebView;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        etName = findViewById(R.id.editText);

         myWebView = (WebView) findViewById(R.id.webview);


        // initiate progress bar and start button
        final ProgressBar simpleProgressBar = (ProgressBar) findViewById(R.id.simpleProgressBar);
        Button startButton = (Button) findViewById(R.id.startButton);

        // perform click event on button
        startButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {


                // visible the progress bar
                simpleProgressBar.setVisibility(View.VISIBLE);


                myWebView.loadUrl("https://see-the-light.herokuapp.com/news/get?link="+ etName.getText().toString());



                /**

                URL url = null;
                try {
                    url = new URL("https://see-the-light.herokuapp.com/see-the-light/news");
                } catch (MalformedURLException e) {
                    e.printStackTrace();
                }
                HttpURLConnection client = null;
                try {
                    client = (HttpURLConnection) url.openConnection();
                    client.setRequestMethod("POST");

                    client.setRequestProperty("link","https://www.wikihow.com/Execute-HTTP-POST-Requests-in-Android");
                    client.setDoOutput(true);

                 HttpClient client = new DefaultHttpClient();

                 HttpGet request = new HttpGet("https://see-the-light.herokuapp.com/see-the-light/news");
                 ResponseHandler<String> handler = new BasicResponseHandler();
                 String response = "";
                 try {
                 response = client.execute(request, handler);
                 } catch (IOException e) {
                 e.printStackTrace();
                 }


                 }
                catch(SocketTimeoutException error) {
                //Handles URL access timeout.
                }
                catch (IOException error) {
                    //Handles input and output errors
                }
                finally {
                    if(client != null) // Make sure the connection is not null.
                        client.disconnect();
                }***/



                }
            });
    }
}
