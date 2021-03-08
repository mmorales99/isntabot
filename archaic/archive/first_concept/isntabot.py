#!/usr/bin/env python3
from time import sleep
from selenium import webdriver
from random import randint
import unicodedata
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import os

def remove_non_acepted_characters(string):
    nfkd_form = unicodedata.normalize('NFKD', string)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

class identitats:
    nombres=["Lucía", "Juan", "Carmelo", "Carmina", "Eva", "María", "Melisa", "José", "Miguel", "Carlos", "Ramon", "Ines", "Hugo", "Víctor", "Nicolás", "Adriana", "Emma", "Mario", "Mariano"]
    apellidos=["Almenabar", "Vicens", "Ferrán", "Hernández","Sánchez", "González", "Martín","Pavia", "Massanet", "Espín", "Muñoz", "Rajoy", "Amat", "Puig"]
    apellidos2=["Martínez", "Galví", "Ferrándiz", "Morales", "Castejón", "Del Toro", "Martinez", "Bellver", "Crespo", "Maciá", "Pomares", "Brey", "Marrón"]

    n = -1
    a = -1
    a1 = -1
    
    def get_rand_name(self):
        self.n = randint(0, len(self.nombres)-1)
        self.a = randint(0, len(self.apellidos)-1)
        self.a1 =randint(0, len(self.apellidos2)-1)
        return self.nombres[self.n] + " " + self.apellidos[self.a] + " " +self.apellidos2[self.a1]

    def get_rand_Uname(self, id):
        name = self.nombres[self.n]
        ap = self.apellidos[self.a]
        ap1 = self.apellidos2[self.a1]
        username = name[0:randint(1,len(name)-1)] + ap[0:randint(1,len(ap)-1)] + ap1[0:randint(1,len(ap1)-1)] + str(id)
        return remove_non_acepted_characters(username)


