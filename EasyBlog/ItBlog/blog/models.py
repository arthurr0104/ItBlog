from django.db import models
from django.urls import reverse_lazy
from mptt.models import MPTTModel, TreeForeignKey
from crum import get_current_user


class BaseCategoryAndTag(models.Model):
    name = models.CharField('Անվանումը', max_length=255)
    slug = models.SlugField(null=True, default=None, unique=True, verbose_name='Սլագ', max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class BasePost(models.Model):
    title = models.CharField(max_length=255, verbose_name='Գրառման վերնագիր')
    content = models.TextField('Կոնտենտ', blank=True)
    created_date = models.DateTimeField('Հրապարակման ժամանակը', auto_now_add=True)
    edited_date = models.DateTimeField('Խմբագրման ժամանակը', auto_now=True)
    is_published = models.BooleanField('Հրապարակված է', default=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class ImportantNews(BasePost):
    class Meta:
        verbose_name = 'Կարևոր հայտարարություն'
        verbose_name_plural = 'Կարևոր հայտարարություններ'
        ordering = ['-created_date', ]


class Post(BasePost):
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Կատեգորիա')
    tag = models.ManyToManyField('Tag', verbose_name='Տեգ', blank=True, related_name="tags", default=None, )
    image = models.ImageField('Նկար', upload_to='media/blog/posts/%Y/%m/%d/', blank=True)
    views = models.IntegerField(verbose_name='Դիտումների քանակը', default=0)
    is_top = models.BooleanField('Թոփ հայտարարություն', default=False)
    slug = models.SlugField(null=True, default=None, unique=True, )

    class Meta:
        verbose_name = 'Գրառում'
        verbose_name_plural = 'Գրառումներ'
        ordering = ['-created_date', ]

    def get_absolute_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.pk,
                                                   'slug': self.slug})


class Category(BaseCategoryAndTag):
    class Meta:
        verbose_name = 'Կատեգորիա'
        verbose_name_plural = 'Կատեգորիաներ'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse_lazy('post_by_category', kwargs={'pk': self.pk,
                                                        'slug': self.slug})


class Tag(BaseCategoryAndTag):
    class Meta:
        verbose_name = 'Տեգ'
        verbose_name_plural = 'Տեգեր'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse_lazy('post_by_tag', kwargs={'pk': self.pk, 'slug': self.slug})


class Comment(MPTTModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Գրառման id')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Հեղինակ', default=None)
    text = models.TextField('Մեկնաբանությունը', )
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children',
                            verbose_name='Ծնող մեկնաբանություն ')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Հրապարակման ժամանակը')
    is_published = models.BooleanField('Հրապարակված է', default=True)

    class MPTTMeta:
        order_insertion_by = ['-created_at']

    class Meta:
        verbose_name = 'Մեկնաբանություն'
        verbose_name_plural = 'Մեկնաբանություններ'

    def __str__(self):
        return str(self.author)

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.modified_by = user
        super(Comment, self).save(*args, **kwargs)
