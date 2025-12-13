from django.contrib import admin

from book.models import BookStoreModel,UserRegistration
# Register your models here.

class BookStoreModelAdmin(admin.ModelAdmin):
    list_display=('id','book_name','author','category','first_pub','last_pub','book_image',)
    
admin.site.register(BookStoreModel, BookStoreModelAdmin)

admin.site.register(UserRegistration)