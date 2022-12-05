# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Contain(models.Model):
    itemid = models.ForeignKey('Item', on_delete = models.CASCADE, db_column='ItemID', related_name = '%(class)s_ItemID')  # Field name made lowercase.
    itembarcode = models.ForeignKey('Item', on_delete = models.CASCADE, db_column='ItemBarcode', related_name = '%(class)s_Barcode')  # Field name made lowercase.
    certificateno = models.ForeignKey('Gems', on_delete = models.CASCADE, db_column='CertificateNo', blank=True, null=True, related_name = '%(class)s_CertificateNo')  # Field name made lowercase.
    batchno = models.ForeignKey('Metals', on_delete = models.CASCADE, db_column='BatchNo', blank=True, null=True, related_name = '%(class)s_BatchNo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Contain'


class Employee(models.Model):
    storeid = models.ForeignKey('Store', on_delete = models.CASCADE, db_column='StoreID', related_name = '%(class)s_StoreID')  # Field name made lowercase.
    personid = models.OneToOneField('Person', on_delete = models.CASCADE, db_column='PersonID', related_name = '%(class)s_PersonID')  # Field name made lowercase.
    essn = models.AutoField(db_column='ESSN', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Employee'


class EmployeeManages(models.Model):
    managerid = models.ForeignKey('Person', on_delete = models.CASCADE, db_column='ManagerID', related_name = '%(class)s_ManagerID')  # Field name made lowercase.
    managerssn = models.ForeignKey('Manager', on_delete = models.CASCADE, db_column='ManagerSSN', related_name = '%(class)s_ManagerSSN')  # Field name made lowercase.
    employeeid = models.ForeignKey(Employee, on_delete = models.CASCADE, db_column='EmployeeID', related_name = '%(class)s_PersonID')  # Field name made lowercase.
    employeessn = models.ForeignKey(Employee, on_delete = models.CASCADE, db_column='EmployeeSSN', related_name = '%(class)s_EmployeeSSN')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Employee_Manages'


class Gems(models.Model):
    certificateno = models.AutoField(db_column='CertificateNo', primary_key=True)  # Field name made lowercase.
    gemtype = models.TextField(db_column='GemType')  # Field name made lowercase.
    carat = models.IntegerField(db_column='Carat')  # Field name made lowercase.
    cut = models.IntegerField(db_column='Cut', blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Gems'


class Item(models.Model):
    itemid = models.AutoField(db_column='ItemID', primary_key=True)  # Field name made lowercase.
    barcode = models.IntegerField(db_column='Barcode', unique=True)  # Field name made lowercase.
    weight = models.IntegerField(db_column='Weight', blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='Price', blank=True, null=True)  # Field name made lowercase.
    type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.itemid + ' ' + self.barcode + ' ' + self.weight + ' ' + self.price + ' ' + self.type

    class Meta:
        managed = False
        db_table = 'Item'


class Manager(models.Model):
    mssn = models.AutoField(db_column='MSSN', primary_key=True)  # Field name made lowercase.
    creditcard = models.IntegerField(db_column='CreditCard')  # Field name made lowercase.
    personid = models.OneToOneField('Person', on_delete = models.CASCADE, db_column='PersonID', related_name = '%(class)s_PersonID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Manager'


class Materiallist(models.Model):
    itemid = models.ForeignKey(Item, on_delete = models.CASCADE, db_column='ItemID', related_name = '%(class)s_ItemID')  # Field name made lowercase.
    barcode = models.ForeignKey(Item, on_delete = models.CASCADE, db_column='Barcode', related_name = '%(class)s_Barcode')  # Field name made lowercase.
    material = models.IntegerField(db_column='Material', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MaterialList'


class Metals(models.Model):
    batchno = models.AutoField(db_column='BatchNo', primary_key=True)  # Field name made lowercase.
    metaltype = models.TextField(db_column='MetalType')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    karat = models.IntegerField(db_column='Karat', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Metals'


class Other(models.Model):
    itemid = models.ForeignKey(Item, on_delete = models.CASCADE, db_column='ItemID', related_name = '%(class)s_ItemID')  # Field name made lowercase.
    otherbarcode = models.OneToOneField(Item, on_delete = models.CASCADE, db_column='OtherBarcode', related_name = '%(class)s_Barcode')  # Field name made lowercase.
    type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Other'


class Person(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    firstname = models.TextField(db_column='FirstName')  # Field name made lowercase.
    lastname = models.TextField(db_column='LastName')  # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.
    customer = models.IntegerField(db_column='Customer', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Person'


class Personaddress(models.Model):
    personid = models.ForeignKey(Person, on_delete = models.CASCADE, db_column='PersonID', related_name = '%(class)s_PersonID')  # Field name made lowercase.
    addressno = models.IntegerField(db_column='AddressNo')  # Field name made lowercase.
    addresscity = models.TextField(db_column='AddressCity')  # Field name made lowercase.
    addressprovince = models.TextField(db_column='AddressProvince')  # Field name made lowercase.
    addresspostalcode = models.TextField(db_column='AddressPostalCode')  # Field name made lowercase.
    addressstreet = models.TextField(db_column='AddressStreet')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PersonAddress'


class Purchase(models.Model):
    recieptid = models.AutoField(db_column='RecieptID', primary_key=True)  # Field name made lowercase.
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    paymenttender = models.TextField(db_column='PaymentTender')  # Field name made lowercase.
    warranty = models.IntegerField(db_column='Warranty', blank=True, null=True)  # Field name made lowercase.
    paymentdate = models.TextField(db_column='PaymentDate')  # Field name made lowercase.
    timeofpay = models.TextField(db_column='TimeOfPay')  # Field name made lowercase.
    storeid = models.ForeignKey('Store', on_delete = models.CASCADE, db_column='StoreID', related_name = '%(class)s_StoreID')  # Field name made lowercase.
    personid = models.ForeignKey(Person, on_delete = models.CASCADE, db_column='PersonID', related_name = '%(class)s_PersonID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Purchase'


class Purchaseitem(models.Model):
    customerid = models.ForeignKey(Person, on_delete = models.CASCADE, db_column='CustomerID', related_name = '%(class)s_PersonID')  # Field name made lowercase.
    recieptid = models.ForeignKey(Purchase, on_delete = models.CASCADE, db_column='RecieptID',related_name = '%(class)s_RecieptID')  # Field name made lowercase.
    itemid = models.ForeignKey(Item, on_delete = models.CASCADE, db_column='ItemID', related_name = '%(class)s_ItemID')  # Field name made lowercase.
    itembarcode = models.ForeignKey(Item, on_delete = models.CASCADE, db_column='ItemBarcode', related_name = '%(class)s_Barcode')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PurchaseItem'


class Purchaseservice(models.Model):
    customerid = models.ForeignKey(Person, on_delete = models.CASCADE, db_column='CustomerID', related_name = '%(class)s_PersonID')  # Field name made lowercase.
    recieptid = models.ForeignKey(Purchase, on_delete = models.CASCADE, db_column='RecieptID',related_name = '%(class)s_RecieptID')  # Field name made lowercase.
    serviceid = models.ForeignKey('Service', on_delete = models.CASCADE, db_column='ServiceID', related_name = '%(class)s_ServiceID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PurchaseService'


class Service(models.Model):
    serviceid = models.AutoField(db_column='ServiceID', primary_key=True)  # Field name made lowercase.
    servicetype = models.TextField(db_column='ServiceType')  # Field name made lowercase.
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    servicedescription = models.TextField(db_column='ServiceDescription', blank=True, null=True)  # Field name made lowercase.
    startdate = models.TextField(db_column='StartDate')  # Field name made lowercase.
    enddate = models.TextField(db_column='EndDate')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Service'


class Soldat(models.Model):
    storeid = models.ForeignKey('Store', on_delete = models.CASCADE, db_column='StoreID',related_name = '%(class)s_StoreID')  # Field name made lowercase.
    itemid = models.ForeignKey(Item, on_delete = models.CASCADE, db_column='ItemID', related_name = '%(class)s_ItemID')  # Field name made lowercase.
    itembarcode = models.ForeignKey(Item, on_delete = models.CASCADE, db_column='ItemBarcode',related_name = '%(class)s_Barcode')  # Field name made lowercase.
    stock = models.IntegerField(db_column='Stock')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SoldAt'


class Store(models.Model):
    storeid = models.AutoField(db_column='StoreID', primary_key=True)  # Field name made lowercase.
    addressno = models.IntegerField(db_column='AddressNo', blank=True, null=True)  # Field name made lowercase.
    addresscity = models.TextField(db_column='AddressCity')  # Field name made lowercase.
    addressprovince = models.TextField(db_column='AddressProvince')  # Field name made lowercase.
    addresspostalcode = models.TextField(db_column='AddressPostalCode')  # Field name made lowercase.
    addressstreet = models.TextField(db_column='AddressStreet')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Store'


class Storemanages(models.Model):
    managerid = models.ForeignKey(Manager, on_delete = models.CASCADE, db_column='ManagerID', related_name = '%(class)s_PersonID')  # Field name made lowercase.
    managerssn = models.ForeignKey(Manager, on_delete = models.CASCADE, db_column='ManagerSSN', related_name = '%(class)s_ManagerSSN')  # Field name made lowercase.
    storeid = models.ForeignKey(Store, on_delete = models.CASCADE, db_column='StoreID', related_name = '%(class)s_StoreID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StoreManages'


class Storephone(models.Model):
    storeid = models.ForeignKey(Store, on_delete = models.CASCADE, db_column='StoreID',related_name = '%(class)s_StoreID')  # Field name made lowercase.
    phoneno = models.IntegerField(db_column='PhoneNo')  # Field name made lowercase.
    areacode = models.IntegerField(db_column='AreaCode')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StorePhone'


class Storeprovides(models.Model):
    storeid = models.ForeignKey(Store, on_delete = models.CASCADE, db_column='StoreID', related_name = '%(class)s_StoreID')  # Field name made lowercase.
    serviceid = models.ForeignKey(Service, on_delete = models.CASCADE, db_column='ServiceID', related_name = '%(class)s_ServiceID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'StoreProvides'


class Supplier(models.Model):
    supplierid = models.AutoField(db_column='SupplierID', primary_key=True)  # Field name made lowercase.
    suppliername = models.TextField(db_column='SupplierName')  # Field name made lowercase.
    supplieremail = models.TextField(db_column='SupplierEmail')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Supplier'


class Supplierphone(models.Model):
    supplierid = models.IntegerField(db_column='SupplierID')  # Field name made lowercase.
    phoneno = models.IntegerField(db_column='PhoneNo')  # Field name made lowercase.
    areacode = models.IntegerField(db_column='AreaCode')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SupplierPhone'


class Supplies(models.Model):
    supplierid = models.ForeignKey(Supplier, on_delete = models.CASCADE, db_column='SupplierID', related_name = '%(class)s_SupplierID')  # Field name made lowercase.
    certificateno = models.ForeignKey(Gems, on_delete = models.CASCADE, db_column='CertificateNo', related_name = '%(class)s_CertificateNo')  # Field name made lowercase.
    batchno = models.ForeignKey(Metals, on_delete = models.CASCADE, db_column='BatchNo', blank=True, null=True, related_name = '%(class)s_BatchNo')  # Field name made lowercase.
    otherid = models.ForeignKey(Other, on_delete = models.CASCADE, db_column='OtherID', blank=True, null=True, related_name = '%(class)s_OtherID')  # Field name made lowercase.
    otherbarcode = models.ForeignKey(Other, on_delete = models.CASCADE, db_column='OtherBarcode', blank=True, null=True,related_name = '%(class)s_OtherBarcode')  # Field name made lowercase.
    watchid = models.ForeignKey('Watch', on_delete = models.CASCADE, db_column='WatchID', blank=True, null=True, related_name = '%(class)s_WatchID')  # Field name made lowercase.
    watchbarcode = models.ForeignKey('Watch', on_delete = models.CASCADE, db_column='WatchBarcode', blank=True, null=True,related_name = '%(class)s_WatchBarcode')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Supplies'


class Watch(models.Model):
    itemid = models.ForeignKey(Item, on_delete = models.CASCADE, db_column='ItemID', related_name = '%(class)s_ItemID')  # Field name made lowercase.
    watchbarcode = models.OneToOneField(Item, on_delete = models.CASCADE, db_column='WatchBarcode', related_name = '%(class)s_ItemBarcode')  # Field name made lowercase.
    watchbrand = models.TextField(db_column='WatchBrand')  # Field name made lowercase.
    batterytype = models.TextField(db_column='BatteryType')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Watch'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, on_delete = models.CASCADE)
    permission = models.ForeignKey('AuthPermission', on_delete = models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', on_delete = models.CASCADE)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    # def __str__(self):
    #     return self.username + ' ' + self.last_name + ' ' + self.email + self.is_superuser 

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, on_delete = models.CASCADE)
    group = models.ForeignKey(AuthGroup, on_delete = models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, on_delete = models.CASCADE)
    permission = models.ForeignKey(AuthPermission, on_delete = models.CASCADE)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', on_delete = models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(AuthUser, on_delete = models.CASCADE)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
