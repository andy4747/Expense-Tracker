from django.urls import path

#Import your views here
from . views import home
from . views import add_item
from . views import update_table
from . views import remove_items

urlpatterns = [
    path('',home,name='home'),
    path('add/',add_item,name='add'),
    path('update/',update_table,name='update'),
    path('remove/',remove_items, name='remove'),
]