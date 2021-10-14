from bs4 import BeautifulSoup
import requests
import time
import dateparser
import datetime
from . import models

class Parser():
    def __init__(self,link):
        self.url = link
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.text, "html.parser")
        self.r_name = self.soup.find('img').get('alt')
        print(self.r_name)

        self.tags = models.Resource.objects.get(resource_name=self.r_name)

        self.tag1 = self.tags.top_tag.split(',')
        self.tag2 = self.tags.bottom_tag.split(',')
        self.tag3 = self.tags.title_cut.split(',')
        self.tag4 = self.tags.date_cut.split(',')

        print(self.tag1,self.tag2,self.tag3,self.tag4)


    def main(self):
        bottom = self.soup.find_all(self.tag1[0],attrs={self.tag1[2]:self.tag1[3]})

        to_return = []
        new = []
        for i in bottom:
            artc = i.find(self.tag1[1])
            if artc :
                link = artc.get('href')
                if '.' in link:
                    new.append(link)
                else:
                    new_link = self.url.split('/')
                    new.append(f'{"/".join(new_link[:3])+link}')
        
        for j in new:
            url_j = j
            page_j = requests.get(url_j)
            soup_j = BeautifulSoup(page_j.text, "html.parser")
            for_p = soup_j.find_all(self.tag2[0],attrs={self.tag2[2]:self.tag2[3]})
            allP = for_p[0].find_all(self.tag2[1],attrs={self.tag2[2]:self.tag2[4]})
            art = ''

            title = soup_j.find(self.tag3[0],attrs={self.tag3[1]:self.tag3[2]}).getText().replace(u'\n',' ').replace(u'\t', '')
            # print(title)

            for every in allP:
                art += every.getText().replace(u'\xa0',' ').replace(u'\u2009', '')
                
            time1 = dateparser.parse(soup_j.find(self.tag4[0]).get(self.tag4[1]))

            to_create = {
                'res_id':self.tags,
                'link':url_j,
                'title':title,
                'content':art,
                'nd_date':int(time.mktime(time1.timetuple())),
                's_date':int(time.mktime(datetime.datetime.now().timetuple())),
                'not_date':time1
                }

            to_return.append(to_create)
            models.Item.objects.create(**to_create)
        return to_return

