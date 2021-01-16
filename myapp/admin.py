from django.contrib import admin
from myapp.models import Song, User, CollaborativeList, Concert

# Register your models here.
admin.site.register(Song)
admin.site.register(User)
admin.site.register(CollaborativeList)
admin.site.register(Concert)
