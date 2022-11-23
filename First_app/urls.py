from django.conf.urls import url
from django.urls import path
from First_app import views

app_name="First_app"

urlpatterns = [
    path('',views.index,name="index" ),
    path('form/',views.form,name="form" ),
    path('form2/',views.form2,name="form2" ),
    path('index2/',views.index2,name="index2" ),
    path('add_album/',views.album_form,name="album_form" ),
    path('add_musician/',views.musician_form,name="musician_form" ),
    path('album_list/<int:artistId>',views.album_list,name="album_list" ),
    path('edit_artist/<int:artist_id>',views.edit_artist,name="edit_artist" ),
    path('edit_album/<int:album_id>',views.edit_album,name="edit_album" ),
    path('delete_album/<int:albumId>',views.delete_album,name="delete_album" ),




]
