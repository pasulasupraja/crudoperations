from django.urls import path
from crud import views
urlpatterns = [
    path('',views.crud),
    path('about/',views.about,name='about'),
    path('insert/',views.insertdata,name='insert'),
    path('update/<id>',views.updateData,name='updataData'),
    path('delete/<id>',views.deleteData,name='deleteData'),
]
