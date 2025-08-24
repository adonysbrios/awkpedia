from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import ArticleForm, PublicationForm
from .models import Article, ActiveVersion, Publication
from django.template.defaultfilters import slugify
from django.core.exceptions import ObjectDoesNotExist
from .utils import markdownify

def index(request):
    return render(request, 'index.html')

def create_article(request):
    if request.method == "POST":
        pubForm = PublicationForm(request.POST)
        articleForm = ArticleForm(request.POST)
        if articleForm.is_valid() and pubForm.is_valid():
            content = pubForm.cleaned_data['content']
            title = articleForm.cleaned_data['title']
            article = Article(title=title, slug=slugify(title))
            article.save()
            publication = Publication(content=content, article=article)
            publication.save()
            version_ = ActiveVersion(article=article, active_version=publication, last_valid_version=publication)
            version_.save()
            return HttpResponseRedirect("/wiki/"+slugify(title))
    return render(request, "create_article.html", {"pub_form":PublicationForm(), "article_form": ArticleForm()})

def get_article(request, slug):
    try:
        article = Article.objects.get(slug=slug)
        publication = Publication()
        if "version" in request.GET:
            publication = Publication.objects.get(id=request.GET['version'], article=article)
        else:
            version = ActiveVersion.objects.get(article=article)
            publication = version.active_version
        content = markdownify(publication.content)
        return render(request, "get_article.html", {"article":article, "content":content})
    except ObjectDoesNotExist:
        return HttpResponseRedirect('/')
    
def edit_article(request, slug):
    try:
        article = Article.objects.get(slug=slug)
        version = ActiveVersion.objects.get(article=article)
        publication = version.active_version
        content = markdownify(publication.content)
        
        if(request.method == "POST"):
            pubForm = PublicationForm(request.POST)
            
            if pubForm.is_valid():
                content = pubForm.cleaned_data['content']
                publication = Publication(content=content, article=article)
                publication.save()
                version.active_version = publication
                version.save()
            return HttpResponseRedirect('/wiki/'+slug)
        
        return render(request, "edit_article.html", {"article":article, "content":content, "publication_content":PublicationForm(initial={'content':publication.content})})
    except ObjectDoesNotExist:
        return HttpResponseRedirect('/')
    
def get_article_versions(request, slug):
    try:
        article = Article.objects.get(slug=slug)
        version = ActiveVersion.objects.get(article=article)
        publications = Publication.objects.filter(article=article).order_by('-id')
        
        return render(request, "article_versions.html", {"article":article, "article_version_info":version, "publications":publications})
    except ObjectDoesNotExist:
        return HttpResponseRedirect('/')
    
def search_article(request):
    if 'q' in request.GET:
        q = request.GET['q']
        articles = Article.objects.filter(title__icontains = q)
        result_data = []
        for article in articles:
            publication = ActiveVersion.objects.get(article=article).active_version
            data = {
                "article": article,
                "content": publication.plain_text[:150]
            }
            result_data.append(data)
            
        return render(request, 'search_articles.html', {"articles":result_data, "title":q})
    return HttpResponseRedirect('/')