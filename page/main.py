'''
@Time    : 2019/12/26 11:45
@Author  : fzj
@Desc    : 学生端主页面
'''
from poium import Page, PageElement,PageElements
from page.xiaole import Xiaolepage
from page.wood import Woodpage
from page.task import Taskpage
from page.cards import Cardspage
from page.exercise import Exercisepage
from page.exreport import Exreportpage
import time


class Mainpage(Page):
    xiaole_loc = PageElement(class_name='enterxiaole')
    wood_loc = PageElement(class_name='wood')
    tasks_loc = PageElements(class_name = 'title')
    #章节弹框
    container_loc = PageElement(class_name = 'container')
    choice_loc = PageElement(class_name = 'am-list-extra')
    subchoice_loc = PageElement(class_name = 'am-picker-popup-header-right')
    click_btn = PageElement(class_name = 'click_btn')

    def task(self):
        return Taskpage(self.driver)

    def exercise(self):
        if self.container_loc:
            self.choice_loc.click()
            time.sleep(2)
            self.subchoice_loc.click()
            time.sleep(2)
            self.click_btn.click()
        for task in self.tasks_loc:
            if task.text == "练习题":
                task.click()
                return Exercisepage(self.driver)

    def exreport(self):
        for task in self.tasks_loc:
            if task.text == "练习题":
                task.click()
                return Exreportpage(self.driver)

    def hi_xiaole(self):
        #小乐同学
        self.xiaole_loc.click()
        return Xiaolepage(self.driver)

    def woods(self):
        #学习森林
        self.wood_loc.click()
        return Woodpage(self.driver)

    def card(self):
        self.get("http://webapp.leke.cn/leke-ai-pad/#/card")
        return Cardspage(self.driver)

