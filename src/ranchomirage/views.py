from django.shortcuts import render
from django.core.context_processors import request
from django.template.context import RequestContext
from django.shortcuts import render_to_response, render

# Create your views here.
def index(request):
    context = RequestContext(request)
    return render_to_response('ranchomirage/index.html', context)
