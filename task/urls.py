from django.urls import path
from task import views

urlpatterns = [
path('',views.index,name="index"),
path('<int:id>',views.edit,name="edit"),
path('edit/<int:id>',views.edit,name="edit"),

]
