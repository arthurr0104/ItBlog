from django.contrib import messages
from django.db.models import F

from .forms import UserCommentForm
from .models import Post, Category, ImportantNews
from django.core.paginator import Paginator


def get_posts_by_category_or_tag(category_or_tag_id, category=True):
    if category:
        return Post.objects.filter(is_published=True, category_id=category_or_tag_id)
    return Post.objects.filter(is_published=True, tag__id=category_or_tag_id)


def create_paginator_for_list(object_list, page_number, count_for_page=12):
    paginator = Paginator(object_list, count_for_page)

    return paginator.get_page(page_number)


def get_important_news(count=2):
    if ImportantNews.objects.filter(is_published=True).exists():
        return ImportantNews.objects.filter(is_published=True)[:count]


def get_top_posts(count=3):
    return {'top_posts': Post.objects.filter(is_published=True, is_top=True)}


def change_as_top(post_id):
    if get_post_status(post_id):
        post = Post.objects.get(pk=post_id)
        post.is_top = True
        post.save()
        post.refresh_from_db()
        return 1
    return 0


def get_post_status(post_id):
    """Ֆունկցիան վերադարձնում է 1, եթե գրառումը թոփում է, 0 հակառակ դեպքում"""
    if Post.objects.get(pk=post_id).views >= 5:
        return 1
    return 0


def add_view(post_id):
    post = Post.objects.get(pk=post_id)
    post.views = F('views') + 1  # Ավելացնում ենք դիտումների քանակին 1
    post.save()
    post.refresh_from_db()


def add_comment(request, post_id):
    initial = {'post': post_id}
    if request.method == "POST":
        comment_form = UserCommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            new_comment.save()
            messages.add_message(request, messages.SUCCESS,
                                 'Մեկնաբանությունը հրապարակված է')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Մեկնաբանությունը հրապարակված չէ')
            return comment_form
    form = UserCommentForm(initial=initial)
    return form
