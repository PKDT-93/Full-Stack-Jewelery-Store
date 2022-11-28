# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Item(models.Model):
    itemid = models.IntegerField(db_column='ItemID', primary_key=True)  # Field name made lowercase.
    barcode = models.IntegerField(db_column='Barcode', unique=True)  # Field name made lowercase.
    weight = models.IntegerField(db_column='Weight')  # Field name made lowercase.
    price = models.IntegerField(db_column='Price')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'item'


class Pendant(models.Model):
    itemid = models.ForeignKey(Item, on_delete = models.CASCADE, db_column='ItemID', related_name = '%(class)s_ItemID')  # Field name made lowercase.
    itembarcode = models.ForeignKey(Item, on_delete = models.CASCADE, db_column='ItemBarcode', related_name = '%(class)s_Barcode')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pendant'


class PendantMateriallist(models.Model):
    itemid = models.ForeignKey(Item, on_delete = models.CASCADE, db_column='ItemID', related_name = '%(class)s_ItemID')  # Field name made lowercase.
    barcode = models.ForeignKey(Item, on_delete = models.CASCADE, db_column='Barcode', related_name = '%(class)s_Barcode')  # Field name made lowercase.
    material = models.CharField(db_column='Material', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pendant_materiallist'