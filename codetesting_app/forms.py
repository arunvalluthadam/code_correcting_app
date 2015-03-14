from django import forms

class QuestForm(forms.Form):
	your_code = forms.CharField(max_length=300, required=True,widget=forms.Textarea(attrs={'class':"form-control",'placeholder':"User Name",'name':'quest','rows':"20"}), label=u'')
	