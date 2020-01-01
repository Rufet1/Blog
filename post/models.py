from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey('auth.User', verbose_name = 'Yazar', on_delete=models.CASCADE,)
    category = models.ForeignKey('post.Category',on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    content = models.TextField(default="bos")
    publishing_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(unique=True,editable=False, max_length=130)

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse("post:detail", kwargs={"slug": self.slug})
        # return '/post/{}'.format(self.id)
    def get_create_url(self):
        return reverse("post:create",)
    def get_update_url(self):
        return reverse("post:update", kwargs={"slug": self.slug})
    def get_delete_url(self):
        return reverse("post:delete", kwargs={"slug": self.slug})
    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı','i'))
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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Kateqoriya'
        verbose_name_plural= 'Kateqoriyalar'

    def get_absolute_url(self):
        return reverse("post:category", kwargs={"categoryid": self.id})

    def get_delete_url(self):
        return reverse ('post:categorydelete', kwargs={'categoryid':self.id})
    