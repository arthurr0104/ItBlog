from django.db import models

from blog.models import BasePost


class AboutUs(BasePost):
    image = models.ImageField('Լուսանկար', upload_to='media/contact/aboutus/')

    class Meta:
        verbose_name = 'Գրառում ընկերության մասին'
        verbose_name_plural = 'Գրառումներ ընկերության մասին'
        ordering = ['-created_date']


class ContactUs(models.Model):
    name = models.CharField('Կապնվողի անունը', max_length=50)
    email = models.EmailField(verbose_name='Կապնվողի էլ հասցեն')
    message = models.TextField('Կապնվողի նամակը')
    created_at = models.DateTimeField('Ստեղծվել է', auto_now_add=True)

    class Meta:
        verbose_name = 'Նամակ'
        verbose_name_plural = 'Նամակներ'
        ordering = ['-created_at']
