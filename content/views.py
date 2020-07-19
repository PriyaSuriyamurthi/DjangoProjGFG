"""Contains all views for content app"""
from __future__ import unicode_literals

import logging
from django.shortcuts import render


def home_view(request):
    """ Renders Home Page"""
    template = 'home.html'
    context = {}
    return render(request, template, context)


def base_view(request):
    """ Renders base Page"""
    template = 'base.html'
    context = {"word": "example"}
    return render(request, template, context)
