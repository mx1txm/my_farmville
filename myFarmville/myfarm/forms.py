from django import forms
from .models import Post

class FilterForm(forms.ModelForm):
    post = forms.CharField()

    class Meta:
        model = Post
        fields = ('post',)


 #  field1 = forms.ChoiceField(required=True, widget=forms.RadioSelect(
  #  attrs={'class': 'Radio'}), choices=(('apple','Apple'),('mango','Mango'),))