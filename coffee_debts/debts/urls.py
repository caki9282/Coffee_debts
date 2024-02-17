from django.urls import path
from . import views
from .views import SignUpView
from .views import add_coffee_purchase
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import home_page
from .views import add_coffee_purchase
from .views import coffee_debt_summary
from .views import add_coffee_costs
# from .views import batch_add_coffee_purchases

urlpatterns = [

    path('signup/', SignUpView.as_view(), name='signup'),

    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('home/', home_page, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('about/', views.add_coffee_costs, name='about'),
    path('debts/', views.list_debts, name='list_debts'),
    path('add-coffee/', views.add_coffee_purchase, name='add_coffee'),
    path('coffee-debt-summary/', coffee_debt_summary, name='coffee_debt_summary'),
    path('add-coffee-costs/', views.add_coffee_costs, name='add_coffee_costs'),

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
