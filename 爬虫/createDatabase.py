#!/usr/bin/python
# coding: utf-8
import pymysql, time, datetime

def createOriginalDatabase():
    conn = pymysql.connect("localhost", "root", "Ilovexukeyu", "test", 3306)
    # conn.text_factory = str
    cursor = conn.cursor()
    # 需要解析的数据表
    # cursor.execute(
        # 'create table comments(id varchar, movieId varchar, name varchar(40), comment TEXT, gender varchar, addTime varchar(20))')
    # 原始数据表
    cursor.execute('create table originalData(id varchar(100), movieId varchar(100), originalInfo varchar(4000), movieName varchar(4000));')
    cursor.close()
    conn.commit()
    conn.close()

def createDealDatabase():
    conn = pymysql.connect("localhost", "root", "Ilovexukeyu", "test", 3306)
    # conn.text_factory = str
    cursor = conn.cursor()
    createTable = """CREATE TABLE realData (
	id	varchar(100),
	content	varchar(4000),
	gender	varchar(100),
	addDate	varchar(400),
	uname	varchar(400),
	userid	varchar(400),
	msgId	varchar(400),
	uidType	varchar(400)
);"""
    # 需要解析的数据表
    cursor.execute(createTable)
    cursor.close()
    conn.commit()
    conn.close()

if __name__ == '__main__':
    # 只能创建一次
    #createOriginalDatabase()
    createDealDatabase()