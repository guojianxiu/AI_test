from poium import Page, PageElement

import pytest
import datetime
from page.login import Loginpage

class TestWood():

    def test_wood(self,browser):
        self.wood_page = Loginpage(browser).login('955112', 'a1234567').wood()
        self.wood_page.my_forest()
        self.wood_page.schoolmate()
        checkoutDate = datetime.datetime.today().date() - datetime.timedelta(days=1)
        log_time = checkoutDate.strftime("%Y.%m.%d")
        assert log_time in self.wood_page.get_log()


if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_wood.py"])