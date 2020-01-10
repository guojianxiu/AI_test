import pytest
from page.login import Loginpage

class Testcards():

    def test_cards(self,browser):
        self.card_page = Loginpage(browser).login('955112', 'a1234567').card()



if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_cards.py"])