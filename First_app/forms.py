from django import forms
from django.core import validators 
from First_app import models



class user_form(forms.Form):
    user_name=forms.CharField(validators=[validators.MaxLengthValidator(20)],label="Full name",widget=forms.TextInput(attrs={'placeholder':'Enter your full name','style':'width:300px'}))
    user_dob=forms.DateField(label="Date of Birth",widget=forms.TextInput(attrs={'type':'date'}))

    user_email=forms.EmailField()
    user_vemail=forms.EmailField()
    number_field=forms.IntegerField()
    choose=(('A','A'),('B','B'),('C','C'))
    boolean_field=forms.BooleanField()
    dropdown_Menu=forms.ChoiceField(choices=choose)
    radio_button=forms.ChoiceField(choices=choose, widget=forms.RadioSelect)

  # select multiple value in checkbox,radio button and dropdown_Menu

    dropdown_Menu_multiple=forms.MultipleChoiceField(choices=choose)
    checkbox_multiple=forms.MultipleChoiceField(choices=choose, widget=forms.CheckboxSelectMultiple)

    def clean(self):
        all_data=super().clean()
        email=all_data['user_email']
        vemail=all_data['user_vemail']

        if email!=vemail:
            raise forms.ValidationError("Email don't match")





class MusicianForm(forms.ModelForm):
    class Meta:
        model=models.Musician
        fields="__all__"


class AlbumForm(forms.ModelForm):
    release_date=forms.DateField(label="Date of release",widget=forms.TextInput(attrs={'type':'date'}))
    class Meta:
        model=models.Album
        fields="__all__"
