from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Pages(models.Model):
    images = models.ImageField(upload_to='imagebanner', verbose_name = "фотки на главной старнице")
    
    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Баннер на Главной Страницы'

class Images(models.Model):
    images = models.ImageField(upload_to='imagebanner', verbose_name = "фотки на главной старнице")
    image = models.ForeignKey(Pages, on_delete=models.CASCADE, related_name='image')

class ContactPage(models.Model):
    title_page = models.CharField(max_length=150, verbose_name='Заголовка')
    title_contact = models.CharField(max_length=150, verbose_name='Заголовка Контактов')  
    description_contact =  RichTextField(verbose_name='Описание')

    def __str__(self):
        return self.title_page
    
    class Meta:
        verbose_name = 'Настройка Страницы Контактов'
        verbose_name_plural = 'Настройка Страницы Контактов'

class ContactSettings(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовка')
    description = RichTextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объекты Контактов'
        verbose_name_plural = 'Объекты Контактов'

class ContactMessage(models.Model):
    name = models.CharField(max_length=80)
    email = models.CharField(max_length=80)
    message = models.TextField(max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True)

    ip = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)

    telegram_ok = models.BooleanField(default=False)
    telegram_message_id = models.BigIntegerField(null=True, blank=True)
    telegram_error = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} <{self.email}> @ {self.created_at:%Y-%m-%d %H:%M}"