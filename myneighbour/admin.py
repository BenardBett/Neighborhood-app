# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import neighbourhood, Profile, Authorities, Health, Post
# Register your models here.
admin.site.register(neighbourhood)
admin.site.register(Profile)
admin.site.register(Authorities)
admin.site.register(Health)
admin.site.register(Post)