'''
@Time    : 2020/1/16 17:34
@Author  : fzj
@Desc    : 提建议测试用例
'''

from page.login import Loginpage
import pytest

class TestXaiole_sg():
    def test_xiaole_sg(self,browser):
        '''提建议'''
        self.xiaole_page = Loginpage(browser).login('955112', 'a1234567').hi_xiaole()
        self.xiaole_page.suggest('123')
        assert '小乐收到你的建议啦' in self.xiaole_page.get_request()

if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_xiaole_sg.py"])