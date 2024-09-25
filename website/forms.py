from django import forms
from django.core.exceptions import ValidationError
from .models import StaffVehicle
from .models import CompanyVehicle
from .models import Premium

from datetime import date
import datetime
from django.utils import timezone

from decimal import Decimal



class StaffVehicleForm(forms.ModelForm):
    class Meta:
        model = StaffVehicle
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        # Pass the user object to the form
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # Set fields as read-only for unauthenticated users
        if self.user and not self.user.is_authenticated:
            self.fields['status'].widget.attrs['disabled'] = 'disabled'
            self.fields['dateofcancelorexpiry'].widget.attrs['disabled'] = 'disabled'
            # Optionally set default values
            self.fields['status'].initial = 'absent'  # Example default value
            # self.fields['dateofcancelorexpiry'].initial = timezone.now().date()


    def clean_regno(self):
        regno_value = self.cleaned_data.get('regno')

        # Check if a record with the same regno already exists
        if StaffVehicle.objects.filter(regno=regno_value).exists():
            raise ValidationError("A record with this registration number already exists.")

        return regno_value


class CompanyVehicleForm(forms.ModelForm):
	class Meta:
		model = CompanyVehicle
		fields = '__all__'
		# fields = ['regno', 'area', 'sumassured', 'make', 'rating', 'chasisno', 'yom', 'status','commencementdate', 'dateofcancelorexpiry', 'logbook']

	def clean_regno(self):
		regno_value = self.cleaned_data.get('regno')

		#check if a record with the same entryfor regno already exists
		if CompanyVehicle.objects.filter(regno=regno_value).exists():
			raise ValidationError("A record with this entry already exists.")

		return regno_value



class PremiumForm(forms.ModelForm):
    class Meta:
        model = Premium
        fields = '__all__'


    def clean(self):
        cleaned_data = super().clean()
        
        # Getting form data
        annualpremium = cleaned_data.get('annualpremium', 0)  # Default to 0 if None
        prorata = cleaned_data.get('prorata', 0)  # Default to 0 if None
        grandtotal = cleaned_data.get('grandtotal', 0)  # Default to 0 if None        
        premiumpayable = cleaned_data.get('premiumpayable', 0)  # Default to 0 if None
        sumassured = cleaned_data.get('sumassured')
        premiumrate = cleaned_data.get('premiumrate')
        commencementdate = cleaned_data.get('commencementdate')
        dateofcancelorexpiry = cleaned_data.get('dateofcancelorexpiry')
        windscreenadditionalpremium = cleaned_data.get('windscreenadditionalpremium', 0)
        radioadditionalpremium = cleaned_data.get('radioadditionalpremium', 0)
        courtesycar = cleaned_data.get('courtesycar', 0)
        excessprotector = cleaned_data.get('excessprotector', 0)
        levies = cleaned_data.get('levies', 0)
        amountpaid = cleaned_data.get('amountpaid', 0)
        amountremaining = cleaned_data.get('amountremaining', 0)

       # Handle prorata calculation
        if commencementdate and dateofcancelorexpiry:
            total_days = (dateofcancelorexpiry - commencementdate).days + 1  # Include the end date in the calculation
            # Convert sumassured and premiumrate to Decimal for consistency
            annualpremium = Decimal(sumassured) * Decimal(premiumrate) / Decimal(100)
            prorata_factor = Decimal(total_days) / Decimal(365)
            prorata = annualpremium * prorata_factor
            prorata = int(prorata)
        else:
            prorata = 0

        grandtotal = prorata + windscreenadditionalpremium + radioadditionalpremium + courtesycar + excessprotector
        premiumpayable = grandtotal + levies
        amountremaining = premiumpayable - amountpaid

        # Set the calculated fields
        cleaned_data['annualpremium'] = annualpremium
        cleaned_data['prorata'] = prorata
        cleaned_data['grandtotal'] = grandtotal
        cleaned_data['premiumpayable'] = premiumpayable
        cleaned_data['amountremaining'] = amountremaining


        return cleaned_data


class UpdateVehicleForm(forms.ModelForm):
    class Meta:
        model = StaffVehicle
        fields = ['status', 'dateofcancelorexpiry']


class UpdateStaffVehicleForm(forms.ModelForm):
    class Meta:
        model = StaffVehicle
        fields = '__all__'


class UpdateCompanyVehicleForm(forms.ModelForm):
    class Meta:
        model = CompanyVehicle
        fields = '__all__'

class UpdatePremiumForm(forms.ModelForm):
    class Meta:
        model = Premium
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()

        # Getting form data
        annualpremium = cleaned_data.get('annualpremium', 0)  # Default to 0 if None
        prorata = cleaned_data.get('prorata', 0)  # Default to 0 if None
        grandtotal = cleaned_data.get('grandtotal', 0)  # Default to 0 if None        
        premiumpayable = cleaned_data.get('premiumpayable', 0)  # Default to 0 if None
        sumassured = cleaned_data.get('sumassured')
        premiumrate = cleaned_data.get('premiumrate')
        commencementdate = cleaned_data.get('commencementdate')
        dateofcancelorexpiry = cleaned_data.get('dateofcancelorexpiry')
        windscreenadditionalpremium = cleaned_data.get('windscreenadditionalpremium', 0)
        radioadditionalpremium = cleaned_data.get('radioadditionalpremium', 0)
        courtesycar = cleaned_data.get('courtesycar', 0)
        excessprotector = cleaned_data.get('excessprotector', 0)
        levies = cleaned_data.get('levies', 0)
        amountpaid = cleaned_data.get('amountpaid', 0)
        amountremaining = cleaned_data.get('amountremaining', 0)


        # Handle prorata calculation
        if commencementdate and dateofcancelorexpiry:
            total_days = (dateofcancelorexpiry - commencementdate).days + 1  # Include the end date in the calculation
            # Convert sumassured and premiumrate to Decimal for consistency
            annualpremium = Decimal(sumassured) * Decimal(premiumrate) / Decimal(100)
            prorata_factor = Decimal(total_days) / Decimal(365)
            prorata = annualpremium * prorata_factor
            prorata = int(prorata)
        else:
            prorata = 0


        grandtotal = prorata + windscreenadditionalpremium + radioadditionalpremium + courtesycar + excessprotector
        premiumpayable = grandtotal + levies
        amountremaining = premiumpayable - amountpaid


        # Ensure fields are set to calculated values
        cleaned_data['annualpremium'] = annualpremium
        cleaned_data['prorata'] = prorata
        cleaned_data['grandtotal'] = grandtotal
        cleaned_data['premiumpayable'] = premiumpayable
        cleaned_data['amountremaining'] = amountremaining

        return cleaned_data
