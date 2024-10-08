from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('thankyou', views.thankyou, name="thankyou"),
    path('contactus', views.contactus, name="contactus"),
    
    path('feedbacks/', views.feedbacks, name='messages'),
    path('export_feedbacks/', views.export_feedbacks, name='export_feedbacks'),
    path('delete_feedback/<int:pk>/', views.delete_feedback, name='delete_feedback'),

    path('premiums/', views.premium, name="premium"),
    path('computepremiumform', views.premiumform, name="premiumform"),
    path('vehiclepremiumdetails/<int:record_id>/', views.premiumrecord_detail, name='premiumrecord_detail'),
    path('searchallpremiums', views.searchallpremium, name='searchallpremium'),
    path('premium/<int:pk>/', views.computedpremium, name='computedpremium'),
    path('premium/update/<int:pk>/', views.update_premium, name='update_premium'),
    path('delete_premium/<int:pk>/', views.delete_premium, name='delete_premium'),
    path('allpremiums/', views.allpremium, name="allpremium"),
    path('paidpremiums', views.paidpremium, name="paidpremium"),
    path('unpaidpremiums', views.unpaidpremium, name="unpaidpremium"),
    path('partpaidpremiums', views.partpaidpremium, name="partpaidpremium"),
    path('cashpayments', views.cashpayment, name="cashpayment"),
    path('salarydeductionpayments', views.salarydeduction, name="salarydeduction"),
    path('otherpaymentmethods', views.otherpayment, name="otherpayment"),
    path('premiumrefunds', views.premiumrefund, name="premiumrefund"),
    path('comprehensivecoverpremiums', views.comprehensivepremium, name="comprehensivepremium"),
    path('thirdpartycoverpremiums', views.thirdpartypremium, name="thirdpartypremium"),
    path('export_premiums/', views.export_premiums, name='export_premiums'),
    path('export_cash_payments/', views.export_cash_payments, name='export_cash_payments'),
    path('export_salary_deductions/', views.export_salary_deductions, name='export_salary_deductions'),
    path('export_other_payments/', views.export_other_payments, name='export_other_payments'),
    path('export_paid_premiums/', views.export_paid_premiums, name='export_paid_premiums'),
    path('export_unpaid_premiums/', views.export_unpaid_premiums, name='export_unpaid_premiums'),
    path('export_partpaid_premiums/', views.export_partpaid_premiums, name='export_partpaid_premiums'),
    path('export_refunded_premiums/', views.export_refunded_premiums, name='export_refunded_premiums'),
    path('export_thirdparty_premiums/', views.export_thirdparty_premiums, name='export_thirdparty_premiums'),
    path('export_comprehensive_premiums/', views.export_comprehensive_premiums, name='export_comprehensive_premiums'),


    path('companymotorcovers', views.companyvehicle, name="companyvehicle"),
    path('requestcompanycoverform', views.companyvehicleform, name="companyvehicleform"),
    path('download-logbook2/<int:pk>/', views.download_logbook2, name='download_logbook2'),
    path('companyvehiclecoverdetails/<int:vehicle_id>/', views.companyrecord_detail, name='companyrecord_detail'),
    path('companyvehicle/update/<int:vehicle_id>/', views.update_company_vehicle, name='update_company_vehicle'),
    path('searchallcompanyvehicles', views.searchallcompanyvehicle, name='searchallcompanyvehicle'),
    path('delete_company_vehicle/<int:pk>/', views.delete_company_vehicle, name='delete_company_vehicle'),
    path('allcompanycovers/', views.allcompanyvehicle, name="allcompanyvehicle"),
    path('absentcompanycovers', views.absentcompanyvehicle, name="absentcompanyvehicle"),
    path('activecompanycovers', views.activecompanyvehicle, name="activecompanyvehicle"),
    path('cancelledcompanycovers', views.cancelledcompanyvehicle, name="cancelledcompanyvehicle"),
    path('export_active_company_vehicles/', views.export_active_company_vehicles, name='export_active_company_vehicles'),
    path('export_cancelled_company_vehicles/', views.export_cancelled_company_vehicles, name='export_cancelled_company_vehicles'),
    path('export-company-vehicles/', views.export_company_vehicles, name='export_company_vehicles'),
    path('export_absent_company_vehicles/', views.export_absent_company_vehicles, name='export_absent_company_vehicles'),
    

    path('staffmotorcovers', views.staffvehicle, name="staffvehicle"),
    path('requestcoverform', views.staffvehicleform, name="staffvehicleform"),
    path('vehiclecoverdetails/<int:vehicle_id>/', views.record_detail, name='record_detail'),
    path('downloadstaffvehiclelogbook/<int:pk>/', views.download_logbook, name='download_logbook'),
    path('update-vehicle/<int:vehicle_id>/', views.update_vehicle, name='update_vehicle'),
    path('staffvehicle/update/<int:vehicle_id>/', views.update_staff_vehicle, name='update_staff_vehicle'),
    path('searchallstaffvehicles', views.searchallstaffvehicle, name='searchallstaffvehicle'),
    path('delete_staff_vehicle/<int:pk>/', views.delete_staff_vehicle, name='delete_staff_vehicle'),
    path('allstaffcovers/', views.allstaffvehicle, name="allstaffvehicle"),
    path('absentstaffcovers', views.absentstaffvehicle, name="absentstaffvehicle"),
    path('activestaffcovers', views.activestaffvehicle, name="activestaffvehicle"),
    path('cancelledstaffcovers', views.cancelledstaffvehicle, name="cancelledstaffvehicle"),
    path('currentstaffcovers', views.currentstaffvehicle, name="currentstaffvehicle"),
    path('managerscovers', views.managervehicle, name="managervehicle"),
    path('exstaffcovers', views.exstaffvehicle, name="exstaffvehicle"),
    path('exmanagerscovers', views.exmanagervehicle, name="exmanagervehicle"),
    path('privatemotorcovers', views.privatevehicle, name="privatevehicle"),
    path('commercialmotorcovers', views.commercialvehicle, name="commercialvehicle"),
    path('comprehensivecovers', views.comprehensivecover, name="comprehensivecover"),
    path('thirdpartycovers', views.thirdpartycover, name="thirdpartycover"),
    path('export_absent_staff_vehicles/', views.export_absent_staff_vehicles, name='export_absent_staff_vehicles'),
    path('export-staff-vehicles/', views.export_staff_vehicles, name='export_staff_vehicles'),
    path('export_active_staff_vehicles/', views.export_active_staff_vehicles, name='export_active_staff_vehicles'),
    path('export_cancelled_staff_vehicles/', views.export_cancelled_staff_vehicles, name='export_cancelled_staff_vehicles'),
    path('export_current_staff_vehicles/', views.export_current_staff_vehicles, name='export_current_staff_vehicles'),
    path('export_managers_vehicles/', views.export_managers_vehicles, name='export_managers_vehicles'),
    path('export_ex_staff_vehicles/', views.export_ex_staff_vehicles, name='export_ex_staff_vehicles'),
    path('export_ex_managers_vehicles/', views.export_ex_managers_vehicles, name='export_ex_managers_vehicles'),
    path('export_private_vehicles/', views.export_private_vehicles, name='export_private_vehicles'),
    path('export_commercial_vehicles/', views.export_commercial_vehicles, name='export_commercial_vehicles'),
    path('export_comprehensive_vehicles/', views.export_comprehensive_vehicles, name='export_comprehensive_vehicles'),
    path('export_thirdparty_vehicles/', views.export_thirdparty_vehicles, name='export_thirdparty_vehicles'),

]