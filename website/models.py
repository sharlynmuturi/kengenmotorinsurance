from django.db import models
import datetime
from django.utils import timezone


# Create your models here.
class StaffVehicle(models.Model):
	regno = models.CharField(max_length=100, unique=True)
	firstname = models.CharField(max_length=100, null=True)
	middlename = models.CharField(max_length=100, blank=True, null=True)
	lastname = models.CharField(max_length=100, null=True)
	staffno = models.IntegerField(null=True)
	employmentstatuschoices = [
	        ('staff', 'Staff'),
	        ('director/manager', 'Director/Manager'),
	        ('ex-staff', 'Ex-Staff'),
	        ('ex-director/manager', 'Ex-Director/Manager'),
	]
	employmentstatus = models.CharField(max_length=100, choices=employmentstatuschoices, null=True)
	email = models.EmailField(default='example@example.com', null=True)
	area = models.CharField(max_length=100, null=True)
	phoneno = models.CharField(max_length=15, null=True)
	idno = models.IntegerField(null=True)
	krapin = models.CharField(max_length=100, null=True)
	sumassured = models.CharField(max_length=100, null=True)
	make = models.CharField(max_length=100, null=True)  # Default is a string 'Unknown Make'
	rating = models.CharField(max_length=100,null=True)  # Default is a string 'Unrated'
	chasisno = models.CharField(max_length=100, null=True)  # Default is 'N/A'
	yom = models.IntegerField(null=True)  # Default year of manufacture is 2000
	typeofvehiclechoices = [
		('private', 'Private'),
		('commercial', 'Commercial'),
	]
	typeofvehicle = models.CharField(max_length=100, choices=typeofvehiclechoices, null=True)
	typeofcoverchoices = [
		('comprehensive', 'Comprehensive'),
		('thirdparty', 'ThirdParty'),
	]
	typeofcover = models.CharField(max_length=100, choices=typeofcoverchoices, null=True)
	commencementdate = models.DateField(null=True, default=datetime.date.today)
	logbook = models.FileField(blank=True,null=True)  # Optional file upload
	statuschoices = [
    	('absent', 'Cover Not Provided'),	
    	('active', 'Cover Active'),
    	('cancelled', 'Cover Cancelled'),
    ]
	status = models.CharField(max_length=100, choices=statuschoices, default='absent', blank=True, null=True)
	dateofcancelorexpiry = models.DateField(null=True, blank=True)

	def __str__(self):
		return self.regno


class CompanyVehicle(models.Model):
	regno = models.CharField(max_length=100, unique=True)
	area = models.CharField(max_length=100, null= True, blank=True)
	sumassured = models.IntegerField(null=True)
	make = models.CharField(max_length=100, null=True)  # Default is a string 'Unknown Make'
	rating = models.CharField(max_length=100, null=True)  # Default is a string 'Unrated'
	chasisno = models.CharField(max_length=100, null=True)  # Default is 'N/A'
	yom = models.IntegerField(null=True)  # Default year of manufacture is 2000
	commencementdate = models.DateField(null=True, default=datetime.date.today)
	logbook = models.FileField(blank=True, null=True)  # Optional file upload
	statuschoices = [
	    ('absent', 'Cover Not Provided'),
    	('active', 'Cover Active'),
    	('cancelled', 'Cover Cancelled'),
    ]
	status = models.CharField(max_length=100, choices=statuschoices, default='absent', blank=True, null=True)
	dateofcancelorexpiry = models.DateField(null=True, blank=True)

	def __str__(self):
		return self.regno



class Premium(models.Model):
	regno = models.CharField(max_length=100)
	firstname = models.CharField(max_length=100, null=True)
	middlename = models.CharField(max_length=100, blank=True, null=True)
	lastname = models.CharField(max_length=100, blank=True, null=True)
	staffno = models.IntegerField(null=True, blank=True)
	typeofcoverchoices = [
		('comprehensive', 'Comprehensive'),
		('thirdparty', 'ThirdParty'),
	]
	typeofcover = models.CharField(max_length=100, choices=typeofcoverchoices, null=True)
	commencementdate = models.DateField(default=datetime.date.today)
	dateofcancelorexpiry = models.DateField(default=datetime.date.today)
	sumassured = models.IntegerField()
	premiumrate = models.DecimalField(max_digits=5, decimal_places=2)
	annualpremium = models.IntegerField(default=0, blank=True)
	prorata = models.IntegerField(default=0, blank=True)
	windscreenadditionalpremium = models.IntegerField(default=0)
	radioadditionalpremium = models.IntegerField(default=0)
	courtesycar = models.IntegerField(default=0)
	excessprotector = models.IntegerField(default=0)
	grandtotal = models.IntegerField(default=0, blank=True, null=True)
	levies = models.IntegerField(default=0, blank=True, null=True)
	premiumpayable = models.IntegerField(default=0, blank=True, null=True)
	amountpaid = models.IntegerField(default=0, blank=True, null=True)
	amountremaining = models.IntegerField(null=True, default=0, blank=True)
	statuschoices = [
    	('paid', 'Payment Made'),
    	('partpaid', 'Part Payment'),
    	('unpaid', 'Payment Not Made'),
    ]
	status = models.CharField(max_length=100, choices=statuschoices, blank=True, null=True)
	paymentmethodchoices = [
    	('cashpayment', 'Cash Payment'),
    	('salarydeduction', 'Salary Deduction'),
    	('otherpayment', 'Other'),
    ]
	paymentmethod = models.CharField(max_length=100, choices=paymentmethodchoices, blank=True, null=True)
	amountrefund = models.IntegerField(null=True, default=0, blank=True)
	refundstatuschoices = [
    	('refunded', 'Refund Made'),
    	('norefund', 'No Refund'),
    ]
	refundstatus = models.CharField(max_length=100, choices=refundstatuschoices, null=True, blank=True)


	def __str__(self):
		return self.regno

