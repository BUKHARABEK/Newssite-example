from django.db import models
from django.urls import reverse


class Post(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=255, verbose_name='Title ')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Url ')
    content = models.TextField(blank=True, verbose_name='Content ')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Time create ')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Time update ')
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT, verbose_name='Is published ')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Photo ')
    views = models.IntegerField(default=0, verbose_name='Views ')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts', verbose_name='Category ')
    tags = models.ManyToManyField('Tag', blank=True, related_name='tags', verbose_name='Tags ')
    author = models.OneToOneField('Author', on_delete=models.SET_NULL,
                                  null=True, blank=True, related_name='post', verbose_name='Author ')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={"slug": self.slug})

    class Meta:
        ordering = ['-time_create']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Category')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Url')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})

    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name='Tag')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Url')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag', kwargs={"slug": self.slug})

    class Meta:
        ordering = ['name']
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name='Author')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Url')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
