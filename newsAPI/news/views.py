from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render

from news.forms import ArticleForm
from news.models import Article


def index(request):
    return HttpResponse("Welcome, you're at the news app.")


def get_news(request):
    news_id = request.GET.get('id', '')
    article = Article.objects.filter(id=news_id).values()
    if article.exists():
        data = list(article)
    else:
        data = {'result': 'error', 'message': 'No article with this id found'}
    return JsonResponse(data, safe=False)


def post_news(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = Article(title=request.POST.get('title'),
                              pub_date=request.POST.get('pub_date'),
                              category=request.POST.get('category'),
                              cover_image=request.POST.get('cover_image'),
                              content=request.POST.get('content'),
                              author=request.POST.get('author'))
            article.save()
            return HttpResponseRedirect('/news/')
    else:
        form = ArticleForm()
    return render(request, 'news/form.html', {'form': form})
