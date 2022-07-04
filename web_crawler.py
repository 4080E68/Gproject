from selenium import webdriver
import mysql.connector
import time
import random
import string
#使用quote進行中文轉碼
from urllib.parse import quote
from web_crawler import *


def web_crawler(keyword):
    connection = mysql.connector.connect(host='localhost',
                                         port='3306',
                                         user='root',
                                         password='0000',
                                         database='test',)

    cursor = connection.cursor()
    try:

        #建立url跟目錄
        

        driver = webdriver.Chrome()
        #調整瀏覽器視窗大小
        driver.set_window_size(1024, 960)

        #進入指定網址
        url = 'https://shopping.pchome.com.tw/'
        driver.get(url)

        search_vedio = driver.find_element_by_id('keyword')
        
        search_vedio.send_keys(keyword)
        time.sleep(1)

        search_button = driver.find_element_by_id('doSearch')
        search_button.click()
        #等待網頁讀取

        time.sleep(2)

        driver.refresh()  # 刷新網頁

        for i in range(20):
            y_position = i*70
            driver.execute_script(f'window.scrollTo(0, {y_position});')
            time.sleep(0.1)
        
        #======================從網頁獲取商品連結===========================
        #建立商品url列表
        pc_url_list = []
        pc_urls = driver.find_elements_by_css_selector('.prod_img')
        #將每個商品連結放入連結list
        #print(len(pc_urls))
        for url in pc_urls:
            if len(pc_url_list) < 10:
                    pc_url_list.append(url.get_attribute('href'))

        #======================從網頁獲取圖片連結===========================
        #建立圖片列表
        pc_images = []
        pc_images_urls = driver.find_elements_by_css_selector('.prod_img img')

        #將每個圖片放入圖片list
        for image in pc_images_urls:
            if len(pc_images) < 10:
                    pc_images.append(image.get_attribute('src'))
       
        #======================從網頁獲取商品標題===========================
        #建立標題列表
        pc_title_list = []
        pc_title_infos = driver.find_elements_by_css_selector('.prod_img img')
        for infos in pc_title_infos:
            if len(pc_title_list) < 10:
                pc_title_list.append(infos.get_attribute('title'))
                
        #======================從網頁獲取商品資訊===========================
        Commodity_list = []
        Commodity_web = driver.find_elements_by_css_selector(".nick")
        #將價錢放置陣列
        print(len(Commodity_list))
        for Commodity in Commodity_web:
            if len(Commodity_list) < 10:
                Commodity_list.append(Commodity.text)
        #======================從網頁獲取價錢===========================
        price_list = []
        price_web = driver.find_elements_by_css_selector(".price .value")
        #將價錢放置陣列
        for price in price_web:
            if len(price_list)<10:
                price_list.append(price.text)
        
        
        print("商品連結數量", len(pc_url_list))
        print("圖片連結數量", len(pc_images))
        print("商品資訊數量", len(Commodity_list))
        print("價錢數量", len(price_list))
        print("標題數量", len(pc_title_list))
        print("儲存成功")

        
        try:
            for i in range(10):
                
                sql = 'INSERT INTO `test`.`test` (`id`,`name`, `price`, `Commodity`, `url_list`, `pc_images`) VALUES (%s,%s, %s, %s, %s, %s);'
                cursor.execute(
                    sql, (i+1, pc_title_list[i], price_list[i], Commodity_list[i], pc_url_list[i], pc_images[i],))
            
                connection.commit()
            

        except:
                connection.rollback()
        driver.close()
        #=====================================================================
        cursor.close()
        connection.close()
    except:
        print("錯誤")
        

if __name__ == '__main__':
    message = web_crawler('SSD')
