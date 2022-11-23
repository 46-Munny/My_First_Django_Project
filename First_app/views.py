from django.shortcuts import render
from django.http import HttpResponse
from First_app.models import Musician,Album
from First_app import forms
from django.db.models import Avg

# Create your views here.
def index(request):
    musician_list=Musician.objects.order_by('first_name')

    diction={'text1':'This is a list of musician', 'musician':musician_list}
    return render(request,'First_app/index.html',context=diction)


def form(request):
    new_form=forms.user_form()
    diction={'test_form':new_form, 'heading':'This form is created using django library'}

    if request.method=='POST':
        new_form=forms.user_form(request.POST)
        diction.update({'test_form':new_form})

        if new_form.is_valid():
            u_name=new_form.cleaned_data['user_name']
            u_dob=new_form.cleaned_data['user_dob']
            u_email=new_form.cleaned_data['user_email']
            b_field=new_form.cleaned_data['boolean_field']
            d_menu=new_form.cleaned_data['dropdown_Menu']
            r_button=new_form.cleaned_data['radio_button']
            d_menu_multiple=new_form.cleaned_data['dropdown_Menu_multiple']
            c_multiple=new_form.cleaned_data['checkbox_multiple']

            diction.update({'uname':u_name})
            diction.update({'udob':u_dob})
            diction.update({'uemail':u_email})
            diction.update({'form_submitted':'yes'})
            diction.update({'bfield':b_field})
            diction.update({'dmenu':d_menu})
            diction.update({'rbutton':r_button})
            diction.update({'dmenuMultiple':d_menu_multiple})
            diction.update({'cmultiple':c_multiple})




    return render(request,'First_app/form.html',context=diction)



def form2(request):
    new_form=forms.MusicianForm()
    if request.method=='POST':
        new_form=forms.MusicianForm(request.POST)


        if new_form.is_valid():
            new_form.save(commit=True)
            return index(request) #After submit form redirect in index.html page
    diction={'test_form':new_form, 'heading':'This form is created using django library'}
    return render(request,'First_app/form2.html',context=diction)




def index2(request):
    musician_list=Musician.objects.order_by('first_name')
    diction={'title':"Home page","musician_list":musician_list}
    return render(request,'First_app/index2.html',context=diction)

def album_list(request, artistId):
    artist_info=Musician.objects.get(pk=artistId)
    album_list=Album.objects.filter(artist=artistId).order_by('name','release_date')
    artist_rating=Album.objects.filter(artist=artistId).aggregate(Avg('num_stars'))
    diction={'title':"List of albums", 'artist_info':artist_info, 'album_list':album_list,'artist_rating':artist_rating}
    return render(request,'First_app/album_list.html',context=diction)

def musician_form(request):
    form=forms.MusicianForm()

    if request.method=="POST":
        form=forms.MusicianForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index2(request)


    diction={'title':"Add musician" ,"musician_form":form}
    return render(request,'First_app/musician_form.html',context=diction)

def album_form(request):
    form=forms.AlbumForm()

    if request.method=="POST":
        form=forms.AlbumForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index2(request)
    diction={'title':"Add album","album_form":form}
    return render(request,'First_app/album_form.html',context=diction)


def edit_artist(request,artist_id):
    artist_info=Musician.objects.get(pk=artist_id)
    form=forms.MusicianForm(instance=artist_info)
    if request.method=="POST":
        form=forms.MusicianForm(request.POST,instance=artist_info)

        if form.is_valid():
            form.save(commit=True)
            return album_list(request,artist_id)
    diction={'edit_form':form}
    return render(request,'First_app/edit_artist.html',context=diction)


def edit_album(request,album_id):
    album_info=Album.objects.get(pk=album_id)
    form=forms.AlbumForm(instance=album_info)
    if request.method=="POST":
        form=forms.AlbumForm(request.POST,instance=album_info)

        if form.is_valid():
            form.save(commit=True)
            return album_list(request,album_id)
    diction={'edit_form':form}
    diction.update({'album_id':album_id})
    return render(request,'First_app/edit_album.html',context=diction)

def delete_album(request,albumId):
    album_del=Album.objects.get(pk=albumId).delete()
    diction={'delete_msg':'delete album successfully'}


    return render(request,'First_app/delete_album.html',context=diction)
