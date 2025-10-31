from django.shortcuts import render,redirect
from book.forms import BookStoreForm
from book.models import BookStoreModel
# Create your views here.

#function base view
# def home(request):
#     return render(request,'base.html')

#class base view
from django.views.generic import TemplateView
class my_template_view(TemplateView):
    template_name='home.html'
    def get_context_data(self,**kwargs): # this function is used for passing data from backend
        context=super().get_context_data(**kwargs)
        context_like={'name':'Hafiz', 'age':22}# this is the example of data passing from backend.
        print(context_like)
        print(kwargs)
        context_like.update(kwargs)
        print(context_like)
        return context_like
    
# ----------------------**********a simple divider **********--------------------------------------
# def store_book(request):
#     if request.method =='POST':
#         book= BookStoreForm(request.POST)
#         if book.is_valid():
#             book.save()
#             print(book.cleaned_data)
#             return redirect('show_books')
#     else:
#         book=BookStoreForm()
#     return render(request,'store_book.html',{'form':book })

#class based view 
#from view
# from django.views.generic.edit import FormView 
# #from django.urls import reverse_lazy # complex url k simple kore.
# #from django.http import HttpResponse
# class BookFormView(FormView):
#     template_name='store_book.html'
#     form_class=BookStoreForm
#     #success_url='/show_books/'
#     #success_url=reverse_lazy('show_books') # every complex url have to simple by using  this function.
#     def form_valid(self,form):
#         print(form.cleaned_data) # for printing data in terminal or backend.
#         form.save()
#         #return HttpResponse('Form has submitted') # its give a response in web page like showbooks.html
#         return redirect('show_books')

#class based view 
#CreateView

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy # complex url k simple kore.

class BookFormView(CreateView):
    model=BookStoreModel
    template_name='store_book.html'
    form_class=BookStoreForm
    #success_url='/show_books/'
    success_url=reverse_lazy('show_books') # every complex url have to simple by using  this function.

# ----------------------**********a simple divider **********--------------------------------------

#function based view:
from book.models import BookStoreModel
# def show_books(request):
#     book=BookStoreModel.objects.all()
#     print(book)
#     return render(request, 'show_book.html',{'data':book})

#class based view:
#list view
from django.views.generic import ListView
class BookListByClassBased(ListView):
    model=BookStoreModel  # model =built-in variable
    template_name='show_book.html' # template_name =built-in variable
    context_object_name='data' # context_object_name =built-in variable
    # ordering='author' # this is make order according to author name.
    #ordering='category' # this is make order according to category.
    #ordering='id' # this is make order according to ascending order.
    #ordering='-id' # this is make order according to dissending order.
    
    # def get_queryset(self): # function name can't be change.
    #     #return BookStoreModel.objects.filter(author='dr hafiz')
    #     return BookStoreModel.objects.filter(id='2')
    
    # def get_context_data(self,**kwargs):
    #     sort_by_author=super().get_context_data(**kwargs)
    #     sort_by_author={'data': BookStoreModel.objects.all().order_by('author')}
    #     return sort_by_author
    
    # # how to over ride template in List View:
    # def get_template_names(self):
    #     if self.request.user.is_superuser:
    #         template_name='superuser.html' # this html have to create.
    #     elif self.request.user.is_staff:
    #         template_name='stuff.html' # this html have to create
    #     else:
    #         template_name=self.template_name
            
    #     return [template_name]

# ----------------------********** a simple divider **********--------------------------------------
## function based view:
# def edit_books(request,id):
#     book=BookStoreModel.objects.get(pk=id)
#     form=BookStoreForm(instance=book)
#     if request.method == 'POST':
#         form=BookStoreForm(request.POST,instance=book)
#         if form.is_valid():
#             form.save()
#             return redirect('show_books')
#     return render(request,'store_book.html',{'form':form })


## class based view:
# UpdateView
from django.views.generic.edit import UpdateView
class BookUpdateView(UpdateView):
    model=BookStoreModel
    template_name='store_book.html'
    form_class=BookStoreForm
    success_url=reverse_lazy('show_books')
    
    
# ----------------------********** a simple divider **********--------------------------------------    
#function based view:
# def delete_book(request,id):
#     book=BookStoreModel.objects.get(pk=id).delete()
#     return redirect('show_books')

##class based view:
##delete view:
from django.views.generic.edit import DeleteView
class DeleteBookView(DeleteView):
    model=BookStoreModel
    template_name='delete_conf.html'
    success_url=reverse_lazy('show_books')

    


    


# ----------------------********** a simple divider **********--------------------------------------


#class based view:
# detail view:
from django.views.generic import DetailView
class BookDetailView(DetailView):
    model=BookStoreModel
    template_name='book_detail.html'
    context_object_name='item'
    pk_url_kwarg='id'



