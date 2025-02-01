
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Index , name="Index"),
    path("contact/<int:id>/", views.Contact1, name="contact"),
    path("contact1/<str:id>/", views.Contact2, name="contact1"),
   path("contact2/<slug:id>/", views.Contact2, name='contact2'),
    path("contact3/<slug:course>/", views.Contact3, name="contact3"),
    path("contact3/<course>/", views.Contact4, name="contact4"),
    




    
]
