from django.urls import path
from backend import views


urlpatterns =[
    path('homepage/',views.homepage,name="homepage"),
    path('about/',views.about,name="about"),
    path('productdis/', views.productdis, name="productdis"),
    path('singledis/',views.singledis,name="singledis"),
    path('regipage/',views.regipage,name="regipage"),
    path('loginpage/',views.loginpage,name="loginpage"),
    # path('productdis/<itemCatg',views.productdis,name="productdis")
]