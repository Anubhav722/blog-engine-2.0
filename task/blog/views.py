from django.shortcuts import render, HttpResponse, get_list_or_404, get_object_or_404
from blog.models import Content, Content_Types

from django.db.models import Count
# Create your views here.
def index(request):
    queryset=Content.objects.all().values_list("title", flat=True).distinct()
    
    context={
        "queryset":queryset,
    }
    return render(request, "index.html", context)
    
def heading(request, title):
    
    instance_list=get_list_or_404(Content, title=title)
    instance=Content.objects.filter(title=title).values_list("sub_title", flat=True).distinct()
    #myset=set(instance_list)
    #print myset
    context={
        "title":title,
        "instance_list":instance_list,
        "instance":instance
        
    }
    return render(request, "heading.html", context)
    
def sub_titles(request, sub_title):
    
    instance_list=get_list_or_404(Content, sub_title=sub_title)
    
    instance=Content.objects.filter(sub_title=sub_title).select_subclasses()
    
   
    context={
        "instance":instance,
        "instance_list":instance_list
    }
    return render(request, "detail.html", context)
    