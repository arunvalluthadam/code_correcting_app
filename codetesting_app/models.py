from django.db import models

# Create your models here.
class Questions(models.Model):
	questions = models.TextField(verbose_name=u'Questions')
	function_name = models.CharField(verbose_name=u'Function Name', max_length=200)
	test_function = models.CharField(verbose_name=u'Test Function', max_length=200)
	expected_ans = models.CharField(verbose_name=u'Expected Answer', max_length=200)

	def __unicode__(self):
		return self.questions