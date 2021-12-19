from django.db import models


class Recipes(models.Model):
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Рецепт')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