class pyBot:
    email = ""
    username = ""
    pword = ""
    id = 0
    toFollow = []

    def create(self, email, id, toFollow=[], path=""):
        self.toFollow = toFollow
        self._goto_register(email, id)
        self.save_bot(path)
        self._do_things(toFollow)

    def __init__(self):
        self.webService = Service('./chromeDriver/chromedriver')
        self.webService.start()

    def activate(self, path=""):
        if(path==""):
            print("NotLoadableBot")
        else:
            self.load_bot(path)
            self._do_things(self.toFollow)

    def save_bot(self, path=""):
        if(path==""):
            path = "./"
        botpath = path+str(self.id)+".bot"
        f = open(botpath, "w+")
        f.write(self.id+"\n")
        f.write(self.email+"\n")
        f.write(self.username+"\n")
        f.write(self.pword+"\n")
        for x in self.toFollow:
            f.write(x+"\n")
    def load_bot(self, path=""):
        if(path==""):
            print("NotLoadableBot")
            return
        if(os.path.isfile(path)):
            f = open(path, "r")
            if(f.mode=="r"):
                loaded = f.readlines()
                f.close()
                l = iter(loaded)
                self.id = next(l)
                self.email = next(l)
                self.username = next(l)
                self.pword = next(l)
                for x in l:
                    self.toFollow.append(x)
        else:
            print("NotLoadableBot")

    def getUname(self):
        return self.username
    def getPword(self):
        return self.pword
    def getEmail(self):
        return self.email
    def getId(self):
        return self.id
    def getToFollow(self):
        return self.toFollow
    
    def _do_things(self, toFollow=[]):
        self._inicia_sesion()
        self._follow_marked(toFollow)
        self._unfollow_no_followers()
        self.browser.quit()
    
    def _follow_marked(self, toFollow=[]):
        if(len(toFollow)==0):
            return
        for x in toFollow:
            cuadro_busqueda = self.browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]")
            cuadro_busqueda.send_keys(x)
            sleep(1)
            self.browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a").click()
            self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/span/span[1]/button").click()
        self.browser.get("https://www.instagram.com")
        
    
    def _unfollow_no_followers(self):
        self._goto_profile()
        followers = self._get_followers()
        following = self._get_following()
        #acabar
	
    def _get_followers(self):
        try:
            followers = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/ul/li[2]")
            followers.click()
        except:
            followers = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
            followers.click()

        return followers

    def _get_following(self):
        try:
            following = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/ul/li[3]")
            following.click()
        except:
            following = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")
            following.click()
            
        return following

    def _goto_profile(self):
        try:
            profile_link = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a")
            profile_link.click()
        except:
            self.browser.maximize_window()
            try:
                profile_link = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a")
                profile_link.click()
            except:
                profile_link = self.browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img")
                profile_link.click()
                profile_link = self.browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div/div[2]/div[2]/a[1]/div/div[2]/div/div/div/div")
                profile_link.click()
        sleep(1)
    def _goto_register(self, email="<YOUR BOT EMAIL>", id="0"):
        self.browser=webdriver.Remote(self.webService.service_url)
        self.browser.implicitly_wait(5)
        self.browser.get('https://www.instagram.com/accounts/emailsignup/')
        sleep(2)
        identitat = identitats()
        nombre = identitat.get_rand_name()
        uname = identitat.get_rand_Uname(id)
        pword = "<YOUR BOT PASSWORD>;"
        arroba = 0
        for x in email:
            if(x=='@'):
                break
            arroba = arroba +1
        conter = email[0:arroba]
        domini = email[arroba:len(email)]
        bot_email = conter +"+"+str(id)+domini
        self.email = bot_email
        self.username = uname
        self.pword = pword
        self.id=id
        sleep(1)
        try:
            self.browser.find_element_by_xpath("/html/body/div[1]/section/div[1]/button").click()
        except:
            pass
        email_input=self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input")
        name_input=self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[4]/div/label/input")
        username_input=self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[5]/div/label/input")
        #                                                  /html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input
        pword_input=self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[6]/div/label/input")
        email_input.send_keys(bot_email)
        name_input.send_keys(nombre)
        username_input.send_keys(uname)
        pword_input.send_keys(pword)
        registre_succeded = False
        while registre_succeded is False:
            try:
                self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[7]/div/button").click()
                registre_succeded = True
            except:
                self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/form/div[5]/div/div/div/button").click()
        sleep(1)
        select_month = Select(self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[1]/select"))
        select_month.select_by_visible_text("agosto")
        select_day = Select(self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[2]/select"))
        select_day.select_by_visible_text("13")
        select_year = Select(self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/div[4]/div/div/span/span[3]/select"))
        select_year.select_by_visible_text("1989")
        self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div/div[6]/button").click()
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
        sleep(15)
        self.browser.get("https://mail.google.com/mail/u/0/#inbox")
        try:
            self.browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys("<YOUR BOT EMAIL>")
            self.browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]").click()
            self.browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input").send_keys("<YOUR BOT PASSWORD>")
            self.browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]").click()
            sleep(2)
        except:
            pass
        self.browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button").click()
        verify_code = self.browser.find_element_by_xpath("//*[@id=\"m_1063509810926715789email_content\"]/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]").text
        self.browser.find_element_by_xpath("/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[1]/div[3]/div[1]/div/div[2]/div[3]").click()
        self.browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'W')
        verify_input = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div[2]/form/div/div[1]/input")
        verify_input.sendKeys(verify_code)
        self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/article/div/div[1]/div[2]/form/div/div[2]/button").click()
        sleep(5)
        self.browser.quit()

    def _inicia_sesion(self):
        self.browser=webdriver.Remote(self.webService.service_url)
        self.browser.implicitly_wait(5)
        self.browser.get('https://www.instagram.com/')
        sleep(2)
 
        self.username_input = self.browser.find_element_by_css_selector("input[name='username']")
        self.password_input = self.browser.find_element_by_css_selector("input[name='password']")
        self.username_input.send_keys(self.username)
        self.password_input.send_keys(self.pword) ## eliminate this, replace with automated pw
        self.login_link = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")
        self.login_link.click()
        try:
            self.keep_logon = self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
            self.keep_logon.click()
        except:
            print("ok")
        self.show_notifications = self.browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
        self.show_notifications.click()
