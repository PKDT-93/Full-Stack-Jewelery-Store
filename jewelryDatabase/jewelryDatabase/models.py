# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bracelet(models.Model):
    itemid = models.OneToOneField('Item', on_delete = models.CASCADE, db_column='ItemID', related_name = '%(class)s_ItemID')  # Field name made lowercase.
    braceletbarcode = models.OneToOneField('Item', on_delete = models.CASCADE, db_column='BraceletBarcode', related_name = '%(class)s_Barcode')  # Field name made lowercase.

    class Meta:
        db_table = 'Bracelet'


class Item(models.Model):
    itemid = models.AutoField(db_column='ItemID', primary_key=True)  # Field name made lowercase.
    barcode = models.IntegerField(db_column='Barcode', unique=True)  # Field name made lowercase.
    weight = models.IntegerField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Item'


class Necklace(models.Model):
    itemid = models.ForeignKey(Item, on_delete = models.CASCADE, db_column='ItemID',related_name = '%(class)s_ItemID')  # Field name made lowercase.
    ringbarcode = models.OneToOneField(Item, on_delete = models.CASCADE, db_column='RingBarcode', related_name = '%(class)s_Barcode')  # Field name made lowercase.

    class Meta:
        db_table = 'Necklace'


class Other(models.Model):
    itemid = models.ForeignKey(Item, on_delete = models.CASCADE, db_column='ItemID', related_name = '%(class)s_ItemID')  # Field name made lowercase.
    otherbarcode = models.OneToOneField(Item, on_delete = models.CASCADE, db_column='OtherBarcode', related_name = '%(class)s_Barcode')  # Field name made lowercase.
    type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Other'


class Pendant(models.Model):
    itemid = models.ForeignKey(Item, on_delete = models.CASCADE, db_column='ItemID',related_name = '%(class)s_ItemID')  # Field name made lowercase.
    pendantbarcode = models.OneToOneField(Item, on_delete = models.CASCADE, db_column='PendantBarcode', related_name = '%(class)s_Barcode')  # Field name made lowercase.

    class Meta:
        db_table = 'Pendant'


class Ring(models.Model):
    itemid = models.ForeignKey(Item, on_delete = models.CASCADE, db_column='ItemID', related_name = '%(class)s_ItemID')  # Field name made lowercase.
    ringbarcode = models.OneToOneField(Item, on_delete = models.CASCADE, db_column='RingBarcode',related_name = '%(class)s_Barcode')  # Field name made lowercase.

    class Meta:
        db_table = 'Ring'


class Watch(models.Model):
    itemid = models.ForeignKey(Item, on_delete = models.CASCADE, db_column='ItemID',related_name = '%(class)s_ItemID')  # Field name made lowercase.
    watchbarcode = models.OneToOneField(Item, on_delete = models.CASCADE, db_column='WatchBarcode', related_name = '%(class)s_Barcode')  # Field name made lowercase.
    watchbrand = models.TextField(db_column='WatchBrand')  # Field name made lowercase.
    batterytype = models.TextField(db_column='BatteryType')  # Field name made lowercase.

    class Meta:
        db_table = 'Watch'
