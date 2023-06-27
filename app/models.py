from django.db import models

from django.contrib.auth.models import User


SUBMISSION_TYPE_CHOICES = [
      ('IMAGE', 'Image'),
      ('FILE', 'File'),
      ('LINK', 'Link'),
    ]

class Hackathon(models.Model):
  name = models.CharField(max_length=300)
  description = models.TextField()
  background_image = models.ImageField(upload_to='hackathon/backgroundImages/')
  hackethon_image = models.ImageField(upload_to='hackathon/hackathonImages/')
  submission_type = models.CharField(max_length=10, choices=SUBMISSION_TYPE_CHOICES)
  start_date = models.DateTimeField(auto_now_add=True)
  end_date = models.DateTimeField()
  reward_price = models.DecimalField(max_digits=10, decimal_places =2)
  
  def __str__(self):
        return self.name
    

class Submission(models.Model):
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    submission_name = models.CharField(max_length=200)
    summary = models.TextField()
    submission_file = models.FileField(upload_to='hackathon/submissions', blank=True, null=True)
    submission_link = models.URLField(blank=True, null=True)
    submission_image = models.ImageField(upload_to='hackathon/submissions', blank=True, null=True)
    submission_datetime = models.DateTimeField(auto_now_add=True)
     
    def __str__(self):
        return self.submission_name

class UserSubmissions(models.Model):
   hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
   user = models.ForeignKey(User, on_delete=models.CASCADE)