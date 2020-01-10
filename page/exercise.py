from poium import Page, PageElement, PageElements
from random import randrange
import time

class Exercisepage(Page):
    #选项元素标签是[2]--[6]
    question_loc = PageElement(class_name = 'slick-current')
    question_list_loc = PageElements(class_name = 'slick - slide')
    selects_loc = PageElements(class_name = 'option')
    subit_loc = PageElement(class_name = 'submit_btn')

    def do_exercise(self):
        for i in range(0,len(self.question_list_loc)):
            select_index = randrange(0, len(self.selects_loc))
            self.selects_loc[select_index].click()
            time.sleep(2)
        self.subit_loc.click()



    def get_exercise_report(self):
        pass
