from django.shortcuts import render,HttpResponse, get_object_or_404,HttpResponseRedirect,redirect,Http404
from.models import Post, Comment,Category,HomeImage
from .forms import PostForm, CommentForm,CategoryForm,HomeForm
from django.contrib import messages
from django.utils.text import slugify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib.auth.models import User


# Create your views here.

def post_create(request):
    if not request.user.is_authenticated:
        return Http404
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # Post.objects.create(title=title, content=content)

    # if request.method == 'POST':
    #     form = PostForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     else:
    #         form = PostForm()
    
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        post = form.save(commit=False)
        print(post)
        post.user = request.user
        post.save()
        messages.success(request, 'Post yuklediniz!')
        return HttpResponseRedirect(post.get_absolute_url())

    return render(request,'post/form.html', {'form':form})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.name = request.user.get_full_name()
        comment.user = request.user
        comment.post = post
        comment.save()
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'post':post,
        'form':form,
        }

    return render(request, 'post/details.html', context)

def post_update(request, slug):
    if not request.user.is_authenticated:
        return Http404

    post = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None,request.FILES or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, 'Post yenilediniz!')

        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form':form
    }
    return render(request, 'post/form.html', context)

    

def post_index(request):
    post_list = Post.objects.all().filter(visibility=True)
    query = request.GET.get('q')
    # print(query)
    if query:
        post_list = post_list.filter(
            Q(title__icontains=query)|
            Q(content__icontains=query)|
            Q(user__first_name__icontains=query)
        ).distinct()


    paginator = Paginator(post_list, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)
    return render(request, 'post/index.html', {'posts':posts})

def post_delete(request, slug):
    if not request.user.is_authenticated:
        return Http404

    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect('post:index')

def home_view(request):
    show_cat = Category.objects.all().filter(home_show=True)
    hide_cat = Category.objects.all().filter(home_show=False)
    images = HomeImage.objects.all()
    for i in images:
        if i == HomeImage.objects.first():
            i.number = 1
            i.save()
    context = {'showed':show_cat,'hidden':hide_cat,'images':images,'counter':0}
    return render(request, 'home.html', context)

def about_view(request):
    return render(request, 'about.html')

def comment_delete(request, commentid):
    comment = get_object_or_404(Comment, id=commentid)
    comment.delete()
    return redirect('post:index')


def category_list(request):
    all_categories = Category.objects.all
    return render (request,'post/category.html',{'categories':all_categories})

# def category_basehtml(request):
#     show_cat = Category.objects.all().filter(home_show=True)
#     hide_cat = Category.objects.all().filter(home_show=False)
#     print('------------------------ ------------------------')
#     return render(request,'header.html',{'showed':show_cat})

def category(request,categoryid):
    category = get_object_or_404(Category, id=categoryid)
    category_objects = category.post_set.all()
    return render (request, 'post/categorydetail.html',{'category':category_objects})

def category_create(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request,'post/form.html',{'form':form})


def category_delete(request,categoryid):
    category = get_object_or_404(Category,id=categoryid)
    category.delete()
    return redirect ('post:categorylist')


def change_visiblity(request,postid):
    post = Post.objects.get(id=postid)
    if post.user == request.user:
        if post.visibility == True:
            post.visibility = False
            post.save()
        else:
            post.visibility = True
            post.save()
    return redirect ('profile:profil')

def arxiv_postlar(request):
    user = request.user
    posts = user.post_set.all().filter(visibility=False)
    print(posts)
    return render (request,'post/notvisibility.html',{"posts":posts})

def home_image_create(request):
    if not request.user.is_superuser:
        return Http404
    form = HomeForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
    return render(request,'post/form.html',{'form':form,'ad':'Şəkil əlavə et'})







# def comment_update(request,commentid):
#     comment = get_object_or_404(Comment,id=commentid)
#     form = CommentForm(request.POST or None, request.FILES or None, instance=comment)
#     if form.is_valid():
#         form.save()
#         return render(request, 'post/comment.html',{'form':form})