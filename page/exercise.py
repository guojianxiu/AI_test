from poium import Page, PageElement, PageElements
import time
import random

class Exercisepage(Page):
    #选项元素标签是[2]--[6]
    question_loc = PageElement(class_name = 'slick-current')
    question_list_loc = PageElements(class_name = 'slick - slide')
    subit_loc = PageElement(class_name = 'submit_btn')
    #selects_loc = PageElement(xpath='/html/body/div[1]/div/div/div[3]/div[1]/div/div/div/div[' + str(x) + ']/div/div/div[3]/span[1]')
    selects_loc = PageElement(css = '.slick-active .option:nth-child(2) > .num')

    def do_exercise(self):
        self.question_loc.click()
        for x in range(0,10):
            self.selects_loc.click()
            time.sleep(2)
        time.sleep(20)


        '''
        for x in range(1,11):
            #异常
            #y = (random.randint(2, 5))
            selects_loc = PageElement(xpath='/html/body/div[1]/div/div/div[3]/div[1]/div/div/div/div[' + str(x) + ']/div/div/div[3]/span[1]')
            self.selects_loc.click()
            time.sleep(2)

    
    正常
        self.question_loc.click()
        print(self.selects_loc1)
        self.selects_loc1.click()
        time.sleep(2)
        #self.selects_loc2[0].click()
        #time.sleep(12)

'''