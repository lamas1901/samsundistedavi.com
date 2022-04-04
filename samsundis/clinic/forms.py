from django import forms

class AppointmentForm(forms.Form):
	attrs = {'class':'form-control'}

	name = forms.CharField(max_length=25,widget=forms.TextInput(attrs=attrs))
	mail = forms.EmailField(widget=forms.EmailInput(attrs=attrs))
	phone = forms.DecimalField(widget=forms.TextInput(attrs=attrs))
	message = forms.CharField(widget=forms.TextInput(attrs=attrs))