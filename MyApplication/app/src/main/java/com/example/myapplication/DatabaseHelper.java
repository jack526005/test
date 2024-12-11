package com.example.myapplication;

import android.content.ContentValues;
import android.content.Context;
import android.database.Cursor;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;

public class DatabaseHelper extends SQLiteOpenHelper {

    // 数据库名称
    private static final String DATABASE_NAME = "mydatabase.db";
    // 数据库版本
    private static final int DATABASE_VERSION = 1;
    // 用户表名称
    private static final String TABLE_USERS = "users";
    // 用户表列名
    private static final String COLUMN_USERNAME = "username";
    private static final String COLUMN_PASSWORD = "password";

    public DatabaseHelper(Context context) {
        super(context, DATABASE_NAME, null, DATABASE_VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        // 创建用户表
        String CREATE_TABLE_USERS = "CREATE TABLE " + TABLE_USERS + "(" +
                COLUMN_USERNAME + " TEXT PRIMARY KEY," +
                COLUMN_PASSWORD + " TEXT" +
                ")";
        db.execSQL(CREATE_TABLE_USERS);
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        // 更新数据库时删除旧表并创建新表
        db.execSQL("DROP TABLE IF EXISTS " + TABLE_USERS);
        onCreate(db);
    }

    // 插入用户数据
    public boolean insertUser(String username, String password) {
        SQLiteDatabase db = this.getWritableDatabase();
        ContentValues values = new ContentValues();
        values.put(COLUMN_USERNAME, username);
        values.put(COLUMN_PASSWORD, password);
        long result = db.insert(TABLE_USERS, null, values);
        return result != -1; // 如果插入成功返回true，否则返回false
    }

    // 查询用户数据
    public Cursor getUser(String username) {
        SQLiteDatabase db = this.getReadableDatabase();
        return db.query(TABLE_USERS, null, COLUMN_USERNAME + "=?", new String[]{username}, null, null, null);
    }

    // 删除用户数据
    public boolean deleteUser(String username) {
        SQLiteDatabase db = this.getWritableDatabase();
        int result = db.delete(TABLE_USERS, COLUMN_USERNAME + "=?", new String[]{username});
        return result > 0; // 如果删除成功返回true，否则返回false
    }
}
