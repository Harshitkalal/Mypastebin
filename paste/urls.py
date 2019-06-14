from django.urls import path

from .import views



urlpatterns = [

    path('',views.home,name='home'),
    path('create',views.create,name='create'),
    path('allpaste',views.allpaste,name='allpaste'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('delete/<int:id>',views.pastedelete,name='pastedelete'),
    path('update/<int:id>',views.update,name='update'),
    path('edit/<int:id>',views.edit,name='edit'),
  #  path('',PasteCreate.as_view(),name='create'),
  #  path('paste/',pasteList.as_view(),name='pastebin_paste_list'),
 #   path('<paste/<int:pk>',PasteDetail.as_view(),name='pastebin_paste_detail'),
]
