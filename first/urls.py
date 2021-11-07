from django.contrib import admin
from django.urls import path, include
from .views import RegisterView, LoginView
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('user/register/',RegisterView.as_view(),name='Register a User'),
    path('user/login/',LoginView.as_view(),name='Login a User'),
    path('admin/advisor/',views.addAdvisor, name="addAdvisor"),
    path('user/<userid>/advisor/',views.showAdvisor, name="showAdvisor"),
    path('user/<userid>/advisor/<advisorid>/', views.bookAdvisor, name="bookAdvisor"),
    path('user/advisor/booking/', views.showBooking,name="showBooking"),
]

'''
urlpatterns = [
    path('user/<userid>/advisor/<advisorid>/', views.bookAdvisor, name="bookAdvisor"),
    path('user/advisor/booking/', views.showBooking,name="showBooking"),
    
]
'''