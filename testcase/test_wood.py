from poium import Page, PageElement

import pytest
import time
from page.login import Loginpage

class TestWood():

    def test_wood(self,browser):
        
        self.wood_page = Loginpage(browser).login('955112', 'a1234567').woods()
        self.wood_page.my_forest()
        self.wood_page.schoolmate()

        log_time = time.strftime("%Y.%m.%d")
        assert log_time in self.wood_page.get_log()

if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_wood.py"])