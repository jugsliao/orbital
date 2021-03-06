from django.urls import path
from . import views

app_name = "traininglog"

urlpatterns = [
    path('', views.home, name='home'),
    path('newlog1/', views.newlog1, name='newlog1'),
    path('editlog/<int:log_id>', views.editlog, name='editlog'),
    path('deletelog/<int:log_id>', views.deletelog, name='deletelog'),
    path('logs/', views.LogsView.as_view(), name='logs'),
    path('logs/<int:log_id>', views.log, name='log'),
]