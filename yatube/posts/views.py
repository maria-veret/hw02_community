from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request: str) -> str:
    """Функция для главной страницы,
    отображение последних 10 постов.
    """
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]
    title = 'Последние обновления на сайте'
    context = {
        'posts': posts,
        'title': title,
    }
    return render(request, template, context)


def group_posts(request: str, slug: str) -> str:
    """Функция для записей сообщества,
    отображение последних 10 постов группы.
    """
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:10]
    title = f'Записи сообщества {group}'
    context = {
        'group': group,
        'posts': posts,
        'title': title,
    }
    return render(request, template, context)
