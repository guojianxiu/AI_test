import pytest
from page.login import Loginpage

class TestTask():

    def test_task(self,browser):
        self.task_page = Loginpage(browser).login('955112', 'a1234567').task()
        self.task_page.do_task()
        #断言已完成角标存在
        assert self.task_page.isElementExist()

if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_task.py"])
