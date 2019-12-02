import pymysql
import scraping as sc

def insert(result):
    db=pymysql.connect(port=3306,user='root',password='1q2w3e4r',charset='utf8',db='test')
    try:
        with db.cursor() as cursor:
            sql="""INSERT into trade_coin (company,type,trade_timestamp,opening_price,high_price,low_price,trade_price,prev_closing_price) values (%s,%s,%s,%s,%s,%s,%s,%s)"""
            cursor.execute(sql,(result[0],result[1],result[2],result[3],result[4],result[5],result[6],result[7]))
            db.commit()
    finally:
        db.close()
