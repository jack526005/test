package network;

import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

public class Myserver implements Runnable {
    ServerSocket server = null;
    Socket clienSocket;
    boolean flog = true;
    Thread connenThread;
    BufferedReader sin = null;
    BufferedWriter sout = null;

    public static void main(String[] args) {
        Myserver MS = new Myserver();
        MS.serverStart();
    }

    public void serverStart() {
        try {
            server = new ServerSocket(8080);
            System.out.println("端口号" + server.getLocalPort());
            while (flog) {
                clienSocket = server.accept();
                System.out.println("连接建立完毕");
                InputStream is = clienSocket.getInputStream();
                sin = new BufferedReader(new InputStreamReader(is, "UTF-8"));
                OutputStream os = clienSocket.getOutputStream();
                sout = new BufferedWriter(new OutputStreamWriter(os, "UTF-8"));
                connenThread = new Thread(this);
                connenThread.start();
                String aLine;
                while ((aLine = sin.readLine()) != null) {
                    System.out.println(aLine);
                    if (aLine.equals("bye")) {
                        flog = false;
                        connenThread.interrupt();
                        break;
                    }
                }
            }
        } catch (Exception e) {
            System.out.println(e);
        } finally {
            try {
                if (sout != null) sout.close();
                if (sin != null) sin.close();
                if (clienSocket != null) clienSocket.close();
                if (server != null) server.close();
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
                sout.write(line);
                sout.newLine();
                sout.flush();
                if ("bye".equals(line)) {
                    // 当输入为 "bye" 时，设置标志位为 false 以停止循环
                    flog = false;
                    // 中断线程
                    connenThread.interrupt();
                    // 跳出当前循环
                    break;
                }
            }
        } catch (IOException e) {
            System.out.println(e);
        }
    }
}