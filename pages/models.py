from django.db import models

# Create your models here.


class Contact(models.Model):
  fullname = models.CharField(max_length=60)
  number = models.IntegerField()
  email = models.EmailField()
  message = models.TextField()
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self) -> str:
    return self.fullname

class News(models.Model):
  title = models.CharField(max_length=200)
  content = models.TextField()
  image = models.ImageField(upload_to='news')
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self) -> str:
    return self.title


class Project(models.Model):
  title = models.CharField(max_length=200)
  content = models.TextField()
  image = models.ImageField(upload_to='projects')
  finish = models.BooleanField(default=False)
  date = models.DateTimeField(auto_now_add=True)

  def __str__(self) -> str:
    return self.title

  def finished_or_not(self):
    status = str()
    if self.finish:
      status = 'Tamamlandı'
    else:
      status = 'Davam edir'
    return status
  