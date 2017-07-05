# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from company.models import Company
# from user.models import User
from user.models import UserProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# admin.site.register(Company)
# admin.site.register(User)

# admin.site.register(Profil)

class ProfileInline(admin.StackedInline):
    model = UserProfile
    # can_delete = False
    # verbose_name_plural = 'Profil'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
	inlines = (ProfileInline, )
	list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_company', 'place')
	list_select_related = ('userprofile', )

	def get_company(self, instance):
		return instance.userprofile.company
	def place(self, instance):
		return instance.userprofile.place
	get_company.short_description = 'company'
	def get_inline_instances(self, request, obj=None):
		if not obj:
			return list()
		return super(CustomUserAdmin, self).get_inline_instances(request, obj)

class CompanyAdmin(admin.ModelAdmin):

    list_display = ('name', 'name', 'name')
    # list_display_links = ('id', 'title')
    # search_fields = ('title', 'content')
    # list_per_page = 25

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Company, CompanyAdmin)
