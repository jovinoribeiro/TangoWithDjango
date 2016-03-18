

from random import randint

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView

from leialater.forms import UserForm, BookmarkForm
from leialater.models import Category, Bookmark

def launcher(request, new_crid=None):
    context = RequestContext(request)
    context_dict = {'new_crid' : new_crid}
    return render_to_response('leialater/launcher.html', context_dict, context)

def new_crid(request):
    env = request.POST['env']
    redirect_url = reverse('launcher', kwargs={'new_crid' : randint(100, 1000)})
    return HttpResponseRedirect(redirect_url)

class UpdateBookmarkView(UpdateView):
    model = Bookmark
    template_name = 'edit_bookmark.html'
    
    def get_success_url(self):
        return reverse('bookmark_list')

class BookmarkView(ListView):
    model = Bookmark
    template_name = 'bookmark_list.html'

def index(request):
    context = RequestContext(request)
    category_list = Category.objects.order_by('name')
    context_dict = {'category_list' : category_list}
    return render_to_response('leialater/index.html', context_dict, context)

def dashboard(request):
    context = RequestContext(request)
    #Fetch 1st ten existing posts
    bookmark_list = Bookmark.objects.order_by('-date')
    context_dict = {'bookmark_list' : bookmark_list}
    return render_to_response('leialater/dashboard.html', context_dict, context)

def register(request):
    registered = False
     
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            
            user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request, user)
            return HttpResponseRedirect('/leialater/dashboard/')
        else:
            print user_form.errors         
    else:
        user_form = UserForm()
         
    return render(request,
                  'leialater/register.html',
                  {'user_form' : user_form, 'registered' : registered})
     
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
         
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/leialater/dashboard/')
            else:
                return HttpResponse("Your Account is disabled.")
        else:
            print "Invalid Login details: {0}, {1}".format(username, password)
            #return HttpResponse("Invalid login details supplied.")
            return render(request, 'leialater/login.html', {'login_error' : "Your userName and/or password is incorrect."})
    else:
        return render(request, 'leialater/login.html', {})
         
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/leialater/')

def add_url(request, bk_id=None):
    context = RequestContext(request)
    if request.method == 'POST':
        form = BookmarkForm(request.POST)
        if form.is_valid():
            bookmark = form.save(commit=False)
            try:
                cat = Category.objects.get(name="Undefined")
                bookmark.category = cat
            except Category.DoesNotExist:
                return render_to_response('leialater/add_url.html', {}, context)
            
            bookmark.save()
            return dashboard(request)
        else:
            print form.errors
    else:
        if bk_id is None:
            form = BookmarkForm()
        else:
            bookmark = Bookmark.objects.get(id=bk_id)
            form = BookmarkForm(instance=bookmark)
            
        
    return render_to_response( 'leialater/add_url.html',
        {'form' : form}, context)    
    
    

