# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Automahnung(models.Model):
    orderid = models.IntegerField(db_column="OrderID", primary_key=True)
    mahnung1verschickt = models.DateTimeField(
        db_column="Mahnung1verschickt", blank=True, null=True
    )
    mahnung2verschickt = models.DateTimeField(
        db_column="Mahnung2verschickt", blank=True, null=True
    )
    mahnung3verschickt = models.DateTimeField(
        db_column="Mahnung3verschickt", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "AutoMahnung"


class CompanyTypes(models.Model):
    companytypeid = models.AutoField(db_column="CompanyTypeID", primary_key=True)
    companytype = models.CharField(db_column="CompanyType", max_length=50)

    class Meta:
        managed = False
        db_table = "Company Types"

    def __str__(self) -> str:
        return self.companytype

    def __repr__(self) -> str:
        return self.companytype


class Customers(models.Model):
    customerid = models.AutoField(db_column="CustomerID", primary_key=True)
    employee = models.ForeignKey(
        "Employees", on_delete=models.DO_NOTHING, db_column="EmployeeID"
    )
    date = models.DateTimeField(db_column="Date")
    companytype = models.ForeignKey(
        "CompanyTypes",
        on_delete=models.DO_NOTHING,
        db_column="CompanyTypeId",
        related_name="Branch",
    )
    companyname = models.CharField(db_column="CompanyName", max_length=50)
    street = models.CharField(db_column="Street", max_length=50)
    house = models.CharField(db_column="House", max_length=50, blank=True, null=True)
    city = models.CharField(db_column="City", max_length=50, blank=True, null=True)
    postalcode = models.CharField(
        db_column="PostalCode", max_length=20, blank=True, null=True
    )
    phonenumber = models.CharField(db_column="PhoneNumber", unique=True, max_length=30)
    contact = models.CharField(db_column="Contact", max_length=50, blank=True, null=True)
    deliverytimes = models.CharField(
        db_column="DeliveryTimes", max_length=50, blank=True, null=True
    )
    closeddays = models.CharField(
        db_column="ClosedDays", max_length=50, blank=True, null=True
    )
    callbackdate = models.DateTimeField(db_column="CallBackDate", blank=True, null=True)
    protokoll = models.TextField(db_column="Protokoll", blank=True, null=True)
    notes = models.TextField(db_column="Notes", blank=True, null=True)
    newtoggle = models.IntegerField(db_column="NewToggle", blank=True, null=True)
    nichtmahnen = models.IntegerField(db_column="NichtMahnen", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "Customers"

    def __str__(self) -> str:
        return self.companyname


class Editors(models.Model):
    username = models.CharField(db_column="Username", primary_key=True, max_length=255)

    class Meta:
        managed = False
        db_table = "Editors"


class Employees(models.Model):
    employeeid = models.AutoField(db_column="EmployeeID", primary_key=True)
    codename = models.CharField(db_column="Codename", unique=True, max_length=50)
    firstname = models.CharField(
        db_column="FirstName", max_length=50, blank=True, null=True
    )
    lastname = models.CharField(
        db_column="LastName", max_length=50, blank=True, null=True
    )
    username = models.CharField(
        db_column="UserName", max_length=50, blank=True, null=True
    )
    dateofbirth = models.DateTimeField(db_column="DateOfBirth", blank=True, null=True)
    street = models.CharField(db_column="Street", max_length=50, blank=True, null=True)
    house = models.CharField(db_column="House", max_length=50, blank=True, null=True)
    city = models.CharField(db_column="City", max_length=50, blank=True, null=True)
    postalcode = models.CharField(
        db_column="PostalCode", max_length=50, blank=True, null=True
    )
    phonenumber = models.CharField(
        db_column="PhoneNumber", max_length=50, blank=True, null=True
    )
    mobile = models.CharField(db_column="Mobile", max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "Employees"

    def __str__(self) -> str:
        return self.codename if self.codename is not None else "None"


class MyCompanyInformation(models.Model):
    setupid = models.AutoField(db_column="SetupID", primary_key=True)
    salestaxrate = models.FloatField(db_column="SalesTaxRate", blank=True, null=True)
    companyname = models.CharField(db_column="CompanyName", max_length=50)
    street = models.CharField(db_column="Street", max_length=50)
    house = models.CharField(db_column="House", max_length=50)
    city = models.CharField(db_column="City", max_length=50)
    postalcode = models.CharField(db_column="PostalCode", max_length=20)
    phonenumber = models.CharField(db_column="PhoneNumber", max_length=30)
    faxnumber = models.CharField(
        db_column="FaxNumber", max_length=30, blank=True, null=True
    )
    defaultpaymentterms = models.CharField(
        db_column="DefaultPaymentTerms", max_length=255, blank=True, null=True
    )
    bankdetails = models.CharField(
        db_column="BankDetails", max_length=255, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "My Company Information"


class Oldinvoicelist(models.Model):
    # TODO: Changed orderid from AutoField. What is the diff??
    orderid = models.IntegerField(db_column="OrderID")
    nichtmahnen = models.IntegerField(db_column="NichtMahnen", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "OldInvoiceList"


class OrderDetails(models.Model):
    orderdetailid = models.AutoField(db_column="OrderDetailID", primary_key=True)
    orderid = models.IntegerField(db_column="OrderID")
    productid = models.IntegerField(db_column="ProductID")
    quantity = models.FloatField(db_column="Quantity")
    units = models.IntegerField(db_column="Units")
    unitprice = models.DecimalField(
        db_column="UnitPrice", max_digits=19, decimal_places=4
    )
    commission = models.FloatField(db_column="Commission")
    variable = models.IntegerField(db_column="Variable")

    class Meta:
        managed = False
        db_table = "Order Details"


class Orders(models.Model):
    orderid = models.AutoField(db_column="OrderID", primary_key=True)
    customer = models.ForeignKey(
        "Customers", db_column="CustomerID", on_delete=models.DO_NOTHING
    )
    employeeid = models.IntegerField(db_column="EmployeeID")
    orderdate = models.DateTimeField(db_column="OrderDate", blank=True, null=True)
    invoicenumber = models.CharField(
        db_column="InvoiceNumber", max_length=50, blank=True, null=True
    )
    shipname = models.CharField(
        db_column="ShipName", max_length=50, blank=True, null=True
    )
    shipstreet = models.CharField(
        db_column="ShipStreet", max_length=50, blank=True, null=True
    )
    shiphouse = models.CharField(
        db_column="ShipHouse", max_length=50, blank=True, null=True
    )
    shipcity = models.CharField(
        db_column="ShipCity", max_length=50, blank=True, null=True
    )
    shippostalcode = models.CharField(
        db_column="ShipPostalCode", max_length=20, blank=True, null=True
    )
    shipphonenumber = models.CharField(
        db_column="ShipPhoneNumber", max_length=30, blank=True, null=True
    )
    shipdate = models.DateTimeField(db_column="ShipDate", blank=True, null=True)
    shippingmethodid = models.IntegerField(
        db_column="ShippingMethodID", blank=True, null=True
    )
    freightcharge = models.DecimalField(
        db_column="FreightCharge", max_digits=19, decimal_places=4, blank=True, null=True
    )
    salestaxrate = models.FloatField(db_column="SalesTaxRate")
    deliverytimes = models.CharField(
        db_column="DeliveryTimes", max_length=50, blank=True, null=True
    )
    closeddays = models.CharField(
        db_column="ClosedDays", max_length=50, blank=True, null=True
    )
    notes = models.TextField(db_column="Notes", blank=True, null=True)
    priceadjustment = models.DecimalField(
        db_column="PriceAdjustment",
        max_digits=19,
        decimal_places=4,
        blank=True,
        null=True,
    )
    newcustomer = models.IntegerField(db_column="NewCustomer")

    class Meta:
        managed = False
        db_table = "Orders"

    def __str__(self) -> str:
        return str(self.orderid)


class PaymentMethods(models.Model):
    paymentmethodid = models.AutoField(db_column="PaymentMethodID", primary_key=True)
    paymentmethod = models.CharField(db_column="PaymentMethod", max_length=50)

    class Meta:
        managed = False
        db_table = "Payment Methods"


class Payments(models.Model):
    paymentid = models.AutoField(db_column="PaymentID", primary_key=True)
    orderid = models.IntegerField(db_column="OrderID")
    paymentamount = models.DecimalField(
        db_column="PaymentAmount", max_digits=19, decimal_places=4, blank=True, null=True
    )
    paymentdate = models.DateTimeField(db_column="PaymentDate", blank=True, null=True)
    paymentmethodid = models.IntegerField(
        db_column="PaymentMethodID", blank=True, null=True
    )
    accountname = models.CharField(
        db_column="AccountName", max_length=50, blank=True, null=True
    )
    sortcode = models.CharField(
        db_column="SortCode", max_length=50, blank=True, null=True
    )
    accountnumber = models.CharField(
        db_column="AccountNumber", max_length=50, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "Payments"


class Products(models.Model):
    productid = models.AutoField(db_column="ProductID", primary_key=True)
    productname = models.CharField(db_column="ProductName", max_length=255)
    units = models.CharField(db_column="Units", max_length=50, blank=True, null=True)
    unitprice = models.DecimalField(
        db_column="UnitPrice", max_digits=19, decimal_places=4
    )
    date = models.DateTimeField(db_column="Date", blank=True, null=True)
    commission = models.FloatField(db_column="Commission", blank=True, null=True)
    variable = models.IntegerField(db_column="Variable", blank=True, null=True)
    dpdtext = models.CharField(db_column="DPDText", max_length=50, blank=True, null=True)
    show = models.IntegerField(db_column="Show", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "Products"


class ShippingMethods(models.Model):
    shippingmethodid = models.AutoField(db_column="ShippingMethodID", primary_key=True)
    shippingmethod = models.CharField(db_column="ShippingMethod", max_length=20)

    class Meta:
        managed = False
        db_table = "Shipping Methods"


class Stockcontrol(models.Model):
    id = models.AutoField(db_column="ID", primary_key=True)
    itemname = models.CharField(
        db_column="ItemName", max_length=50, blank=True, null=True
    )
    initialcount = models.IntegerField(db_column="InitialCount", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "StockControl"


class Stockcontrolsettings(models.Model):
    id = models.AutoField(db_column="ID", primary_key=True)
    countdate = models.DateTimeField(db_column="CountDate", blank=True, null=True)

    class Meta:
        managed = False
        db_table = "StockControlSettings"


class SwitchboardItems(models.Model):
    switchboardid = models.IntegerField(db_column="SwitchboardID", primary_key=True)
    itemnumber = models.IntegerField(db_column="ItemNumber")
    itemtext = models.CharField(
        db_column="ItemText", max_length=255, blank=True, null=True
    )
    command = models.IntegerField(db_column="Command", blank=True, null=True)
    argument = models.CharField(
        db_column="Argument", max_length=255, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "Switchboard Items"
        unique_together = (("switchboardid", "itemnumber"),)


class SwitchboardItems1(models.Model):
    switchboardid = models.IntegerField(db_column="SwitchboardID", primary_key=True)
    itemnumber = models.IntegerField(db_column="ItemNumber")
    itemtext = models.CharField(
        db_column="ItemText", max_length=255, blank=True, null=True
    )
    command = models.IntegerField(db_column="Command", blank=True, null=True)
    argument = models.CharField(
        db_column="Argument", max_length=255, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "Switchboard Items1"
        unique_together = (("switchboardid", "itemnumber"),)


class Users(models.Model):
    userid = models.AutoField(db_column="UserID", primary_key=True)
    useralias = models.CharField(
        db_column="UserAlias", max_length=255, blank=True, null=True
    )
    useranrede = models.CharField(
        db_column="UserAnrede", max_length=255, blank=True, null=True
    )
    uservorname = models.CharField(
        db_column="UserVorname", max_length=255, blank=True, null=True
    )
    usernachname = models.CharField(
        db_column="UserNachname", max_length=255, blank=True, null=True
    )
    userpasswort = models.CharField(
        db_column="UserPasswort", max_length=255, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "Users"


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = "auth_group"


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey("AuthPermission", models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_group_permissions"
        unique_together = (("group", "permission"),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey("DjangoContentType", models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "auth_permission"
        unique_together = (("content_type", "codename"),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "auth_user"


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_user_groups"
        unique_together = (("user", "group"),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_user_user_permissions"
        unique_together = (("user", "permission"),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        "DjangoContentType", models.DO_NOTHING, blank=True, null=True
    )
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "django_admin_log"


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "django_content_type"
        unique_together = (("app_label", "model"),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_migrations"


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_session"
