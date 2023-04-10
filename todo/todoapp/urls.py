from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    path('',views.home,name="home"),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbv/',views.tasklistview.as_view(),name='cbv'),
    path('cbv/<int:pk>/',views.detailview.as_view(),name='detailview'),
    path('cbvupdate/<int:pk>/',views.updateview.as_view(),name='updateview'),
    path('cbvdelete/<int:pk>/',views.deleteview.as_view(),name='deleteview')
]