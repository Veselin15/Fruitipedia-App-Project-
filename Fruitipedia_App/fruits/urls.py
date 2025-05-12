from django.contrib import admin
from django.urls import path, include
from .views import index, dashboard, create_fruit, details_fruit, edit_fruit, delete_fruit, create_category

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),

    path('create-fruit/', create_fruit, name='create_fruit'),
    path('<int:fruit_id>/', include([
        path('details-fruit/', details_fruit, name='details_fruit'),
        path('edit-fruit/', edit_fruit, name='edit_fruit'),
        path('delete-fruit/', delete_fruit, name='delete_fruit'),
    ])),
    path('create-category/', create_category, name='create_category'),

]