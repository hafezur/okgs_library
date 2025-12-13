from django.shortcuts import render,redirect
from book.forms import BookStoreForm
from book.models import BookStoreModel



#class base view
from .models import UserRegistration

def homepage_view1(request):
    user_id = request.session.get("user_id")

    if user_id:
        try:
            user = UserRegistration.objects.get(id=user_id)
            user1 = user.first_name
        except UserRegistration.DoesNotExist:
            user1 = None
    else:
        user1 = None

    context = {
        'user1': user1,
    }
    return render(request, 'part_of_index.html', context)



"""from django.views.generic import TemplateView
class my_template_view(TemplateView):
    template_name='part_of_index.html'  """
from django.views.generic import TemplateView
def Combinelogin_interface(request):
    return render(request, 'login_interface.html')
    

class userInterfaceView(TemplateView):
     template_name ='user_interface.html'



from django.views.generic.edit import CreateView
from django.urls import reverse_lazy # complex url k simple kore.

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import BookStoreModel
from .forms import BookStoreForm


from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import UserRegistration
from .forms import BookStoreForm

def book_form_view(request):
    # 🔐 login check
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("user_login")

    try:
        user = UserRegistration.objects.get(id=user_id)
        user1 = user.first_name
    except UserRegistration.DoesNotExist:
        return redirect("user_login")

    if request.method == "POST":
        form = BookStoreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('show_books'))
    else:
        form = BookStoreForm()

    context = {
        'form': form,
        'user1': user1,
    }
    return render(request, 'store_book.html', context)


from book.models import BookStoreModel, UserRegistration

def show_books(request):
    all_books = BookStoreModel.objects.all()

    user_id = request.session.get("user_id")

    if user_id:
        try:
            user = UserRegistration.objects.get(id=user_id)
            user1 = user.first_name
        except UserRegistration.DoesNotExist:
            user1 = None
    else:
        user1 = None

    context = {
        'all_book': all_books,
        'user1': user1,
    }
    return render(request, 'show_book.html', context)

    
from django.views.generic.edit import UpdateView
class BookUpdateView(UpdateView):
    model=BookStoreModel
    template_name='store_book.html'
    form_class=BookStoreForm
    success_url=reverse_lazy('show_books')
    
    

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import BookStoreModel, UserRegistration

def delete_book(request, pk):
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("user_login")

    try:
        user = UserRegistration.objects.get(id=user_id)
        user1 = user.first_name
    except UserRegistration.DoesNotExist:
        return redirect("user_login")

    book = get_object_or_404(BookStoreModel, pk=pk)

    if request.method == "POST":
        book.delete()
        return redirect(reverse_lazy("show_books"))

    context = {
        'book': book,
        'user1': user1,
    }
    return render(request, "delete_conf.html", context)

    


    


# ----------------------********** a simple divider **********--------------------------------------


#class based view:
# detail view:
from django.views.generic import DetailView
class BookDetailView(DetailView):
    model=BookStoreModel
    template_name='book_detail.html'
    context_object_name='item'
    pk_url_kwarg='id'

def News_Events(request):
    user_id = request.session.get("user_id")

    if user_id:
        try:
            user = UserRegistration.objects.get(id=user_id)
            user1 = user.first_name
        except UserRegistration.DoesNotExist:
            user1 = None
    else:
        user1 = None

    context = {
        'user1': user1
    }
    return render(request, 'news&event.html', context)
 


from django.shortcuts import render, redirect
from .forms import RegistrationForm

def user_register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():

            # Normally you should hash password
            user = form.save(commit=False)
            user.password = form.cleaned_data['password']
            user.save()

            return redirect("login_interface")   # redirect after success
    else:
        form = RegistrationForm()

    return render(request, "registration.html", {"form": form})




def contact(request):
    user_id = request.session.get("user_id")

    if user_id:
        try:
            user = UserRegistration.objects.get(id=user_id)
            user1 = user.first_name
        except UserRegistration.DoesNotExist:
            user1 = None
    else:
        user1 = None

    context = {
        'user1': user1
    }
    return render(request, 'contact.html', context)


"""
def contact(request):
    authenticate_user=UserRegistration.objects.all().first()
    if authenticate_user ==None:
        user1=None
    else:
        user1=authenticate_user.is_active
    context={
        'user1':user1,
    }
    return render(request, 'contact.html',context)

"""

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserRegistration

def user_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = UserRegistration.objects.get(email=email)

            if user.password == password:
                # Save session
                request.session["user_id"] = user.id
                request.session["user_email"] = user.email

                # Correct way to update user field
                user.is_active = True
                user.save()

                messages.success(request, "Login successful!")
                return redirect("dashboard")

            else:
                messages.error(request, "Incorrect password!")

        except UserRegistration.DoesNotExist:
            messages.error(request, "No account found with this email!")

    return render(request, "user_interface.html")


from .models import UserRegistration
def dashboard_function(request):
     authenticate_user=UserRegistration.objects.all().first()
     if authenticate_user.is_active == False:
        user1=None
     else:
        varified_user=authenticate_user
        user1=authenticate_user.first_name
        profile_picture=authenticate_user.profile_picture
        email=authenticate_user.email
        city=authenticate_user.city
        region=authenticate_user.region
        country=authenticate_user.country
     context={
         'user1':user1,
         'profile_picture':profile_picture,
         'email':email,
         'city':city,
         'region':region,
         'country':country,
         'varified_user':varified_user,
     }
     return render(request,'dashboard.html',context)

    


from django.shortcuts import render,redirect

from book.models import UserRegistration
def homepage_view(request):
    authenticate_user=UserRegistration.objects.all().first()
    if authenticate_user ==None:
        user1=None
    else:
        user1=authenticate_user.first_name
    context={
        'user1': user1,
    }
    return render(request,'part_of_index.html',context)

from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .models import UserRegistration

from django.contrib.auth import logout

from django.contrib.auth import logout
from django.contrib import messages
from .models import UserRegistration

def user_logout(request):
    user_id = request.session.get("user_id")

    if user_id:
        try:
            user = UserRegistration.objects.get(id=user_id)
            user.is_active = False
            user.save()
        except UserRegistration.DoesNotExist:
            pass

    request.session.flush()
    messages.success(request, "You are logged out.")
    return redirect("user_login")



"""
from django.shortcuts import redirect
from django.contrib import messages

def user_logout(request):
    # Clear all session data
    request.session.flush()

    messages.success(request, "You have been logged out successfully!")
    return redirect("user_login")   # redirect to your login page

"""



