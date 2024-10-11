import java.util.ArrayList;
import java.util.List;

public class Example1 {
    public static void main(String[] args) {
        List intList=new ArrayList();
        intList.add(1);
        intList.add(2);
       // intList.add("3");   编译时不出错，运行时报错，因为是string型
        for (int i = 0; i <intList.size() ; i++) {
            Integer num=(Integer)intList.get(i); //强制转换为object型 Integer
            System.out.println(num);
            

        }
    }
}
