package network;

import java.net.InetAddress;
import java.net.UnknownHostException;

public class ipaddress {
    InetAddress myipaddress=null;
    InetAddress server=null;

    public static void main(String[] args) {
        ipaddress ipaddress=new ipaddress();

        System.out.println(ipaddress.myip());
        System.out.println(ipaddress.ServerIp());
        System.out.println();
    }
    public InetAddress myip(){
        try{
            myipaddress=InetAddress.getLocalHost();

        } catch (UnknownHostException e) {

        }
        return myipaddress;
    }
    public InetAddress ServerIp(){
        try{
            server=InetAddress.getByName("www.baidu.com");


        } catch (UnknownHostException e) {

        }
        return (server);
    }
}
