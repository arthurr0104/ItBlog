from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Post
from .services import get_important_news, get_post_status, change_as_top, add_view, create_paginator_for_list, \
    add_comment

from .services import get_posts_by_category_or_tag


class IndexPage(ListView):
    model = Post
    paginate_by = 6
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexPage, self).get_context_data(**kwargs)
        context['temp'] = 1
        context['range'] = range(1, self.paginate_by, 3)
        context['important_news'] = get_important_news()
        return context

    def get_queryset(self):
        return Post.objects.filter(is_published=True, )


def post_detail(request, pk, slug):
    post = Post.objects.get(pk=pk)
    # start add view and add top list operations
    add_view(pk)
    if get_post_status(pk):
        change_as_top(pk)
    # end operation

    return render(request, 'blog/post_detail.html', context={'post': post,
                                                             'form': add_comment(request, pk)})


def post_by_category(request, pk, slug):
    temp = 1
    rangee = range(1, 6, 3)
    posts = get_posts_by_category_or_tag(pk)
    page_obj = create_paginator_for_list(posts, request.GET.get('page'), 12)
    return render(request, 'blog/post_by_category.html', {'posts': page_obj.object_list, 'page_obj': page_obj,
                                                          'temp': temp,
                                                          'range': rangee})


def post_by_tag(request, pk, slug):
    temp = 1
    rangee = range(1, 6, 3)
    posts = get_posts_by_category_or_tag(pk, category=False)
    page_obj = create_paginator_for_list(posts, request.GET.get('page'), 2)

    return render(request, 'blog/post_by_category.html', {'posts': page_obj.object_list, 'page_obj': page_obj,
                                                          'temp': temp,
                                                          'range': rangee})
