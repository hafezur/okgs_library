from django.contrib import admin
from .models import BookStoreModel, UserRegistration

@admin.register(BookStoreModel)
class BookStoreAdmin(admin.ModelAdmin):
    list_display = ('book_name','author','category','first_pub','last_pub')
    list_filter = ('category',)
    search_fields = ('book_name','author')
    ordering = ('-first_pub',)
    list_per_page = 10


@admin.register(UserRegistration)
class UserRegistrationAdmin(admin.ModelAdmin):
    list_display = ('email','first_name','last_name','city','country','is_active','is_admin')
    list_filter = ('country','is_active','is_admin')
    search_fields = ('email','first_name','last_name')
    ordering = ('email',)


"""
from book.models import BookStoreModel,UserRegistration
# Register your models here.

class BookStoreModelAdmin(admin.ModelAdmin):
    list_display=('id','book_name','author','category','first_pub','last_pub','book_image',)
    
admin.site.register(BookStoreModel, BookStoreModelAdmin)

admin.site.register(UserRegistration) """

from book.models import Category
# Register your models here.

    


admin.site.register(Category)