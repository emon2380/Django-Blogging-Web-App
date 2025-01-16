from django import forms

ARTICLE_STATUS = (
    ("draft", "draft"),
    ("inprogress", "in progress"),
    ("posted", "posted"),
)

class CreateArticleForm(forms.Form):
    tittle = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    word_count = forms.IntegerField()
    status = forms.ChoiceField(choices=ARTICLE_STATUS)
    twitter_post = forms.CharField(required=False, widget=forms.Textarea)