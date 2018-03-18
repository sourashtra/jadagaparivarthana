from django import forms
from matrimony.models import MatrimonyApplication

CHOICES = (
    (0, 'Zero'),
    (1, 'One'),
    (2, 'Two'),
)


class MatrimonyApplicationForm(forms.ModelForm):
    class Meta:
        model = MatrimonyApplication

    def save(self, commit=True):
        print "here"

    # Name = forms.CharField()
    # Place = forms.CharField()
    # Origin = forms.CharField()
    # Gothram = forms.CharField()
    # Family_Name = forms.CharField()
    # Natchathram = forms.CharField()
    # Padam = forms.CharField()
    # Rasi = forms.CharField()
    # Height = forms.CharField()
    # Color = forms.CharField()
    # Blood_Group = forms.CharField()
    # #
    # SomeChoice = forms.ChoiceField(choices=CHOICES)
    # Employment_details = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    # Marital_Status = forms.MultipleChoiceField(choices=CHOICES)
    # Marital_Status = forms.MultipleChoiceField(choices=CHOICES, widget=forms.CheckboxSelectMultiple)
    # photo = forms.FileField()
    # password_field = forms.CharField(widget=forms.PasswordInput)
    # textarea = forms.CharField(widget=forms.Textarea)
    # boolean_field = forms.BooleanField()
