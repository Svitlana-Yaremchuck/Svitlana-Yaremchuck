from django.db import models
import uuid
import os


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True, db_index=True)
    is_visible = models.BooleanField(default=True)
    positive = models.PositiveSmallIntegerField(unique=True)

    def __str__(self):
        return f'{self.title}: {self.positive}'

    class Meta:
        ordering = ('positive', )


class Dish(models.Model):

    def get_file_name(self, file_name: str):
        ext = file_name.strip().split()[-1]
        return os.path.join('images/dishes', f'{uuid.uuid4()}.{ext}')

    title = models.CharField(max_length=50, unique=True, db_index=True)
    ingredients = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_special = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=True)
    positive = models.PositiveSmallIntegerField()
    desc = models.TextField(max_length=500, blank=True)
    photo = models.ImageField(upload_to=get_file_name)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}: {self.positive}'

    class Meta:
        ordering = ('positive', )


class About(models.Model):

    def get_about(self, file_name: str):
        ext = file_name.strip().split()[-1]
        return os.path.join('images/about', f'{uuid.uuid4()}.{ext}')

    address = models.TextField(max_length=50, blank=True)
    phone = models.TextField(max_length=30, blank=True)
    work_time = models.TextField(max_length=10, blank=True)
    facebook = models.TextField(max_length=20, blank=True)
    instagram = models.TextField(max_length=20, blank=True)
    wifi = models.CharField(max_length=10)
    map = models.DateField()
    photo = models.ImageField(upload_to=get_about)


class Why(models.Model):

    def get_why(self, file_name: str):
        ext = file_name.strip().split()[-1]
        return os.path.join('images/event', f'{uuid.uuid4()}.{ext}')

    date_of_creating = models.DateField(auto_now=False)
    desc = models.TextField(max_length=500, blank=True)
    advantage_1 = models.TextField(max_length=100, blank=True)
    advantage_2 = models.TextField(max_length=100, blank=True)
    advantage_3 = models.TextField(max_length=100, blank=True)
    photo = models.ImageField(upload_to=get_why)


class Event(models.Model):

    def get_event(self, file_name: str):
        ext = file_name.strip().split()[-1]
        return os.path.join('images/event', f'{uuid.uuid4()}.{ext}')

    date_of_event = models.DateField(auto_now=False)
    title = models.TextField(max_length=50)
    guest = models.TextField(max_length=50)
    menu = models.TextField(max_length=50)
    guests_num = models.PositiveSmallIntegerField()
    photo = models.ImageField(upload_to=get_event)
