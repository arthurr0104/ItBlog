from django.urls import path

from .views import IndexPage,  post_by_tag, post_by_category, post_detail

urlpatterns = [
    path('', IndexPage.as_view(), name='home'),
    path('post/<int:pk>/<slug:slug>/', post_detail, name='post_detail'),
    path('category/<int:pk>/<slug:slug>/', post_by_category, name='post_by_category'),
    path('tag/<int:pk>/<slug:slug>/', post_by_tag, name='post_by_tag'),
]
