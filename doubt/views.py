from django.shortcuts import render,HttpResponse,redirect
from .models import contact,doubts_data,comments
from django.contrib import messages


# Create your views here.
def homepage(request):
    return render(request,'doubt/home.html')

def about(request):
    return render(request,'doubt/about.html')

def contacts(request):
    if request.method=='POST':
        data=contact()
        data.email=request.POST.get('email')
        data.query=request.POST.get('query')
        data.save()
        messages.info(request,'Thank You for contacting us.')
        return  redirect('/contact')
    else:
        return render(request,'doubt/contact.html')

def doubt(request):
    data_ = doubts_data()
    if request.method == 'POST':
        data_ = doubts_data()
        data_.doubt_text = request.POST.get('text')
        data_.doubt_file = request.POST.get('file')
        data_.doubt_language=request.POST.get('lang')
        data_.doubt_code=request.POST.get('code')
        data_.title=request.POST.get('title')
        data_.author=str(request.user)
        data_.save()
        data_.slug = slug_creator(data_.title,data_.id)
        data_.save()
        messages.success(request, 'Doubt Submitted')
        return redirect('/doubt')
    else:
        posts=doubts_data.objects.all()
        return render(request,'doubt/doubt.html',{'posts':posts})

def doubt_view(request,slug):
    query=doubts_data.objects.filter(slug=slug)
    comment=comments.objects.filter(post=doubts_data.objects.filter(slug=slug).first())
    return render(request,'doubt/doubt_view.html',{'queryset':query ,'comments':comment})

def slug_creator(value,id__):
    new_slug=''
    slug=value.lower()
    for char in slug:
        if char == ' ':
            new_slug=new_slug+'-'
        else:
            new_slug=new_slug+char
    new_slug+=str(id__)
    return new_slug

def answers(request):
    data=comments()
    data.comment = request.POST.get('comment')
    data.user=request.user
    #comment.parent = request.POST.get('comment')
    postid=request.POST.get('postid')
    data.post = doubts_data.objects.get(id=postid)
    data.save()
    messages.success(request,'Answer Submitted')
    slug=request.POST.get('slug')
    print(slug)
    return redirect('/doubt_view/'+slug)

def search(request):
    query=request.GET['search']
    if query == 'user':
        result_author = doubts_data.objects.filter(author__icontains=str(request.user))
    else :
        result_author = doubts_data.objects.filter(author__icontains=query)
    result_language = doubts_data.objects.filter(doubt_language__icontains=query)
    result_title = doubts_data.objects.filter(title__icontains=query)
    result_code = doubts_data.objects.filter(doubt_code__icontains=query)
    result_text = doubts_data.objects.filter(doubt_text__icontains=query)
    result = result_title.union(result_code, result_text, result_language, result_author)
    return render(request,'doubt/search.html',{'posts':result,'query':query})