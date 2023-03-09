from django.urls import path
from apps import views


urlpatterns =[

    path('index/', views.index, name="index"),
    path('newpage/',views.newpage, name="newpage"),
    path('savedata/',views.savedata,name="savedata"),
    path('displaypage/',views.displaypage,name="displaypage"),
    path('newadmin/',views.newadmin,name="newadmin"),
    path('newsave/',views.newsave,name="newsave"),
    path('admindisplay/',views.admindisplay,name="admindisplay"),
    path('editadminpage/<int:dataid>/',views.editadminpage,name="editadminpage"),
    path('updateadmin/<int:dataid>/',views.updateadmin,name="updateadmin"),
    path('deleteadmin/<int:dataid>/',views.deleteadmin,name="deleteadmin"),
    path('logadmin/',views.logadmin,name="logadmin"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('adminlogout/',views.adminlogout,name="adminlogout"),
    path('newhi/',views.newhi,name="newhi")
    ]