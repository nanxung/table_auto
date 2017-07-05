#coding:utf-8
from selenium import webdriver
import time
import json

class test_ecjtu:
    def __init__(self):
        self.username='admin'
        self.password='admin'
        self.table_url=''
        self.table_data=''
        self.fileUrl=''
        #self.web=webdriver.Chrome('./chromedriver.exe')


    def login(self):
        #self.web=webdriver.Chrome('./chromedriver.exe')
        self.web = webdriver.Chrome()
        self.web.get('http://222.73.157.153:8080/a?login')
        name=self.web.find_element_by_id('username')
        name.send_keys(self.username)
        pw=self.web.find_element_by_id('password')
        pw.send_keys(self.password)
        btn=self.web.find_element_by_id('loginBtn')
        btn.click()
        time.sleep(3)
        #self.web.get('http://222.73.157.153:8080/a/bd/tJcgxx/form?taskId=5fee0de7ea924037a182711043aa3686&isGather=1&approveState=&isTotal=&isFixed=0&tableId=106&ids=&isView=&isApprove=')
        if self.web.title == '教学工作管理系统':
            print('login success')


    def openTableUrl(self,url):
        self.web.get(url)

    def readFile(self,fileUrl):
        datalist=[]
        rw=open(fileUrl,'r')
        for i in rw:
            datalist.append(i.strip('\n'))
        return datalist

    def submitBtn(self):
        self.web.find_element_by_id('btnSubmit').click()


    def to_one(self,name,value):
        flag=self.web.find_element_by_name(name)
        flag.clear()
        flag.send_keys(value)


    def toTable(self):
        datalist=self.readFile(self.fileUrl)
        #print(datalist)

        lall=list()
        for l in datalist:
            ll = list()
            dl=json.loads(str(l))
            for k in dl.keys():
                ll.append((k,dl[k]))

            lall.append(ll)

        return lall





#li1=web.find_element_by_xpath('//*[@id="menu"]/li[2]/a')
#li1.click()
#time.sleep(3)
#l2=web.find_element_by_xpath('//*[@id="menu-700"]/li[2]')
#l2.click()


'''
web=webdriver.Chrome('./chromedriver.exe')
web.get('http://222.73.157.153:8080/a?login')
name=web.find_element_by_id('username')
name.send_keys('admin')
pw=web.find_element_by_id('password')
pw.send_keys('admin')
btn=web.find_element_by_id('loginBtn')
btn.click()
time.sleep(3)
'''

