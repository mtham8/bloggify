from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

# To add models ==> python manage.py makemigrations {{name}}
# To apply the added models to the database ==> python manage.py migrate {{name}}

# Model to post blog content
# models.Model tells Django that Post is a Django Model
class Post(models.Model):
  author = models.ForeignKey(User)
  slug = models.SlugField(unique=True)
  title = models.CharField(max_length=200)
  text = models.TextField()
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)
  # def publish(self):
  #   self.published_date = timezone.now()
  #   self.save()
  def __unicode__(self):
    return self.title
  @models.permalink
  def get_absolute_url(self):
    return ('blog_post_detail', (),
            {
                'slug' :self.slug,
            })
  def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = slugify(self.title)
    super(Post, self).save(*args, **kwargs)

# Model to post comments
class Comment(models.Model):
  name = models.CharField(max_length=42)
  text = models.CharField(max_length=200)
  text = models.TextField()
  post = models.ForeignKey(Post)
  created_date = models.DateTimeField(default=timezone.now)
  def __unicode__(self):
    return self.text
