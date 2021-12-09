from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings

# Create your models here.

class Notification(models.Model):
    notification_type = models.IntegerField()
    to_user = models.ForeignKey(User, related_name='notification_to', on_delete=models.CASCADE, null=True)
    from_user = models.ForeignKey(User, related_name='notification_from', on_delete=models.CASCADE, null=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='+', blank=True, null=True)
    reply = models.ForeignKey('Reply', on_delete=models.CASCADE, related_name='+', blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    user_has_seen = models.BooleanField(default=False)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Reply(models.Model):
    post = models.ForeignKey(Post, related_name="replies", on_delete=models.CASCADE, default="0")
    author = models.CharField(max_length=100)
    content = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.author)

class Activities(models.Model):
    SPORTS = 'Sport'
    ENTERTAINMENT = 'Entertainment'
    EXERCISE = 'Fitness'
    HANGOUT = 'Hangout'
    HEALTH = 'Health'
    SCHOOL = 'School'
    WORK = 'Work'
    OTHER = 'Other'

    ACTIVITY_CHOICES = [
        (SPORTS, 'Sports'),
        (ENTERTAINMENT, 'Entertainment'),
        (EXERCISE, 'Exercise'),
        (HANGOUT, 'Hangout'),
        (HEALTH, 'Health'),
        (SCHOOL, 'School'),
        (WORK, 'Work'),
        (OTHER, 'Other')
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE, default="0")
    name = models.CharField('Event Title', max_length=100)
    type = models.CharField(max_length=20, choices=ACTIVITY_CHOICES, default=SPORTS)
    startTime = models.DateTimeField('Start Date')
    endTime = models.DateTimeField('End Date')
    location = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
    @property
    def get_html_url(self):
        url = reverse('activity-detail', args=(self.id,))
        return f'<a href="{url}"> {self.name} </a>'
    
class Shopping(models.Model):
    OUTDOOR = 'Outdoor'
    ENTERTAINMENT = 'Entertainment'
    HYGEINE = 'Hygeine'
    FOOD = 'Food'
    CLOTHING = 'Clothing'

    ITEM_CATEGORIES = [
        (OUTDOOR, 'Outdoor'),
        (ENTERTAINMENT, 'Entertainment'),
        (HYGEINE, 'Hygeine'),
        (FOOD, 'Food'),
        (CLOTHING, 'Clothing')
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE, default="0")
    item_category = models.CharField(max_length=20, choices=ITEM_CATEGORIES, default=FOOD)
    item = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    store = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.item


class Attendees(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Meeting(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default="0")
    name = models.CharField(max_length=100)
    numParticipants = models.IntegerField()
    participantNames = models.ManyToManyField(Attendees)

    def __str__(self):
        return self.name

class Health(models.Model):
    ONCE_DAILY = 'Once daily'
    TWICE_A_DAY = 'Two times a day'
    ONCE_NIGHTLY = 'Once nightly'
    ONCE_WEEKLY = 'Once a week'
    ONCE_EVERY_OTHER_DAY = 'Once every other day'

    DOSE_TIME_CHOICES = [
        (ONCE_DAILY, 'Once daily'),
        (TWICE_A_DAY, 'Two times a day'),
        (ONCE_NIGHTLY, 'Once nightly'),
        (ONCE_WEEKLY, 'Once a week'),
        (ONCE_EVERY_OTHER_DAY, 'Once every other day'),
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE, default="0")
    doctorName = models.CharField(max_length=30)
    phoneNum = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=100)
    medicine = models.CharField(max_length=100)
    dose = models.IntegerField()
    timeToTake = models.CharField(max_length=20, choices=DOSE_TIME_CHOICES, default=ONCE_DAILY)

    def __str__(self):
        return self.medicine

class ActivityReply(models.Model):
    post = models.ForeignKey(Activities, related_name="replies", on_delete=models.CASCADE, default="0")
    author = models.CharField(max_length=100)
    content = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

class File(models.Model):
    name= models.CharField(max_length=500)
    filepath= models.FileField(upload_to='files/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.filepath)