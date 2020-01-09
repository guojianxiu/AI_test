from poium import Page, PageElement

class Woodpage(Page):
    view_class = PageElement(class_name = 'top')   #参观别人的森林
    back = PageElement(class_name = 'bottom')      #返回我的森林、返回学习计划
    tab_control = PageElement(class_name = 'item')  #周、月tab切换开关
    before = PageElement(xpath='//*[@id="root"]/div/div/div[1]/div[1]/div[2]/span[1]')
    next = PageElement(xpath = '//*[@id="root"]/div/div/div[1]/div[1]/div[2]/span[3]')
    log_msg = PageElement(xpath = '//*[@id="root"]/div/div/div[2]/div[2]/div[1]/span[1]')

    def my_forest(self):
        self.before.click()
        self.next.click()
        self.tab_control.click()

    def get_log(self):
        #验证昨日得成长动态
        return str(self.log_msg.text)

    def schoolmate(self):
        self.view_class.click()
        self.back.click()





