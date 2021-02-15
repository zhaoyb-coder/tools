from util.util import Util
from engine.engine import Engine
import time


class Bing(Engine):
    HOME_URL = 'https://cn.bing.com/images/'

    def __init__(self, web_driver, keys, storing_folder):
        Engine.__init__(self, web_driver)
        self.storing_folder = storing_folder
        self.keys = keys

    def retrieve_image(self):
        Engine.retrieve_image(self)
        self.web_driver.get(Bing.HOME_URL)

        # 循环爬取
        for key in self.keys:
            key_v =  self.keys[key]
            print('正在爬取【'+key_v+'】相关图片......')
            search_box = self.web_driver.find_element_by_class_name("b_searchbox")
            search_box.send_keys(key_v)
            search_box.submit()

            self.web_driver.find_elements_by_css_selector("[class='mimg']")[0].click()
            time.sleep(2)

            current_url = self.web_driver.current_url
            self.web_driver.get(current_url)

            img = self.web_driver.find_elements_by_css_selector("div.imgContainer > img")[0]
            current_index = 0
            while img is not None:
                img_src = img.get_attribute('src')
                image_format = 'jpg'
                image_name = key + str(current_index) + '.' + image_format
                if Util.download_image(img_src, self.storing_folder, image_name):
                    current_index += 1
                    print('爬取【'+key_v+'】-->第【'+str(current_index)+'】张图片......')
                try:
                    # 自动点击下一页
                    self.web_driver.find_element_by_id('navr').click()
                    time.sleep(2)
                    img = self.web_driver.find_elements_by_css_selector("div.imgContainer > img")[0]
                except NoSuchElementException:
                    print('爬取失败......')

                
