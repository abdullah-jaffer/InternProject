from django import forms


class ArticleForm(forms.Form):
    title = forms.CharField(label='title', max_length=300, initial="")
    pub_date = forms.DateField(label='Date Published?', widget=forms.SelectDateWidget)
    category = forms.CharField(label='category', max_length=100)
    cover_image = forms.CharField(label='cover_image', max_length=700)
    content = forms.CharField()
    author = forms.CharField(label='author', max_length=100, required=False)
