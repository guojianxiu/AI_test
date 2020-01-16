from page.login import Loginpage
import pytest
from poium import Page

class TestExReport():

    def test_exreport(self,browser):
        self.exreport_page = Loginpage(browser).login('955112', 'a1234567').exreport()
        assert '习题报告' in self.exreport_page.get_exreport_title()

if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_exreport.py"])