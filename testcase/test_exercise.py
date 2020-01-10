from page.login import Loginpage
import pytest

class TestExercise():

    def test_exercise(self,browser):
        self.exercise_page = Loginpage(browser).login('955112', 'a1234567').exercise()
        self.exercise_page.do_exercise()

if __name__ == '__main__':
    pytest.main(["-v", "-s", "test_exercise.py"])