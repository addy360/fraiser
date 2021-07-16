from core.models import Donation, Profile
from django.contrib import admin

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile_img', 'user')
    list_filter = ( 'user__username',)

class DonationAdmin(admin.ModelAdmin):
    list_display = ('id', 'reference_number', 'transaction_id','profile')
    list_filter = ( 'profile',)



admin.site.register(Profile, ProfileAdmin)

admin.site.register(Donation, DonationAdmin)