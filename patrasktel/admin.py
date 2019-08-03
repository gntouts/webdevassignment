from django.contrib import admin

# Register your models here.
from patrasktel.models import Stop, Route, Schedule, Announcement, Ticket,  About, Contact
admin.site.register(Stop)
admin.site.register(Route)
admin.site.register(Schedule)
admin.site.register(Announcement)
admin.site.register(Ticket)
admin.site.register(Contact)
admin.site.register(About)
