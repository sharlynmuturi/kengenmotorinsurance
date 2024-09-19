from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q  # for complex queries
from django.urls import reverse
from django.http import HttpResponse
from import_export.admin import ExportActionModelAdmin
from import_export.formats.base_formats import XLSX
import openpyxl

from .models import StaffVehicle
from .models import CompanyVehicle
from .models import Premium

from .forms import StaffVehicleForm
from .forms import CompanyVehicleForm
from .forms import PremiumForm

from .forms import UpdateVehicleForm
from .forms import UpdateStaffVehicleForm
from .forms import UpdateCompanyVehicleForm
from .forms import UpdatePremiumForm


from .resources import StaffVehicleResource
from .resources import CompanyVehicleResource
from .resources import PremiumResource

from django.core.mail import send_mail

import os

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def thankyou(request):
    return render(request, 'thankyou.html', {})

from django.core.mail import send_mail
def contactus(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        # Optional: Send an email
        send_mail(
            subject,
            message,
            email,
            ['sharlynnmuturi@gmail.com'],  # Change to the email
        )

        messages.success(request, 'Your message has been sent!')
        return redirect('contactus')
    return render(request, 'contactus.html')

def download_logbook(request, pk):
    staff_vehicle = get_object_or_404(StaffVehicle, pk=pk)
    logbook_file = staff_vehicle.logbook

    if not logbook_file:
        raise Http404("No logbook file available.")

    return FileResponse(logbook_file, as_attachment=True)


def download_logbook2(request, pk):
    company_vehicle = get_object_or_404(CompanyVehicle, pk=pk)
    logbook_file = company_vehicle.logbook

    if not logbook_file:
        raise Http404("No logbook file available.")

    return FileResponse(logbook_file, as_attachment=True)

##################################################################################### PREMIUMS ##########################
def premium(request):
    all_premium = Premium.objects.all()
    return render(request, 'premium.html', {'all':all_premium})


def premiumform(request):
    if request.method == "POST":
        form = PremiumForm(request.POST, request.FILES)  # Include request.FILES for file input
        if form.is_valid():
            # Save the form, which will trigger the model's save method
            premium = form.save()
            # Display a success message
            messages.success(request, 'Premium Successfully Computed and Recorded!')
            # Redirect to the computedpremium view with the premium object's ID
            return redirect('computedpremium', pk=premium.pk)
        else:
            messages.error(request, 'There was an error in your input. Please check for error messages and try again.')
            # Render the form with errors
            return render(request, 'premiumform.html', {'form': form})
    else:
        # Create an empty form for GET request
        form = PremiumForm()
        return render(request, 'premiumform.html', {'form': form})


def searchallpremium(request):
    if request.method == "POST":
        searched = request.POST.get('searchedpremium', None)
        # Redirect to the allcompanyvehicle view with the search term as a query parameter
        return redirect(reverse('allpremium') + f'?searchedpremium={searched}')
    else:
        return render(request, 'searchallpremium.html', {})


def update_premium(request, pk):
    # Retrieve the Premium object with the given primary key (pk)
    premium = get_object_or_404(Premium, pk=pk)
    if request.method == 'POST':
        # Bind the form to the POST data and the specific instance of the Premium model
        form = UpdatePremiumForm(request.POST, instance=premium)
        if form.is_valid():
            # Save the form which automatically computes the premiumpayable and grandtotal in the clean method
            form.save()
            # Optionally, display a success message
            messages.success(request, 'Premium record updated successfully.')
            # Redirect to the detail view of the updated record
            return redirect('update_premium', pk=premium.pk)
        else:
            # If the form is not valid, return errors
            messages.error(request, 'There was an error updating the premium record. Please check your input.')
    else:
        # If it's a GET request, instantiate the form with the existing premium data
        form = UpdatePremiumForm(instance=premium)
    # Render the template with the form
    return render(request, 'update_premium.html', {'form': form, 'premium': premium})

def delete_premium(request, pk):
    vehicle = get_object_or_404(Premium, pk=pk)
    
    if request.method == 'POST':
        vehicle.delete()
        return redirect('allpremium')  # Redirect to a list or home page after deletion
    
    return render(request, 'confirm_delete.html', {'vehicle': vehicle})

def allpremium(request):
    # Check if there is a search query
    searched = request.GET.get('searchedpremium', None)
    if searched:
        searchedpremiums = Premium.objects.filter(regno__icontains=searched)
        forms = [PremiumForm(instance=vehicle) for vehicle in searchedpremiums]
    else:
        allpremiums = Premium.objects.all()
        forms = [PremiumForm(instance=vehicle) for vehicle in allpremiums]
    return render(request, 'allpremium.html', {'forms': forms, 'searched': searched})

def comprehensivepremium(request):
    comprehensivepremium = Premium.objects.filter(typeofcover='comprehensive')
    forms = [PremiumForm(instance=vehicle) for vehicle in comprehensivepremium]
    return render(request, 'comprehensivepremium.html', {'forms': forms})

def thirdpartypremium(request):
    thirdpartypremium = Premium.objects.filter(typeofcover='thirdparty')
    forms = [PremiumForm(instance=vehicle) for vehicle in thirdpartypremium]
    return render(request, 'thirdpartypremium.html', {'forms': forms})


def computedpremium(request, pk):
    # Retrieve the premium object
    premium = get_object_or_404(Premium, pk=pk)
    if request.method == 'POST':
        # Create a form instance with POST data and the current premium instance
        form = PremiumForm(request.POST, instance=premium)
        if form.is_valid():
            # Save the form, which will trigger the model's save method
            form.save()
            # Extract computed data directly from the model instance
            annualpremium = premium.annualpremium
            prorata = premium.prorata
            grandtotal = premium.grandtotal
            premiumpayable = premium.premiumpayable
            amountremaining = premium.amountremaining
            # Render the results in computedpremium.html
            return render(request, 'computedpremium.html', {
                'annualpremium': annualpremium, 
                'prorata': prorata,
                'grandtotal': grandtotal,
                'premiumpayable': premiumpayable,
                'amountremaining': amountremaining
            })
    else:
        # Create a form instance with the current premium object for GET request
        form = PremiumForm(instance=premium)
    # If not a POST request or form is invalid, render the form template
    return render(request, 'premiumform.html', {'form': form})


def paidpremium(request):
    paidpremiums = Premium.objects.filter(status='paid')
    forms = [PremiumForm(instance=vehicle) for vehicle in paidpremiums]
    return render(request, 'paidpremium.html', {'forms': forms})

def unpaidpremium(request):
    unpaidpremiums = Premium.objects.filter(status='unpaid')
    forms = [PremiumForm(instance=vehicle) for vehicle in unpaidpremiums]
    return render(request, 'unpaidpremium.html', {'forms': forms})

def partpaidpremium(request):
    partpaidpremiums = Premium.objects.filter(status='partpaid')
    forms = [PremiumForm(instance=vehicle) for vehicle in partpaidpremiums]
    return render(request, 'partpaidpremium.html', {'forms': forms})

def cashpayment(request):
    cashpayments = Premium.objects.filter(paymentmethod='cashpayment')
    forms = [PremiumForm(instance=vehicle) for vehicle in cashpayments]
    return render(request, 'cashpayment.html', {'forms': forms})

def otherpayment(request):
    otherpayments = Premium.objects.filter(paymentmethod='otherpayment')
    forms = [PremiumForm(instance=vehicle) for vehicle in otherpayments]
    return render(request, 'otherpayment.html', {'forms': forms})


def salarydeduction(request):
    salarydeductions = Premium.objects.filter(paymentmethod='salarydeduction')
    forms = [PremiumForm(instance=vehicle) for vehicle in salarydeductions]
    return render(request, 'salarydeduction.html', {'forms': forms})

def premiumrefund(request):
    premiumrefunds = Premium.objects.filter(refundstatus='refunded')
    forms = [PremiumForm(instance=vehicle) for vehicle in premiumrefunds]
    return render(request, 'premiumrefund.html', {'forms': forms})

def export_comprehensive_premiums(request):
    # Filter the queryset to include only active vehicles
    vehicles = Premium.objects.filter(typeofcover='comprehensive')

    # Use the resource to handle the export
    resource = PremiumResource()
    dataset = resource.export(queryset=vehicles)  # Pass the filtered queryset to the export

    filename = 'comprehensive_premiums_covers.xlsx'
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    return response

def export_thirdparty_premiums(request):
    # Filter the queryset to include only active vehicles
    vehicles = Premium.objects.filter(typeofcover='thirdparty')

    # Use the resource to handle the export
    resource = PremiumResource()
    dataset = resource.export(queryset=vehicles)  # Pass the filtered queryset to the export

    filename = 'thirdparty_premiums_covers.xlsx'
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    return response

def export_premiums(request):
    resource = PremiumResource()
    dataset = resource.export()  # Export data from the resource

    # Specify your desired filename here
    filename = 'AllPremiums.xlsx'
    
    # Create an HTTP response with the exported data
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    return response


def export_refunded_premiums(request):
    # Filter the queryset to include only active vehicles
    vehicles = Premium.objects.filter(refundstatus='refunded')

    # Use the resource to handle the export
    resource = PremiumResource()
    dataset = resource.export(queryset=vehicles)  # Pass the filtered queryset to the export

    filename = 'refunded_premiums.xlsx'
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    return response


def export_paid_premiums(request):
    # Filter the queryset to include only active vehicles
    vehicles = Premium.objects.filter(status='paid')

    # Use the resource to handle the export
    resource = PremiumResource()
    dataset = resource.export(queryset=vehicles)  # Pass the filtered queryset to the export

    filename = 'paid_premiums.xlsx'
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    return response


def export_unpaid_premiums(request):
    # Filter the queryset to include only active vehicles
    vehicles = Premium.objects.filter(status='unpaid')

    # Use the resource to handle the export
    resource = PremiumResource()
    dataset = resource.export(queryset=vehicles)  # Pass the filtered queryset to the export

    filename = 'unpaid_premiums.xlsx'
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    return response

def export_partpaid_premiums(request):
    # Filter the queryset to include only active vehicles
    vehicles = Premium.objects.filter(status='partpaid')

    # Use the resource to handle the export
    resource = PremiumResource()
    dataset = resource.export(queryset=vehicles)  # Pass the filtered queryset to the export

    filename = 'partpaid_premiums.xlsx'
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    return response

def export_cash_payments(request):
    # Filter the queryset to include only active vehicles
    vehicles = Premium.objects.filter(paymentmethod='cashpayment')

    # Use the resource to handle the export
    resource = PremiumResource()
    dataset = resource.export(queryset=vehicles)  # Pass the filtered queryset to the export

    filename = 'cash_payments.xlsx'
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    return response


def export_salary_deductions(request):
    # Filter the queryset to include only active vehicles
    vehicles = Premium.objects.filter(paymentmethod='salarydeduction')

    # Use the resource to handle the export
    resource = PremiumResource()
    dataset = resource.export(queryset=vehicles)  # Pass the filtered queryset to the export

    filename = 'salary_deductions.xlsx'
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    return response

def export_other_payments(request):
    # Filter the queryset to include only active vehicles
    vehicles = Premium.objects.filter(paymentmethod='otherpayment')

    # Use the resource to handle the export
    resource = PremiumResource()
    dataset = resource.export(queryset=vehicles)  # Pass the filtered queryset to the export

    filename = 'other_payment_methods.xlsx'
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    return response


################################################################# STAFF VEHICLES ##########################################################################

def staffvehicle(request):
    all_staff_vehicle = StaffVehicle.objects.all()
    return render(request, 'staffvehicle.html', {'all':all_staff_vehicle})

def staffvehicleform(request):
    if request.method == "POST":
        form = StaffVehicleForm(request.POST, request.FILES, user=request.user)  # Include request.FILES for file upload
        regno = form.data.get('regno')  # Get the registration number from form data

        # Check if a vehicle with the same regno already exists
        if StaffVehicle.objects.filter(regno=regno).exists():
            vehicle = StaffVehicle.objects.get(regno=regno)

            # Redirect to the update form for status and date_of_cancel
            messages.warning(request, f'Vehicle {regno} already exist.')
            return redirect('update_vehicle', vehicle_id=vehicle.id)

        if form.is_valid():
            form.save()
            messages.success(request, 'Record Submitted Successfully!')
            return redirect('thankyou')
        else:
            messages.error(request, 'There was an error in your input. Please check for error messages and try again.')
    else:
        form = StaffVehicleForm(user=request.user)
    return render(request, 'staffvehicleform.html', {'form': form})

def update_staff_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(StaffVehicle, id=vehicle_id)
    if request.method == 'POST':
        form = UpdateStaffVehicleForm(request.POST, request.FILES, instance=vehicle)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vehicle record updated successfully.')
            return redirect('update_staff_vehicle', vehicle_id=vehicle_id)  # Change to your list view or desired redirect
    else:
        form = UpdateStaffVehicleForm(instance=vehicle)

    return render(request, 'update_staffvehicle.html', {'form': form, 'vehicle': vehicle})


def searchallstaffvehicle(request):
    if request.method == "POST":
        searched = request.POST.get('searchedstaffvehicle', None)
        # Redirect to the allstaffvehicle view with the search term as a query parameter
        return redirect(reverse('allstaffvehicle') + f'?searchedstaffvehicle={searched}')
    else:
        return render(request, 'searchallstaffvehicle.html', {})

def delete_staff_vehicle(request, pk):
    vehicle = get_object_or_404(StaffVehicle, pk=pk)
    
    if request.method == 'POST':
        vehicle.delete()
        return redirect('allstaffvehicle')  # Redirect to a list or home page after deletion
    
    return render(request, 'confirm_delete.html', {'vehicle': vehicle})


def update_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(StaffVehicle, id=vehicle_id)

    if request.method == 'POST':
        # Use the custom form that only includes status and date_of_cancel fields
        form = UpdateStaffVehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vehicle record updated successfully!')
            return redirect('update_staff_vehicle', vehicle_id=vehicle_id)
        else:
            messages.error(request, 'Error updating the vehicle record. Please try again.')
    else:
        # Display the custom form with current vehicle data
        form = UpdateStaffVehicleForm(instance=vehicle)

    return render(request, 'update_vehicle_form.html', {'form': form, 'vehicle': vehicle})


    
def allstaffvehicle(request):
    # Check if there is a search query
    searched = request.GET.get('searchedstaffvehicle', None)
    if searched:
        searchedstaffvehicles = StaffVehicle.objects.filter(regno__icontains=searched)
        forms = [StaffVehicleForm(instance=vehicle) for vehicle in searchedstaffvehicles]
    else:
        allstaffvehicles = StaffVehicle.objects.all()
        forms = [StaffVehicleForm(instance=vehicle) for vehicle in allstaffvehicles]
    return render(request, 'allstaffvehicle.html', {'forms': forms, 'searched': searched})


def absentstaffvehicle(request):
    absentstaffvehicles = StaffVehicle.objects.filter(status='absent')
    forms = [StaffVehicleForm(instance=vehicle) for vehicle in absentstaffvehicles]
    return render(request, 'absentstaffvehicle.html', {'forms': forms})

def activestaffvehicle(request):
    activestaffvehicles = StaffVehicle.objects.filter(status='active')
    forms = [StaffVehicleForm(instance=vehicle) for vehicle in activestaffvehicles]
    return render(request, 'activestaffvehicle.html', {'forms': forms})

def cancelledstaffvehicle(request):
    cancelledstaffvehicles = StaffVehicle.objects.filter(status='cancelled')
    forms = [StaffVehicleForm(instance=vehicle) for vehicle in cancelledstaffvehicles]
    return render(request, 'cancelledstaffvehicle.html', {'forms': forms})

def currentstaffvehicle(request):
    currentstaffvehicles = StaffVehicle.objects.filter(employmentstatus='staff')
    forms = [StaffVehicleForm(instance=vehicle) for vehicle in currentstaffvehicles]
    return render(request, 'currentstaffvehicle.html', {'forms': forms})

def managervehicle(request):
    managervehicles = StaffVehicle.objects.filter(employmentstatus='director/manager')
    forms = [StaffVehicleForm(instance=vehicle) for vehicle in managervehicles]
    return render(request, 'managervehicle.html', {'forms': forms})

def exstaffvehicle(request):
    exstaffvehicles = StaffVehicle.objects.filter(employmentstatus='ex-staff')
    forms = [StaffVehicleForm(instance=vehicle) for vehicle in exstaffvehicles]
    return render(request, 'exstaffvehicle.html', {'forms': forms})

def exmanagervehicle(request):
    exmanagervehicles = StaffVehicle.objects.filter(employmentstatus='ex-director/manager')
    forms = [StaffVehicleForm(instance=vehicle) for vehicle in exmanagervehicles]
    return render(request, 'exmanagervehicle.html', {'forms': forms})

def privatevehicle(request):
    privatevehicles = StaffVehicle.objects.filter(typeofvehicle='private')
    forms = [StaffVehicleForm(instance=vehicle) for vehicle in privatevehicles]
    return render(request, 'privatevehicle.html', {'forms': forms})

def commercialvehicle(request):
    commercialvehicles = StaffVehicle.objects.filter(typeofvehicle='commercial')
    forms = [StaffVehicleForm(instance=vehicle) for vehicle in commercialvehicles]
    return render(request, 'commercialvehicle.html', {'forms': forms})

def comprehensivecover(request):
    comprehensivecovers = StaffVehicle.objects.filter(typeofcover='comprehensive')
    forms = [StaffVehicleForm(instance=vehicle) for vehicle in comprehensivecovers]
    return render(request, 'comprehensivecover.html', {'forms': forms})

def thirdpartycover(request):
    thirdpartycovers = StaffVehicle.objects.filter(typeofcover='thirdparty')
    forms = [StaffVehicleForm(instance=vehicle) for vehicle in thirdpartycovers]
    return render(request, 'thirdpartycover.html', {'forms': forms})


def export_staff_vehicles(request):
    resource = StaffVehicleResource()
    dataset = resource.export()  # Export data from the resource

    # Specify your desired filename here
    filename = 'AllStaffVehiclesCovers.xlsx'
    
    # Create an HTTP response with the exported data
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    return response

def export_active_staff_vehicles(request):
    # Filter the queryset to include only active vehicles
    vehicles = StaffVehicle.objects.filter(status='active')

    # Use the resource to handle the export
    resource = StaffVehicleResource()
    dataset = resource.export(queryset=vehicles)  # Pass the filtered queryset to the export

    filename = 'active_staff_vehicles_covers.xlsx'
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    return response

def export_absent_staff_vehicles(request):
    # Filter the queryset to include only active vehicles
    vehicles = StaffVehicle.objects.filter(status='absent')

    # Use the resource to handle the export
    resource = StaffVehicleResource()
    dataset = resource.export(queryset=vehicles)  # Pass the filtered queryset to the export

    filename = 'absent_staff_vehicles_covers.xlsx'
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    return response

def export_cancelled_staff_vehicles(request):
    # Filter the queryset to include only active vehicles
    vehicles = StaffVehicle.objects.filter(status='cancelled')

    # Use the resource to handle the export
    resource = StaffVehicleResource()
    dataset = resource.export(queryset=vehicles)  # Pass the filtered queryset to the export

    filename = 'cancelled_staff_vehicles_covers.xlsx'
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    return response

def export_current_staff_vehicles(request):
    # Filter the queryset to include only active vehicles
    vehicles = StaffVehicle.objects.filter(employmentstatus='staff')

    # Use the resource to handle the export
    resource = StaffVehicleResource()
    dataset = resource.export(queryset=vehicles)  # Pass the filtered queryset to the export

    filename = 'current_staff_vehicles_covers.xlsx'
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    return response

def export_managers_vehicles(request):
    # Filter the queryset to include only active vehicles
    vehicles = StaffVehicle.objects.filter(employmentstatus='director/manager')

    # Use the resource to handle the export
    resource = StaffVehicleResource()
    dataset = resource.export(queryset=vehicles)  # Pass the filtered queryset to the export

    filename = 'directors_managers_vehicles_covers.xlsx'
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    return response

def export_ex_staff_vehicles(request):
    # Filter the queryset to include only active vehicles
    vehicles = StaffVehicle.objects.filter(employmentstatus='ex-staff')

    # Use the resource to handle the export
    resource = StaffVehicleResource()
    dataset = resource.export(queryset=vehicles)  # Pass the filtered queryset to the export

    filename = 'ex_staff_vehicles_covers.xlsx'
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    return response

def export_ex_managers_vehicles(request):
    # Filter the queryset to include only active vehicles
    vehicles = StaffVehicle.objects.filter(employmentstatus='ex-director/manager')

    # Use the resource to handle the export
    resource = StaffVehicleResource()
    dataset = resource.export(queryset=vehicles)  # Pass the filtered queryset to the export

    filename = 'ex_managers_vehicles_covers.xlsx'
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    return response

def export_private_vehicles(request):
    # Filter the queryset to include only active vehicles
    vehicles = StaffVehicle.objects.filter(typeofvehicle='private')

    # Use the resource to handle the export
    resource = StaffVehicleResource()
    dataset = resource.export(queryset=vehicles)  # Pass the filtered queryset to the export

    filename = 'private_vehicles_covers.xlsx'
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    return response

def export_commercial_vehicles(request):
    # Filter the queryset to include only active vehicles
    vehicles = StaffVehicle.objects.filter(typeofvehicle='commercial')

    # Use the resource to handle the export
    resource = StaffVehicleResource()
    dataset = resource.export(queryset=vehicles)  # Pass the filtered queryset to the export

    filename = 'commercial_vehicles_covers.xlsx'
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    return response

def export_comprehensive_vehicles(request):
    # Filter the queryset to include only active vehicles
    vehicles = StaffVehicle.objects.filter(typeofcover='comprehensive')

    # Use the resource to handle the export
    resource = StaffVehicleResource()
    dataset = resource.export(queryset=vehicles)  # Pass the filtered queryset to the export

    filename = 'comprehensive_vehicles_covers.xlsx'
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    return response

def export_thirdparty_vehicles(request):
    # Filter the queryset to include only active vehicles
    vehicles = StaffVehicle.objects.filter(typeofcover='thirdparty')

    # Use the resource to handle the export
    resource = StaffVehicleResource()
    dataset = resource.export(queryset=vehicles)  # Pass the filtered queryset to the export

    filename = 'thirdparty_vehicles_covers.xlsx'
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    return response


######################################################################### COMPANY VEHICLES ######################################################################

def companyvehicle(request):
    all_company_vehicle = CompanyVehicle.objects.all()
    return render(request, 'companyvehicle.html', {'all':all_company_vehicle})

def companyvehicleform(request):
    if request.method == "POST":
        form = CompanyVehicleForm(request.POST, request.FILES)  # Include request.FILES for file upload
        regno = form.data.get('regno')  # Get the registration number from form data

        # Check if a vehicle with the same regno already exists
        if CompanyVehicle.objects.filter(regno=regno).exists():
            vehicle = CompanyVehicle.objects.get(regno=regno)

            # Redirect to the update form for status and date_of_cancel
            messages.warning(request, f'Vehicle {regno} already exist.')
            return redirect('update_company_vehicle', vehicle_id=vehicle.id)

        if form.is_valid():
            form.save()
            messages.success(request, 'Record Submitted Successfully!')
            return redirect('companyvehicleform')
        else:
            messages.error(request, 'There was an error in your input. Please check for error messages and try again.')
    else:
        form = CompanyVehicleForm()
    return render(request, 'companyvehicleform.html', {'form': form})

def update_company_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(CompanyVehicle, id=vehicle_id)
    if request.method == 'POST':
        form = UpdateCompanyVehicleForm(request.POST, request.FILES, instance=vehicle)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vehicle record updated successfully.')
            return redirect('update_company_vehicle', vehicle_id=vehicle_id)  # Change to your list view or desired redirect
    else:
        form = UpdateCompanyVehicleForm(instance=vehicle)

    return render(request, 'update_companyvehicle.html', {'form': form, 'vehicle': vehicle})


def delete_company_vehicle(request, pk):
    vehicle = get_object_or_404(CompanyVehicle, pk=pk)
    
    if request.method == 'POST':
        vehicle.delete()
        return redirect('allcompanyvehicle')  # Redirect to a list or home page after deletion
    
    return render(request, 'confirm_delete.html', {'vehicle': vehicle})

def searchallcompanyvehicle(request):
    if request.method == "POST":
        searched = request.POST.get('searchedcompanyvehicle', None)
        # Redirect to the allcompanyvehicle view with the search term as a query parameter
        return redirect(reverse('allcompanyvehicle') + f'?searchedcompanyvehicle={searched}')
    else:
        return render(request, 'searchallcompanyvehicle.html', {})


def allcompanyvehicle(request):
    # Check if there is a search query
    searched = request.GET.get('searchedcompanyvehicle', None)
    if searched:
        searchedcompanyvehicles = CompanyVehicle.objects.filter(regno__icontains=searched)
        forms = [CompanyVehicleForm(instance=vehicle) for vehicle in searchedcompanyvehicles]
    else:
        allcompanyvehicles = CompanyVehicle.objects.all()
        forms = [CompanyVehicleForm(instance=vehicle) for vehicle in allcompanyvehicles]
    return render(request, 'allcompanyvehicle.html', {'forms': forms, 'searched': searched})


def activecompanyvehicle(request):
    activecompanyvehicles = CompanyVehicle.objects.filter(status='active')
    forms = [CompanyVehicleForm(instance=vehicle) for vehicle in activecompanyvehicles]
    return render(request, 'activecompanyvehicle.html', {'forms': forms})


def cancelledcompanyvehicle(request):
    cancelledcompanyvehicles = CompanyVehicle.objects.filter(status='cancelled')
    forms = [CompanyVehicleForm(instance=vehicle) for vehicle in cancelledcompanyvehicles]
    return render(request, 'cancelledcompanyvehicle.html', {'forms': forms})

def absentcompanyvehicle(request):
    absentcompanyvehicles = CompanyVehicle.objects.filter(status='absent')
    forms = [CompanyVehicleForm(instance=vehicle) for vehicle in absentcompanyvehicles]
    return render(request, 'absentcompanyvehicle.html', {'forms': forms})


def export_company_vehicles(request):
    resource = CompanyVehicleResource()
    dataset = resource.export()  # Export data from the resource

    # Specify your desired filename here
    filename = 'AllCompanyVehiclesCovers.xlsx'
    
    # Create an HTTP response with the exported data
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    return response

def export_active_company_vehicles(request):
    # Filter the queryset to include only active vehicles
    vehicles = CompanyVehicle.objects.filter(status='active')

    # Use the resource to handle the export
    resource = CompanyVehicleResource()
    dataset = resource.export(queryset=vehicles)  # Pass the filtered queryset to the export

    filename = 'active_company_vehicles_covers.xlsx'
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    return response

def export_absent_company_vehicles(request):
    # Filter the queryset to include only active vehicles
    vehicles = CompanyVehicle.objects.filter(status='absent')

    # Use the resource to handle the export
    resource = CompanyVehicleResource()
    dataset = resource.export(queryset=vehicles)  # Pass the filtered queryset to the export

    filename = 'absent_company_vehicles_covers.xlsx'
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    return response


def export_cancelled_company_vehicles(request):
    # Filter the queryset to include only active vehicles
    vehicles = CompanyVehicle.objects.filter(status='cancelled')

    # Use the resource to handle the export
    resource = CompanyVehicleResource()
    dataset = resource.export(queryset=vehicles)  # Pass the filtered queryset to the export

    filename = 'cancelled_company_vehicles_export.xlsx'
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    return response