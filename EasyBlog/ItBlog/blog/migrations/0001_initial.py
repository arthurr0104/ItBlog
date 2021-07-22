# Generated by Django 3.2.5 on 2021-07-14 16:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Անվանումը')),
                ('slug', models.SlugField(default=None, max_length=255, null=True, unique=True, verbose_name='Սլագ')),
            ],
            options={
                'verbose_name': 'Կատեգորիա',
                'verbose_name_plural': 'Կատեգորիաներ',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ImportantNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Գրառման վերնագիր')),
                ('content', models.TextField(blank=True, verbose_name='Կոնտենտ')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Հրապարակման ժամանակը')),
                ('edited_date', models.DateTimeField(auto_now=True, verbose_name='Խմբագրման ժամանակը')),
                ('is_published', models.BooleanField(default=True, verbose_name='Հրապարակված է')),
            ],
            options={
                'verbose_name': 'Կարևոր հայտարարություն',
                'verbose_name_plural': 'Կարևոր հայտարարություններ',
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Անվանումը')),
                ('slug', models.SlugField(default=None, max_length=255, null=True, unique=True, verbose_name='Սլագ')),
            ],
            options={
                'verbose_name': 'Տեգ',
                'verbose_name_plural': 'Տեգեր',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Գրառման վերնագիր')),
                ('content', models.TextField(blank=True, verbose_name='Կոնտենտ')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Հրապարակման ժամանակը')),
                ('edited_date', models.DateTimeField(auto_now=True, verbose_name='Խմբագրման ժամանակը')),
                ('is_published', models.BooleanField(default=True, verbose_name='Հրապարակված է')),
                ('image', models.ImageField(blank=True, upload_to='media/blog/posts/%Y/%m/%d/', verbose_name='Նկար')),
                ('views', models.IntegerField(default=0, verbose_name='Դիտումների քանակը')),
                ('is_top', models.BooleanField(default=False, verbose_name='Թոփ հայտարարություն')),
                ('slug', models.SlugField(default=None, null=True, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.category', verbose_name='Կատեգորիա')),
                ('tag', models.ManyToManyField(blank=True, default=None, related_name='tags', to='blog.Tag', verbose_name='Տեգ')),
            ],
            options={
                'verbose_name': 'Գրառում',
                'verbose_name_plural': 'Գրառումներ',
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Մեկնաբանությունը')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Հրապարակման ժամանակը')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Հեղինակ')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='blog.comment')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post', verbose_name='Գրառման id')),
            ],
            options={
                'verbose_name': 'Մեկնաբանություն',
                'verbose_name_plural': 'Մեկնաբանություններ',
            },
        ),
    ]