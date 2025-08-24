from bs4 import BeautifulSoup
from django.db import models
from .utils import markdownify
from markdownx.models import MarkdownxField
from django.db.models.signals import post_save
import datetime

def create_article():
    pass

def create_publication():
    pass

def change_article_version():
    pass

class Article(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField()
    
    def __str__(self):
        return self.title

class Publication(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    content = MarkdownxField()
    plain_text = models.TextField(default="")
    
    def save(self, *args, **kwargs):
        content = markdownify(self.content)
        soup = BeautifulSoup(content, 'html.parser')
        paragraphs = soup.find_all('p')
        plain_text = ""
        for p in paragraphs:
            plain_text += p.text + " "
        self.plain_text = plain_text
        super(Publication, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.article.title + " " + str(self.date.day) + "/" + str(self.date.month) + "/" + str(self.date.year) + " " + str(self.date.hour) + ":" + str(self.date.minute)
    
class ActiveVersion(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    active_version = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name="Active_version")
    last_valid_version = models.ForeignKey(Publication, on_delete=models.CASCADE, related_name="Last_valid_version")
    
    def __str__(self):
        return self.active_version.__str__()