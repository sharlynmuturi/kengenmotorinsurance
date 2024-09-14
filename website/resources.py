from import_export import resources
from .models import StaffVehicle
from .models import CompanyVehicle
from .models import Premium



class StaffVehicleResource(resources.ModelResource):
    class Meta:
        model = StaffVehicle

class CompanyVehicleResource(resources.ModelResource):
    class Meta:
        model = CompanyVehicle

class PremiumResource(resources.ModelResource):
    class Meta:
        model = Premium


