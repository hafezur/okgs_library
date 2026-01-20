from django.contrib import admin
from  django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static

#from . views import home
#from book.views import home,store_book,show_books,edit_books,delete_book
from . import views
urlpatterns = [
    path('',views.homepage_view1,name="homepage"),
    #path('',views.home), # function base view
    #path('',views.my_template_view.as_view(),name='homepage'), # class base viewS
    path('dashboard/',views.dashboard_function,name='dashboard'), # class base viewS
    path('login_interface/',views.Combinelogin_interface,name='login_interface'), # class base viewS
    path('user_interface/', views.userInterfaceView.as_view(), name='get_user_interface'),
    #path('store_new_book/',views.store_book, name='store_book'),
    path('store_new_book/',views.book_form_view, name='store_book'),
    
    #path('show_books/',views.show_books,name='show_books'),
    path('show_books/',views.show_books,name='show_books'),
    
    path('book_details/<int:id>',views.book_detail_view, name='book_details'),
    
    # path('edit_book/<int:id>',views.edit_books,name='edit_book'),
    path('edit_book/<int:id>',views.update_book,name='edit_book'),
    
    # path('delete_book/<int:id>',views.delete_book, name='delete_book')
    path('delete_book/<int:pk>',views.delete_book, name='delete_book'),
    path('news&events/',views.News_Events, name='newsEvent'),
    path('register/',views.user_register, name='sign_up'),
    path('contact/',views.contact, name='contact'),
    path('login/', views.user_login, name='user_login'),
    path("logout/", views.user_logout, name="logout"),
    path('update-profile-picture/', views.update_profile_picture, name='update_profile_picture'),
    path('read-book/<int:book_id>/', views.read_book, name='read_book'),
    path('add_category/', views.add_category, name='add_category'),
    path('show_category/', views.show_category, name='show_category'),
    path('show_stock/', views.show_stock, name='show_stock'),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

