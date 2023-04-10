from .models import ArticleMaster, PassengerNumbers
import django_tables2 as tables

class Products_Table(tables.Table):
    ava = tables.Column(footer="HALLO")
    test = tables.Column(accessor="hehehe")
    Number = tables.Column(accessor="article_nr")
    class Meta:
        model = ArticleMaster
        fields = ['article_desc', 'category_desc', 'class_desc', 'subclass_desc']
