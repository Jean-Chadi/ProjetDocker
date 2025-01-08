# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import mysql.connector


class BooksPipeline:
    def process_item(self, item, spider):
        return item

class ConversionPipeline:
    def process_item(self, item, spider):
        prix = item['prix']
        item['prix'] = round(float(prix[1:])*1.198, 2)
        return item
    
class MysqlPipeline:
    def process_item(self, item, spider):
        mydb = mysql.connector.connect(
        host="localhost",
        user="toto",
        password="toto",
        database="Produits"
        )

        mycursor = mydb.cursor()

        sql = "INSERT INTO Livre (titre, prix, genre) VALUES (%s, %s, %s)"
        val = (item['titre'], item['prix'], item['genre'])
        mycursor.execute(sql, val)

        mydb.commit()

        return item