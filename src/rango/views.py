from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, render
from django.template.context import RequestContext

from rango.forms import CategoryForm, PageForm, UserProfileForm, UserForm, \
    LoginForm
from rango.models import Category, Page


def index(request):
    context = RequestContext(request)
    #===========================================================================
    # context_dict = {'boldmessage' : "I am a bold font from the context",
    #                 'name' : "My name is Borg",}
    #===========================================================================
    category_list = Category.objects.order_by('name')
    context_dict = {'categories' : category_list}
    
    most_viewed = Page.objects.order_by('-views')[:5]
    context_dict['most_viewed'] = most_viewed
    
    return render_to_response('rango/index.html', context_dict, context)
    #===========================================================================
    # 'return HttpResponse("Rango says hello world! <a href='/rango/about'>About</a>")
    #===========================================================================

def about(request):
    context = RequestContext(request)
    return render_to_response('rango/about.html', context)
    #===========================================================================
    # return HttpResponse("Rango Says: Here is the about page. <a href='/rango'>Home</a>")
    #===========================================================================
    
def category(request, category_name_url):
    context =RequestContext(request)
    
    category_name = category_name_url.replace('_', ' ')
    context_dict = {'category_name' : category_name,
                    'category_name_url' : category_name_url}
    
    try:
        category = Category.objects.get(name=category_name)
        context_dict['category'] = category

        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        
    except Category.DoesNotExist:
        pass

    return render_to_response('rango/category.html', context_dict, context)

def add_category(request):
    context = RequestContext(request)
    
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = CategoryForm()
        
    return render_to_response('rango/add_category.html', {'form' : form}, context)

def add_page(request, category_name_url):
    context = RequestContext(request)
    
    category_name = category_name_url;
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            page = form.save(commit=False)
            try:
                cat = Category.objects.get(name=category_name)
                page.category = cat
            except Category.DoesNotExist:
                return render_to_response('rango/add_category.html', {}, context)
            
            page.views = 0
            page.save()
            return category(request, category_name_url)
        else:
            print form.errors
        
    else:
        form = PageForm()
    
    return render_to_response( 'rango/add_page.html',
        {'category_name_url': category_name_url,
         'category_name': category_name, 'form' : form},
        context)
        
def register(request):
    registered = False
    
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors         
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()  
        
    return render(request,
                  'rango/register.html',
                  {'user_form' : user_form, 'profile_form' : profile_form, 'registered' : registered})
    
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/rango/')
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print "Invalid Login details: {0}, {1}".format(username, password)
            #return HttpResponse("Invalid login details supplied.")
            return render(request, 'rango/login.html', {'login_error' : "Your userName and/or password is incorrect."})
    else:
        return render(request, 'rango/login.html', {})
        

def user_login_form(request):
    if request.method == 'POST':
        user_login_form = LoginForm(data=request.POST)
        
        if user_login_form.is_valid():
            user = authenticate(username=user_login_form.cleaned_data['username'], password=user_login_form.cleaned_data['password'])
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/rango/')
                else:
                    return HttpResponse("Your Rango account is disabled.")
            else:
                return render(request, 'rango/login1.html', {'user_login_form' : user_login_form, 'login_error' : "Your userName and/or password is incorrect."})
        else:
            print user_login_form.errors
             
    else:
        user_login_form = LoginForm()
         
    return render(request, 'rango/login1.html', {'user_login_form' : user_login_form})              

@login_required      
def restricted(request):
    return render(request, 'rango/restricted.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/rango/')
    