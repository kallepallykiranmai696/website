from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from website_app import views

urlpatterns = [
    path('web/', views.Web,name="web"),
    path('about/',views.About,name="about"),
    path('all course/',views.Course,name="all course"),
    path('call/',views.Call,name="call"),
    path('callus/',views.Callus,name="callus"),
    path('join/',views.Join,name="join"),
    path('contact/',views.Contact,name="contact"),
    path('getcall/',views.Getcall,name="getcall"),
    path('readmore',views.Readmore,name="readmore"),
    ]


