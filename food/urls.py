from django.urls import path
from food import views
app_name='food'
urlpatterns = [
    path('',views.index,name='idex'),
    path('item/',views.item,name='item'),
    path('<int:item_id>/',views.details,name='detail'),
    path('add/',views.creatitem.as_view(),name='create'),
    path('update/<int:item_id>/',views.update_item,name='update'),
    path('delet/<int:item_id>/',views.delete_item,name='delete')
]
