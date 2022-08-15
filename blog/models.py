from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    content = models.TextField()
    by = models.CharField(help_text='Provide your name if you are the originator', max_length=50, default='')
    resources = models.TextField(help_text='Where can the excerpt be found? Provide links, books, titles etc. if any.',
                                 blank=True, default='')
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class Review(models.Model):
    objects = None
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='reviews', on_delete=models.CASCADE)
    content = models.TextField(help_text='Share your thoughts or query the subject.')
    date_commented = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.reviewer.username

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
