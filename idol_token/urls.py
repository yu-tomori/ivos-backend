from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    path("", top, name = "top"),

    path("all_idol/", all_idol, name = "all_idol"),
    # To show the "Idol" page
    path("<int:idol_id>/", idol, name = "idol"),
    # path("idol_page/", idol_page, name = "idol_page"),
    #=========TEST=============
    # path("test/", test, name = "test"),
    path('index/', get_index, name='index'),
    path('idol/', get_idol, name='idol_detail'),
    path('register_idol/', register_idol, name = 'register_idol'),
    path('register_item/', register_item, name='register_item'),
    path('purchase_item/', purchase_item, name='purchase_item'),
    path('item/<int:pk>/', item_detail, name='item_detail' )
]
