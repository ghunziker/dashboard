from django import forms
from .models import ArticleMaster
from bootstrap_modal_forms.forms import BSModalModelForm

class BookModelForm(BSModalModelForm):
    class Meta:
        model = ArticleMaster
        fields = ['article_nr', 'article_desc', 'UOM']