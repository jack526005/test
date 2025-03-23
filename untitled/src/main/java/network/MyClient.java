package network;

import java.io.*;
import java.net.Socket;

public class MyClient implements Runnable {
    Socket clientSocket;
    boolean flog = true;
    Thread connenThread;
    BufferedReader cin;
    BufferedWriter cout;

    public static void main(String[] args) {
        new MyClient().clientStart();
    }

    public void clientStart() {
        try {
            clientSocket = new Socket("localhost", 8080);
            System.out.println("已建立连接");
            // 初始化 connenThread
            connenThread = new Thread(this);
            InputStream is = clientSocket.getInputStream();
            cin = new BufferedReader(new InputStreamReader(is, "UTF-8"));
            OutputStream os = clientSocket.getOutputStream();
            cout = new BufferedWriter(new OutputStreamWriter(os, "UTF-8"));
            // 启动线程
            connenThread.start();
            String aLine;
            while ((aLine = cin.readLine()) != null) {
                System.out.println(aLine);
                if (aLine.equals("bye")) {
                    flog = false;
                    connenThread.interrupt();
                    break;
                }
            }
        } catch (Exception e) {
            System.out.println(e);
        } finally {
            try {
                if (cout != null) cout.close();
                if (cin != null) cin.close();
                if (clientSocket != null) clientSocket.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    @Override
    public void run() {
        try {
            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in, "UTF-8"));
            String line;
            while ((line = reader.readLine()) != null) {
                cout.write(line);
                cout.newLine();
                cout.flush();

            }
        } catch (IOException e) {
            System.out.println(e);
        }
    }
}