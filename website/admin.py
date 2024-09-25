from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import StaffVehicle
from .models import CompanyVehicle
from .models import Premium
from .models import StaffMember
from .models import ContactMessage

from .resources import StaffVehicleResource
from .resources import CompanyVehicleResource
from .resources import PremiumResource
from .resources import StaffMemberResource
from .resources import ContactMessageResource


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
@admin.register(StaffMember)
class StaffMemberAdmin(ImportExportModelAdmin):
    resource_class = StaffMemberResource
@admin.register(ContactMessage)
class ContactMessageAdmin(ImportExportModelAdmin):
    resource_class = ContactMessageResource