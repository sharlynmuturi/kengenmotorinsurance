from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import StaffVehicle
from .models import CompanyVehicle
from .models import Premium


from .resources import StaffVehicleResource
from .resources import CompanyVehicleResource
from .resources import PremiumResource

# Register the models with ImportExportModelAdmin
@admin.register(StaffVehicle)
class StaffVehicleAdmin(ImportExportModelAdmin):
    resource_class = StaffVehicleResource
@admin.register(CompanyVehicle)
class CompanyVehicleAdmin(ImportExportModelAdmin):
    resource_class = CompanyVehicleResource
@admin.register(Premium)
class PremiumAdmin(ImportExportModelAdmin):
    resource_class = PremiumResource
