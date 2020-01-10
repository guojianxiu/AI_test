from poium import Page, PageElement, PageElements

class Taskpage(Page):
    tasks_title = PageElements(class_name = 'grayColor')
    logo_loc = PageElement(class_name='finishIcon')

    def do_task(self):
        #完成其他线下任务
        for task in self.tasks_title:
            #print(task)
            if task.text != '练习题':
                task.click()

    def isElementExist(self):
        try:
            self.driver.find_element_by_css_selector(self.logo_loc)
            return True
        except:
            #如果已完成角标不存在，重新获取页面元素
            return Taskpage(self.driver)