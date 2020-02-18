from django.urls import path

from . import views

urlpatterns = [
    path('', views.members, name='members'),
    path('<int:member_id>', views.individual_member, name='individual_member'),
    path('<int:member_id>/edit', views.edit_profile, name='edit_profile'),
    path('<int:member_id>/profile', views.view_profile, name='view_profile'),
    path('<int:member_id>/pic/add', views.add_pic, name='add_pic'),
    path('pic/<int:member_pic_id>/edit', views.edit_pic, name='edit_pic'),
    path('pic/<int:member_pic_id>/delete', views.delete_pic, name='delete_pic'),
    path('csv/', views.export_csv, name='export_csv'),
]