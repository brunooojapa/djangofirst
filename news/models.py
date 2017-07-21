# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class CategoryNews(models.Model):
    category_name = models.CharField('Nome da categoria', max_length=140)

    def __unicode__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = '01. Categorias'


class New(models.Model):
    title = models.CharField(u'Título', max_length=140)
    text = models.CharField('Texto', max_length=1000)
    category = models.ForeignKey(CategoryNews, verbose_name='Categoria', related_name='new_cateogory')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Notícia'
        verbose_name_plural = '02. Notícias'
