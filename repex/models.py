from django.db import models

# Create your models here.
class ArticleMaster(models.Model):
    location_id = models.IntegerField()
    article_nr = models.IntegerField()
    article_desc = models.CharField(max_length=255)
    item_status = models.CharField(max_length=255)
    UOM = models.CharField(max_length=255)
    category_id = models.IntegerField(null=True)
    category_desc = models.CharField(max_length=255, null=True)
    class_id = models.IntegerField(null=True)
    class_desc = models.CharField(max_length=255, null=True)
    subclass_id = models.IntegerField(null=True)
    subclass_desc = models.CharField(max_length=255, null=True)
    brand_id = models.IntegerField(null=True)
    brand_desc = models.CharField(max_length=255, null=True)
    unitcost = models.FloatField(null=True)
    supplier_id = models.IntegerField(null=True)
    supplier_desc = models.CharField(max_length=255, null=True)
    leadtime = models.FloatField(null=True)
    minstock = models.IntegerField(null=True)
    lotsize = models.IntegerField(null=True)
    actualstock = models.IntegerField(null=True)
    undefined = models.CharField(max_length=255, null=True)
    minorder_qty = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.article_nr}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['article_nr', 'location_id'], name='unique_articlenr_locationid_combination'
            )
        ]

class Inbound(models.Model):
    article_nr = models.IntegerField()
    date = models.DateTimeField()
    value = models.FloatField()

class PassengerNumbers(models.Model):
    date = models.DateField(unique=True)
    location_id = models.IntegerField()
    passengers = models.IntegerField()

    def __str__(self):
        return f"{self.date, self.passengers, self.location_id}"

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['date', 'location_id'], name='unique_date_locationid_combination'
            )
        ]