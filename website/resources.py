from import_export import resources
from .models import StaffVehicle
from .models import CompanyVehicle
from .models import Premium
from .models import StaffMember
from .models import ContactMessage


class StaffVehicleResource(resources.ModelResource):
    class Meta:
        model = StaffVehicle

class CompanyVehicleResource(resources.ModelResource):
    class Meta:
        model = CompanyVehicle

class PremiumResource(resources.ModelResource):
    class Meta:
        model = Premium

class StaffMemberResource(resources.ModelResource):
    class Meta:
        model = StaffMember
        
class ContactMessageResource(resources.ModelResource):
    class Meta:
        model = ContactMessage
