from django.contrib import admin

# Register your models here.
from .models import Team, User,Board,Task

admin.site.register(User)
admin.site.register(Team)
admin.site.register(Board)
admin.site.register(Task)
