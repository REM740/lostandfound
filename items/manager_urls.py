from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.manager_login, name='manager_login'),
    path('dashboard/', views.manager_dashboard, name='manager_dashboard'),
    path('logout/', views.manager_logout, name='manager_logout'),

    path('add-lost-item/', views.add_lost_item, name='add_lost_item'),
    path('edit-lost-item/<int:id>/', views.edit_lost_item, name='edit_lost_item'),
    path('delete-lost-item/<int:id>/', views.delete_lost_item, name='delete_lost_item'),

    path('add-found-item/', views.add_found_item, name='add_found_item'),
    path('edit-found-item/<int:id>/', views.edit_found_item, name='edit_found_item'),
    path('delete-found-item/<int:id>/', views.delete_found_item, name='delete_found_item'),

    path('manage_lost_items/', views.manage_lost_items, name='manage_lost_items'),
    path('manage_found_items/', views.manage_found_items, name='manage_found_items'),

    path('mark-as-found/<int:id>/', views.mark_as_found, name='mark_as_found'),
]