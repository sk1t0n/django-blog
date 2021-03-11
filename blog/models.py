from hashlib import shake_256
from time import time

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from django.shortcuts import reverse
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(
        max_length=100, unique=True, verbose_name=_('name')
    )
    slug = models.SlugField(
        max_length=111, blank=True, unique=True,
        verbose_name=_('slug'), help_text=_('slug_help_text')
    )
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.SET_NULL,
        verbose_name=_('parent')
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name=_('title'))
    slug = models.SlugField(
        max_length=161, blank=True, unique=True,
        verbose_name=_('slug'), help_text=_('slug_help_text')
    )
    content = models.TextField(verbose_name=_('content'))
    excerpt = models.TextField(
        max_length=500, blank=True,
        verbose_name=_('excerpt'), help_text=_('excerpt_help_text')
    )
    views = models.PositiveIntegerField(
        default=0, verbose_name=_('number_of_views')
    )
    read_time = models.PositiveIntegerField(
        default=0, verbose_name=_('read_time')
    )
    created_date = models.DateTimeField(
        auto_now_add=True, verbose_name=_('created_date')
    )
    is_published = models.BooleanField(
        default=False, db_index=True, verbose_name=_('published')
    )
    published_date = models.DateTimeField(
        null=True, verbose_name=_('published_date')
    )
    modified_date = models.DateTimeField(
        auto_now=True, verbose_name=_('modified_date')
    )
    image = models.ImageField(
        null=True, blank=True, upload_to='images/posts/',
        verbose_name=_('image')
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name=_('author')
    )
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL,
        related_name='posts', verbose_name=_('category')
    )
    tags = models.ManyToManyField(
        'Tag', blank=True, related_name='posts', verbose_name=_('tags')
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-published_date', '-created_date', 'title']
        verbose_name = _('post')
        verbose_name_plural = _('posts')

    def save(self, *args, **kwargs):
        if self.pk and self.is_published:
            post = Post.objects.filter(pk=self.pk).first()
            if post and not post.published_date:
                self.published_date = timezone.localtime()
        elif self.is_published:
            self.published_date = timezone.localtime()
        super(Post, self).save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(
        max_length=100, unique=True, verbose_name=_('name')
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag-post-list', kwargs={'name': self.name})

    class Meta:
        ordering = ['name']
        verbose_name = _('tag')
        verbose_name_plural = _('tags')


def set_unique_slug(sender, instance, *args, **kwargs):
    # update slug:
    if instance.pk:
        db_obj = sender.objects.filter(pk=instance.pk).first()
        # old and new slugs are equal
        if db_obj.slug == instance.slug:
            return

    # create slug
    if not instance.slug:
        if isinstance(instance, Post):
            slug = slugify(instance.title)
        else:
            slug = slugify(instance.name)
    # # update slug
    else:
        slug = instance.slug

    qs = sender.objects.filter(slug=slug).first()
    if qs:
        hash = shake_256(str(time()).encode()).hexdigest(5)
        slug = f'{slug}-{hash}'
    instance.slug = slug


pre_save.connect(set_unique_slug, sender=Category)
pre_save.connect(set_unique_slug, sender=Post)
