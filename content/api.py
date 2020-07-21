from __future__ import unicode_literals

import logging

from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import responses
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework.views import APIView
from content.models import VocabItem

logger = logging.getLogger(__name__)


@api_view(['GET'])
def vocab_items_detail(request):
    """ Returns details of vocab items"""
    pass
