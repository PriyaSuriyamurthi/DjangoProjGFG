from django.db import models
from django.contrib.postgres.fields import ArrayField


class VocabItem(models.Model):
    """Vocab Item Model"""

    word = models.CharField(max_length=512, unique=True, db_index=True)

    origin = models.TextField(null=True, blank=True)

    meaning = models.TextField(null=True, blank=True)

    meanings = ArrayField(models.TextField(null=True, blank=True), default=list, null=True, blank=True)

    sentences = ArrayField(models.TextField(null=True, blank=True), default=list, null=True, blank=True)

    synonyms = ArrayField(models.CharField(max_length=300, null=True, blank=True), default=list, null=True, blank=True)

    antonyms = ArrayField(models.CharField(max_length=300, null=True, blank=True), default=list, null=True, blank=True)

    pronunciation = models.CharField(max_length=200, null=True, blank=True)

    pos = models.CharField(max_length=300, null=True, blank=True)

    audio_file_link = models.URLField(max_length=300, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)
