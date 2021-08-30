from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required
urlpatterns = [
				path('',login_required(views.nMeetViewDashboard.as_view()),name='default'),
				path('login/',views.nMeetLogin,name='nMeetLogin'),
				path('logout/', login_required(views.nMeetLogout),name='nMeetLogout'),
				path('dashboard/',login_required(views.nMeetViewDashboard.as_view()),name='nMeetDashboard'),
				path('enterFigures/', login_required(views.nMeetEnterFigures.as_view()),name='nMeetEnterFigures'),
				path('chat/',login_required(views.nMeetChat.as_view()),name='nMeetChat'),
				path('refreshChat/',login_required(views.refreshChat),name='nMeetRefreshChat'),
				path('clearDashboard/',login_required(views.nMeetClearDashboard),name='nMeetClearDashboard'),
				path('nMeetClearChat/',login_required(views.nMeetClearChat),name='nMeetClearChat'),
				path('saveDashboard/',login_required(views.nMeetSaveDashboard),name='nMeetSaveDashboard'),
                path('cancelFigs/',login_required(views.nMeetCancelFigs.as_view()),name="nMeetCancelFigs"),
                path('upload_summary_file',login_required(views.nMeet_upload_summary_file),name="nMeet_upload_summary_file"),
                path('nMeetDeletedMessages',login_required(views.get_deleted_messages),name="nMeetDeletedMessages"),
                path('nMeetDeleteMessage', login_required(views.deleteMessage),name="nMeetDeleteMessage"),
			]