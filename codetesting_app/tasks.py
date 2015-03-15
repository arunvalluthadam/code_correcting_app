from __future__ import absolute_import

from codeTesting_project.celery import app
from celery.task import task
import unittest
import code_for_test
from .models import *

@app.task
def add(x, y):
    return x + y

def get_current(question_id=1):
	questions = Questions.objects.get(id=question_id)
	test_func = questions.test_function
	expect_ans = questions.expected_ans

@app.task
class TestCode(unittest.TestCase):
	# def setUp(self):
 #        """
 #        This method is called before each test
 #        """
 #        self.false_int = "A"

 #    def tearDown(self):
 #        """
 #        function with a last process
 #        """
 #        pass

	def testCode(self):
		self.assertEqual(code_for_test.test_func, expect_ans)

	# def testBadInput(self):
	# 	self.assertRaises(code_for_test.TypeError, expect_ans)


if __name__ == "__main__":
	unittest.main()