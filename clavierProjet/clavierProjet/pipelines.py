# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector


class ClavierprojetPipeline:
    def process_item(self, item, spider):
        return item

class DatabaseInsertionPipeline:
    def process_item(self, item, spider):
        mydb = mysql.connector.connect(
        host="localhost",
        user="toto",
        password="toto",
        database="bdd"
        )

        mycursor = mydb.cursor()

        sql = "INSERT INTO clavier(titre, marque, prix, nom_site, lien) VALUES (%s, %s, %s, %s, %s)"
        val = (item['titre'], item['marque'], item['prix'], item['site'], item['lien'])
        mycursor.execute(sql, val)

        mydb.commit()

        return item