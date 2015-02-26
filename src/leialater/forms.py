from django import forms
from django.contrib.auth.models import User

from leialater import models
from leialater.models import Bookmark, Category


#===============================================================================
# from leialater.models import UserProfileLeia
#===============================================================================
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        

class BookmarkForm(forms.ModelForm):
    #===========================================================================
    # category = forms.CharField(max_length=128, help_text="Please enter the category name")
    #===========================================================================
    title = forms.CharField(max_length=128, help_text="Please enter the title")
    url = forms.URLField(max_length=200, help_text="Please enter the url of your link")
    summary = forms.CharField(max_length=500, help_text="Please enter a summary of your link")
    class Meta:
        model = Bookmark
        fields = ('title', 'url', 'summary')
        
#===============================================================================
# class CategoryForm(forms.ModelForm):
#     cat_name = forms.CharField(max_length=128, help_text="Please enter the name of your category")
#     class Meta:
#         model = Category        
#         fields = (cat_name)
#===============================================================================
        
    