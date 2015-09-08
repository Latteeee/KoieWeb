from django import forms

class KoieForm(forms.Form):
    koie_name = forms.CharField(label='Koienavn', max_length=20)
    vedstatus = forms.IntegerField(label='Vedstatus')
    skaderapport = forms.CharField(label='Skaderapport',widget=forms.Textarea)

