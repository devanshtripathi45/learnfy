from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.title


class Item(models.Model):
    TYPE_BLOG = 'blog'
    TYPE_COURSE = 'course'
    TYPE_CHOICES = (
        (TYPE_BLOG, 'Blog'),
        (TYPE_COURSE, 'Course'),
    )

    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    short_description = models.TextField(max_length=500, blank=True, help_text="A brief description of the item (max 500 characters)")
    description = models.TextField(blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='items/', blank=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-published_at']

    def __str__(self) -> str:
        return f"{self.get_type_display()}: {self.title}"
