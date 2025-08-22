from django.db import models
from ckeditor.fields import RichTextField

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

class Events(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовка')
    title_events = models.CharField(max_length=150, verbose_name='Заголовка Событий')
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Настройка Страницы Событий'
        verbose_name_plural = 'Настройка Страницы Событий'    

class EventsOBJ(models.Model):
    year = models.CharField(max_length=155, verbose_name='Дата')
    title = models.CharField(max_length=155, verbose_name='Заголовка Событий')
    data = models.CharField(max_length=255,verbose_name='Место Проведение')
    url_events = models.URLField(verbose_name='Ссылкана карта', help_text='Вставьте ссылку google карту')
    image = models.ImageField(upload_to='events', verbose_name='Фото событий')
    description = RichTextField(verbose_name='Описание Событий')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Список Событий'
        verbose_name_plural = 'Список Событий'    


class About(models.Model):
    title_pages = models.CharField(
        max_length=155,
        verbose_name='Заголовка Страницы'
    )
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка О нас'
    )
    description = RichTextField(
        verbose_name='Описание О нас'
    )
    image = models.ImageField(
        upload_to='about',
        verbose_name='Фото'
    )
    title_sheff = models.CharField(
        max_length=155,
        verbose_name='Заголовка Поваров'
    ) 
    description_sheff = RichTextField(
        verbose_name='Описание Поваров'
    )
    title_testimonials = models.CharField(
        max_length=155,
        verbose_name='Заголовка Отзывов'
    )

    def __str__(self):
        return self.title_pages

    class Meta:
        verbose_name = 'Настройки Страницы О Нас'
        verbose_name_plural = 'Настройки Страницы О Нас'

class Sheff(models.Model):
    name = models.CharField(
        max_length=155,
        verbose_name='Имя'
    )
    job_type = models.CharField(
        max_length=155,
        verbose_name='Должность'
    )
    image = models.ImageField(
        upload_to='Sheff',
        verbose_name='Фото Повара'
    )

    def __str__(self):
        return self.name 


    class Meta:
        verbose_name = 'Наши Повара'
        verbose_name_plural = 'Наши Повара' 

class Testimonials(models.Model):
    name = models.CharField(
        max_length=155,
        verbose_name='Имя'
    )
    text = models.TextField(
        verbose_name='Текст'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'

class Reservation(models.Model):
    image = models.ImageField(
        upload_to='reservation',
        verbose_name='Фото Расположение'
    )
    image2 = models.ImageField(
        upload_to='reservation',
        verbose_name='Фото Расположение 2'
    )

    class Meta:
        verbose_name = 'Расположение Заведение'
        verbose_name_plural = 'Расположение Заведение'

class ReservationSettings(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    description = RichTextField(
        verbose_name='Описание'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Настройка Страницы Заведение'
        verbose_name_plural = 'Настройка Страницы Заведение'    