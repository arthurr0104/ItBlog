from django import template

from blog.models import Category, Post, Tag, Comment

register = template.Library()


@register.simple_tag(name='change_temp_var')
def change_temp_var(value):
    value += 1
    return value


@register.simple_tag(name='get_tags')
def get_tags():
    return Tag.objects.all()


@register.simple_tag(name='get_categories')
def get_categories():
    return Category.objects.all()


@register.simple_tag()
def get_top_posts():
    posts = Post.objects.filter(is_published=True, views__gte=10, is_top=True).order_by('-views', '-created_date')

    return posts[:3]


@register.simple_tag()
def get_comment(post_id):
    comments = Comment.objects.filter(is_published=True, post_id=post_id)
    return comments


@register.simple_tag()
def get_comments_count(post_id):
    post = Post.objects.get(pk=post_id)
    count = post.comment_set.all().count()
    return count

