######################## Utility methods ######################
import datetime
date = datetime.datetime.now().strftime('%Y')
#################  Dependecies for core app  ####################
from django.views import View
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password, check_password

def portaLogin(request):
	try:
		if request.method == 'GET': #serve login page
			if request.user.is_authenticated : #except if already logged_in
				return redirect('redirectLandingPage')
			else :
				context = {'message':'', 'error':'none', 'date':date}
				return render(request, "portalLogin.html", context)
		if request.method == 'POST': #validate user
			user = authenticate(username=request.POST.get('username'), password=request.POST.get('password') )
			if user is not None :
				login(request, user, backend=user.backend)
				requested_page = request.GET.get('next')
				if requested_page is not None :
					print(requested_page)
					return redirect(requested_page)
				else :
					return redirect('redirectLandingPage')

			deactivated = False
			try :
				User.objects.get(is_active=False, username=request.POST.get('username'))
				deactivated = True
			except Exception as e:
				print( str(e) )
				
			if deactivated:
				context = {'message' : 'User has been deactivated.', 'error':'visible', 'date':date}
				return render(request, 'portalLogin.html',  context)
			else:
				context = {'message' : 'Incorrect Username or Password.', 'error':'visible', 'date':date}
				return render(request, 'portalLogin.html',  context)


	except Exception as e: #catch any errors just to be extra safe.
		print(e)
		return redirect('landingPageRedirectlogin')
def portalLogout(request):
	from django.contrib.auth import logout
	logout(request)
	return redirect('landingPageLogin')
def redirectLandingPage(request):
	return render(request,'redirectLandingPage.html',{'date':date})
def generic500page(request,redirect_url):
	return render(request,'generic500page.html',{'redirect_url':redirect_url})