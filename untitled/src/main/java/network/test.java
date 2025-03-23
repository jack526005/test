package network;

import javax.imageio.IIOException;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.*;
import java.net.URL;

public class test {
    public static void main(String[] args) {
        try{
            URL url1,url2,url3;
            url1=new URL("https://whit.fanya.chaoxing.com");
            BufferedReader reader=new BufferedReader(new InputStreamReader(url1.openStream()));
            String line;
            while ((line=reader.readLine())!=null){
                System.out.println(line);
            }
            reader.close();
        }catch (IIOException e){
            e.printStackTrace();
        } catch (MalformedURLException e) {
            throw new RuntimeException(e);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

    }
}
