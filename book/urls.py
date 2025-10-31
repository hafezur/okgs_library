from  django.urls import path
#from . views import home
#from book.views import home,store_book,show_books,edit_books,delete_book
from . import views
urlpatterns = [
    #path('',views.home), # function base view
    path('<int:roll>/',views.my_template_view.as_view(),{'author':'Mahadi'},name='homepage'), # class base view
    
    #path('store_new_book/',views.store_book, name='store_book'),
    path('store_new_book/',views.BookFormView.as_view(), name='store_book'),
    
    #path('show_books/',views.show_books,name='show_books'),
    path('show_books/',views.BookListByClassBased.as_view(),name='show_books'),
    
    path('book_details/<int:id>',views.BookDetailView.as_view(),name='book_details'),
    
    # path('edit_book/<int:id>',views.edit_books,name='edit_book'),
    path('edit_book/<int:pk>',views.BookUpdateView.as_view(),name='edit_book'),
    
    # path('delete_book/<int:id>',views.delete_book, name='delete_book')
    path('delete_book/<int:pk>',views.DeleteBookView.as_view(), name='delete_book')
]
