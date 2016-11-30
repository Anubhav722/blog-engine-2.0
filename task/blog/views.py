from django.shortcuts import render, HttpResponse, get_list_or_404, get_object_or_404
from blog.models import Content, Content_Types

from django.db.models import Count

from django.db.models import Q
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
    object_list=Content.objects.filter(title=title).select_subclasses()
    
    extra_value=Content_Types.objects.filter(title=title)
    query=request.GET.get('query')
    if query:
        object_list=extra_value.filter(
            Q(element__icontains=query) |
            Q(content__icontains=query) |
            Q()
            
            )
    context={
        "title":title,
        "instance_list":instance_list,
        "instance":instance,
        "object_list":object_list,
        
    }
    return render(request, "heading.html", context)
    
def sub_titles(request, sub_title):
    
    instance_list=get_list_or_404(Content, sub_title=sub_title)
    
    instance=Content.objects.filter(sub_title=sub_title).select_subclasses()
    extra_value=Content_Types.objects.filter(sub_title=sub_title)
    """for x in instance:
        x.content
        x.element
        x.content
        x.element"""
    query=request.GET.get('query')
    """if query:
        instance=instance.filter(
            Q(title__icontains=query) | 
            Q(sub_title__icontains=query)
            )"""
            
    if query:
        instance=extra_value.filter(
            Q(element__icontains=query) |
            Q(content__icontains=query)
            )
        
        
   
    context={
        "instance":instance,
        "instance_list":instance_list
    }
    return render(request, "detail.html", context)
    