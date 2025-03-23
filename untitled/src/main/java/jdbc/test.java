package jdbc;

import java.sql.*;

public class test {

    public static void main(String[] args) {
        String url="jdbc:mysql://localhost:3306/school";
        String userName="root";
        String passWord="123456";
        try {
            Connection connection= DriverManager.getConnection(url,userName,passWord);
            Statement statement=connection.createStatement();
            String sqlStr="select * from users";
            ResultSet rs=statement.executeQuery(sqlStr);
            System.out.println("用户表");

            while (rs.next()){
                int Id =rs.getInt("Id");
                String Username=rs.getNString("Username");
                String Password=rs.getNString("Password");


                System.out.println("id:"+Id+"   用户名:"+Username+"   密码:"+passWord);
            }
            rs.close();
            statement.close();
            connection.close();
        }catch (SQLException e){
            e.printStackTrace();
        }

    }
}
