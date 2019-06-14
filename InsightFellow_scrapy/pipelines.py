# -*- coding: utf-8 -*-

# Define your Item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/Item-pipeline.html


import mysql.connector

class InsightfellowPipeline(object):
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            passwd = '',
            database = 'Insight_Fellow'
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS fellow_tb""")
        self.curr.execute(""" create table fellow_tb(
            Name text,
            Title text,
            Company text,
            Project text,
            Background text
        ) """)
    
    def process_item(self, item, spider):
        self.curr.execute("""insert into fellow_tb values(%s,%s,%s,%s,%s)""", ( 
            item['Name'][0],
            item['Title'][0],
            item['Company'][0],
            item['Project'][0],
            item['Background'][0]
        ))
        self.conn.commit()
        return item
        

    def close_spider(self, spider):
        self.curr.close()
        self.conn.close()