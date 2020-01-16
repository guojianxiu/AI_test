from poium import Page, PageElement, PageElements
import time
import random

class Exreportpage(Page):

    def get_exreport_title(self):
        return self.get_title
