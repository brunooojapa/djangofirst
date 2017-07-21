# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from serializers import *


class NewViewSet(ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewSerializer


class CategoryNewsViewSet(ModelViewSet):
    queryset = CategoryNews.objects.all()
    serializer_class = CategoryNewsSerializer
