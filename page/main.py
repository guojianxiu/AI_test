'''
@Time    : 2019/12/26 11:45
@Author  : fzj
@Desc    : 学生端主页面
'''
from poium import Page, PageElement,PageElements
from page.xiaole import Xiaolepage
from page.wood import Woodpage
from page.exercise import Exercisepage
from page.task import Taskpage


class Mainpage(Page):
    xiaole_loc = PageElement(class_name='enterxiaole')
    wood_loc = PageElement(class_name='wood')
    tasks_loc = PageElements(class_name = 'title')

    def task(self):
        #任务
        return Taskpage(self.driver)

    def exercise(self):
        for task in self.tasks_loc:
            if task.text == "练习题":
                task.click()
                return Exercisepage(self.driver)

    def hi_xiaole(self):
        #小乐同学
        self.xiaole_loc.click()
        return Xiaolepage(self.driver)

    def woods(self):
        #学习森林
        self.wood_loc.click()
        return Woodpage(self.driver)

    def card(self):
        pass
