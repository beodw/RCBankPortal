from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views


urlpatterns = [
				path('',views.asset_login),
				path('login/',views.asset_login,name='login'),
				path('viewAllAssets/', login_required ( views.View_all_assets.as_view() ), name='view_all_assets'),
				path('viewAllAssets/<str:message>/<str:error>/<str:success>/', login_required ( views.View_all_assets.as_view() ), name='view_all_assets_success'),
				path('viewAsset/<int:id>/<str:type>/', login_required ( views.View_asset.as_view() ), name='view_asset'),
				path('suppliedHardware/', login_required ( views.Supplied_hardware.as_view() ), name='supplied_hardware'),
				path('manageUsers/', login_required ( views.Manage_users.as_view() ), name='manage_users'),
				path('supplyDetails/<int:id>/', login_required ( views.Supply_details.as_view() ), name='supply_details'),
				path('createSupply/', login_required( views.Create_supply.as_view() ), name='create_supply'),
				path('printSupply/', login_required( views.Supply_details.print_supply ), name="print_supply"),
				path('genReport/', login_required(views.Supplied_hardware.gen_report) ,name="gen_report"),
                path('logout/', views.asset_logout,name="aMgntLogout"),
                path('delete_hardware/', login_required(views.delete_hardware), name="delete_hardware"),
                path('generalIncidents/',login_required(views.aMgntGeneralIncidents.as_view()), name="aMgntGeneralIncidents"),
                path('updateIncident/',login_required(views.aMgntGeneralIncidents.updateIncident),name="aMgntUpdateIncident"),
                path('getIncidents/',login_required(views.aMgntGeneralIncidents.get_incidents),name="aMgntGetIncidents"),
                path('incident/<int:incidentId>/',login_required(views.aMgntGeneralIncident.as_view()),name="aMgntGeneralIncident"),
                path('deleteIncident/',login_required(views.aMgntGeneralIncident.delete_incident),name='aMgntDeleteIncident'),
                path('scanQR-Code/',login_required(views.aMgntQRScanner.as_view()),name='aMgntQRScanner'),
                path('aMgntViewAllAssetsTable/',login_required(views.View_all_assets.aMgntViewAllAssetsTable),name="aMgntViewAllAssetsTable"),
			]

from django.urls import re_path

urlpatterns += [
    re_path(r'^accounts/login/', views.asset_login, name='login'),
    # re_path(r'^viewAllAssets/?(?P<message>[\W\w]*)', login_required ( views.View_all_assets.as_view() ), name='view_all_assets_error'),

    #re_path(r'logout', views.asset_logout, name='logout'),
]
