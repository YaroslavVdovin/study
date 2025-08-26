from django.db import models

class Article(models.Model):

    """Статья на сайте."""

    class ArticleStatus(models.TextChoices):
        DRAFT = "draft", 'На модерации'
        PUBLISH = 'publish', 'Готово к публикации'
        INACTIVE = 'inactive', 'К удалению'

    author = models.ForeignKey('users.User', related_name='articles', on_delete=models.SET_NULL, null=True, default=None)

    title = models.CharField("Заголовок новости", max_length=64, unique=True)
    description = models.CharField("Описание новости", max_length=200)
    text = models.TextField("Текст новости")
    pub_date = models.DateTimeField("Дата публикации")
    status = models.CharField(max_length=8, choices=ArticleStatus.choices, default=ArticleStatus.DRAFT)

    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    upd_date = models.DateTimeField("Дата обновления", auto_now=True)