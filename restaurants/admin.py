# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import (
    Reservation,
    Restaurant,
)

admin.site.register(Restaurant)
admin.site.register(Reservation)
