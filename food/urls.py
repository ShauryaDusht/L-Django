from . import views # import views from current directory
from django.urls import path

app_name = 'food'

urlpatterns = [
    # class based view
    path('',views.IndexClassView.as_view(),name='index'), 
    path('index/',views.IndexClassView.as_view(),name='index'),
    path('<int:pk>/', views.FoodDetail.as_view(), name='detail'), # pk means primary key
    path('add/', views.CreateItem.as_view(), name='create_item'),
    path('update/<int:pk>/', views.UpdateItem.as_view(), name='update_item'),
    path('delete/<int:pk>/', views.DeleteItem.as_view(), name='delete_item'),
    
    
    # function based view
    # path('', views.index, name='index'),
    # path('index/', views.index, name='index'),
    # path('item/', views.item, name='item'),
    # path('<int:item_id>/', views.detail, name='detail'),
    # path('add/', views.create_item, name='create_item'),
    # path('update/<int:item_id>/', views.update_item, name='update_item'),
    # path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
]
