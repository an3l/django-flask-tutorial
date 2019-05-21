from django.contrib import admin

# Register your models here.
from .models import Smjer, Ucenik, Predmet, Diploma

admin.site.register(Smjer)
admin.site.register(Ucenik)
admin.site.register(Predmet)
admin.site.register(Diploma)
admin.site.site_header = 'Upis ucenika'
admin.site.index_title = 'Tehnicka skola Zenica'
admin.site.site_title = 'Upis ucenika u skolu' # default: "Django site admin"