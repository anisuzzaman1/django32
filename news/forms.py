from django import forms
from django.forms import fields
from .models import News

class NewsForms(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content']

    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        qs = News.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error("title", f"{title} is already in used")
        return data


class NewsFormsOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    def clean(self):
        banned_data = "office"
        cleaned_data = self.cleaned_data
        print('All data', cleaned_data)
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title.lower().strip() == "the office":
            self.add_error('title', 'This title is taken.')
        if banned_data in content.lower() or banned_data in title.lower():
            self.add_error('content', "Office cannot be in content")
            raise forms.ValidationError("Office a BANNED word which is not allowed")
        return cleaned_data

    """ Old Version
    def clean_title(self):
        cleaned_data = self.cleaned_data # Dictionary
        print(cleaned_data)
        title = cleaned_data.get('title')
        if title.lower().strip() == "the office":
            raise forms.ValidationError('This title is taken')
        print (title)
        return title
    """