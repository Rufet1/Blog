from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey('auth.User', verbose_name = 'Yazar', on_delete=models.CASCADE,)
    category = models.ForeignKey('post.Category',on_delete=models.SET_NULL, null=True, blank=True)
    visibility = models.BooleanField(default=True)
    title = models.CharField(max_length=120)
    content = RichTextField(null=True,blank=True)
    publishing_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(unique=True,editable=False, max_length=130)

    def __str__(self):
        return self.title

    def get_like_url(self):
        return reverse("post:like", kwargs={"id": self.id})
    
    def get_absolute_url(self):
        return reverse("post:detail", kwargs={"id": self.id})
        # return '/post/{}'.format(self.id)
    def get_create_url(self):
        return reverse("post:create",)
    def get_update_url(self):
        return reverse("post:update", kwargs={"id": self.id})
    def get_delete_url(self):
        return reverse("post:delete", kwargs={"id": self.id})
    def get_visibility_url(self):
        return reverse('post:visibility', kwargs={"postid":self.id})
        
    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı','i').replace('ə','e').replace('ü','u').replace('ö','o').replace('ğ','g').replace('ç','c').replace('ş','s'))
        unique_slug = slug
        counter = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, counter)
            counter += 1
        return unique_slug
    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        return super(Post,self).save(*args, **kwargs)
    class Meta:
        ordering = ['-publishing_date']

class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def get_delete_url(self):
        return reverse("post:commentdelete", kwargs={"commentid": self.id})

    # def get_update_url(self):
    #     return rever
    
class Category(models.Model):
    title = models.CharField(max_length=200)
    created_date=models.DateTimeField(auto_now_add=True)
    home_show = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Kateqoriya'
        verbose_name_plural= 'Kateqoriyalar'

    def get_absolute_url(self):
        return reverse("post:category", kwargs={"categoryid": self.id})

    def get_delete_url(self):
        return reverse ('post:categorydelete', kwargs={'categoryid':self.id})
    

class HomeImage(models.Model):
    content = models.TextField(default='...')
    image = models.ImageField(upload_to='homeimage')
    number = models.IntegerField(default=0)


class PostLike(models.Model):
    user = models.ManyToManyField(User)
    post = models.OneToOneField(Post,on_delete=models.CASCADE,)

class UploadImage(models.Model):
    image = models.ImageField(upload_to='image_for_url')

    class Meta:
        verbose_name_plural = 'Upload Images'
    
    