from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('regimens/', views.regimens_index, name='index'),
    path('regimens/<int:regimen_id>/', views.regimens_detail, name='detail'),
    path('regimens/create/', views.RegimenCreate.as_view(), name='regimens_create'),
    path('regimens/<int:pk>/update/', views.RegimenUpdate.as_view(), name='regimens_update'),
    path('regimens/<int:pk>/delete/', views.RegimenDelete.as_view(), name='regimens_delete'),
    path('regimens/<int:regimen_id>/add_doing/', views.add_doing, name='add_doing'),
    path('regimens/<int:regimen_id>/assoc_exercise/<int:exercise_id>/', views.assoc_exercise, name='assoc_exercise'),
    path('regimens/<int:regimen_id>/assoc_exercise/<int:exercise_id>/delete/', views.assoc_exercise_delete, name='assoc_exercise_delete'),
    path('exercises/', views.exercises_index, name='exercises_index'),
    path('exercises/<int:pk>/', views.ExerciseDetail.as_view(), name='exercises_detail'),
    path('exercises/create/', views.ExerciseCreate.as_view(), name='exercises_create'),
    path('exercises/<int:pk>/update/', views.ExerciseUpdate.as_view(), name='exercises_update'),
    path('exercises/<int:pk>/delete/', views.ExerciseDelete.as_view(), name='exercises_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]
