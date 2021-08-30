from . import views
from django.urls import path, include
from django.contrib.auth.decorators import login_required

urlpatterns = [
				# path('',login_required(views.addRecord),name='default'),
				path('addRecord/',login_required(views.sMntAddRecord),name='sMntAddRecord'),
				path('sMntDashboard/',login_required(views.sMntDashboard.as_view()),name='sMntDashboard'),
				path('cancelStatements/',login_required(views.sMntCancelStatments),name="sMntCancelStatments"),
				path('genReport/',login_required(views.sMntGenReport),name="sMntGenReport"),
				path('setQuantity/',login_required(views.sMntSetQuantity),name="sMntSetQuantity"),
                		path('sMntSearch/',login_required(views.sMntSearch),name="sMntSearch"),
				path('sMntDelSmnt', login_required(views.sMntDelSmnt.as_view()),name="sMntDelSmnt"),
			]

from django.urls import re_path
# urlpatterns += [
    # re_path(r'^accounts/login/', views.asset_login, name='login'),
    # re_path(r'logout', views.asset_logout, name='logout'),
# ]
