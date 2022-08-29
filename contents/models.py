from django.db import models
from cloudinary.models import CloudinaryField


class Type(models.Model):
    title = models.CharField(max_length=250)
    slug = models.CharField(max_length=250)
    excerpt = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    slug = models.SlugField()
    excerpt = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Category(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Publication(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    excerpt = models.TextField(null=True, blank=True)
    img = models.ImageField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title


class Geotag(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    amar_code = models.CharField(max_length=100, null=True, blank=True)
    json = models.JSONField()

    def __str__(self):
        return self.title


class Content(models.Model):
    months = [
        (1,'فروردین'), (2,'اردیبهشت'), (3,'خرداد'),
        (4,'تیر'), (5,'مرداد'), (6,'شهریور'), (7,'مهر'),
        (8,'آبان'), (9,'آذر'), (10,'دی'),(11,'بهمن'),
        (12,'اسفند'),
    ]
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    featured = models.BooleanField(default=False)
    authors = models.ManyToManyField(Author, related_name="authors", blank=True)
    translators = models.ManyToManyField(Author, related_name="translators", blank=True)
    category = models.ManyToManyField(Category, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    excerpt = models.TextField(null=True, blank=True)
    img = CloudinaryField(resource_type="", null=True, blank=True)
    publication = models.ForeignKey(Publication, null=True, blank=True, on_delete=models.CASCADE)
    pub_date_y = models.IntegerField(null=True, blank=True)
    pub_date_m = models.IntegerField(choices=months, null=True, blank=True)
    pub_date_d = models.IntegerField(null=True, blank=True)
    pub_date_full = models.IntegerField(null=True, blank=True)
    edition = models.IntegerField(null=True, blank=True)
    volume = models.CharField(max_length=250, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    pdf_file = CloudinaryField(resource_type="", null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    geotags = models.ManyToManyField(Geotag, blank=True)
    created_by = models.CharField(max_length=300, default='maskan', null=True, blank=True)
    modified_by = models.CharField(max_length=300, default='', null=True, blank=True)
    published = models.BooleanField(default=True)


    def __str__(self):
        return self.title


