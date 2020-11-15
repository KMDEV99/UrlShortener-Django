from django import forms
from django.core.validators import URLValidator

def validate_url(value):
	url_validator = URLValidator()
	try:
		url_validator(value)
	except:
		raise forms.ValidationError("Invalid URL")
	return value

class SubmitUrlForm(forms.Form):
	url = forms.CharField(label='Submit URL', validators=[validate_url])
