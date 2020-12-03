from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create', views.create),
    path('create_show', views.add_show),
    path('display_show/<int:show_id>', views.display_show),
    path('delete/<int:show_id>', views.delete),
    path('edit_show/<int:show_id>', views.edit),
    path('update_show/<int:show_id>', views.update),
]



