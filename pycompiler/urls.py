
from django.urls import path, include

# import views

from . import views

urlpatterns = [
    path('', views.index, name="indexpage"),
    path('runcode', views.runcode, name="runcode"),
    path('submitcode', views.submitcode),
    path('submitgg', views.submitgg),
    path('login', views.login_page),
    path('register-student/', views.registerstu),
    path('register-faculty/', views.registerfac)

    # path('save', views.save)
]