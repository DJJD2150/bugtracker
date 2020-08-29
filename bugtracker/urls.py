"""bugtracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bugtracker_app import views

urlpatterns = [
    path('', views.index_view, name="homepage"),
    path('ticket/<int:ticket_id>/edit/', views.ticket_edit_view),
    path('ticket/<int:ticket_id>', views.ticket_view, name="ticket_view"),
    path('newticket/', views.create_ticket_view, name="create_ticket_view"),
    path('username/<int:user_id>/edit/', views.user_edit_view),
    path('username/<int:user_id>', views.user_view, name="user_view"),
    # path('newuser/', views.create_user_view, name="create_user_view"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('admin/', admin.site.urls),
]
