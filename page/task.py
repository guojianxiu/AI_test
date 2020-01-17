from poium import Page, PageElement, PageElements

class Taskpage(Page):
    tasks_title = PageElements(class_name = 'grayColor')
    logo_loc = PageElements(class_name='finishIcon')
    cardbtn_loc = PageElement(class_name='cardbtn')

    def do_task(self):
        #完成其他线下任务
        if self.cardbtn_loc:
            self.cardbtn_loc.click()
        for task in self.tasks_title:
            #print(task)
            if task.text != '练习题':
                try:
                    task.click()
                except:
                    return Taskpage(self.driver).do_task()

    def get_len(self):
        if len(self.logo_loc) == 4:
            return Taskpage(self.driver).get_len()
        return len(self.logo_loc)