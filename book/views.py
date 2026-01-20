from django.shortcuts import render,redirect
from book.forms import BookStoreForm
from book.models import BookStoreModel



#function base view
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
    #login check
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

    
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import BookStoreModel
from .forms import BookStoreForm

def update_book(request, id):
    book = get_object_or_404(BookStoreModel, id=id)

    user_id = request.session.get("user_id")
    is_adm = None

    if user_id:
        try:
            user = UserRegistration.objects.get(id=user_id)
            is_adm = user.is_admin
        except UserRegistration.DoesNotExist:
            pass

    # --- FORM LOGIC (always define form) ---
    if request.method == "POST":
        form = BookStoreForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('show_books')
    else:
        is_adm=is_adm
        form = BookStoreForm(instance=book)

        context = {
            'is_adm': is_adm,
            'form': form,
            'book': book
        }

        return render(request, 'store_book.html', context)


    
    

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

    


    


# ----------------------**********      a simple divider     **********-----------------------------



def book_detail_view(request, id):
    item = get_object_or_404(BookStoreModel, id=id)

    user = None
    user1 = None

    user_id = request.session.get("user_id")
    if user_id:
        user = UserRegistration.objects.get(id=user_id)
        if user:
            user1 = user.first_name
            is_adm=user.is_admin

    context = {
        'user1': user1,
        'custom_user': user,   # rename for avoid conflict
        'item': item,
        'is_adm': is_adm,
    }

    return render(request, 'book_detail.html', context)


def show_stock(request):
    all_stock=BookStoreModel.objects.all()
    
    context={
        'all_book':all_stock,
    }
    return render(request,'admin/stock.html',context)




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


from django.shortcuts import render
from .models import UserRegistration

def dashboard_function(request):
    user_id = request.session.get("user_id")  # get logged-in user
    user1 = profile_picture = email = city = region = country = varified_user = None
    all_book=BookStoreModel.objects.all()

    if user_id:
        all_category=Category.objects.all()
        try:
            authenticate_user = UserRegistration.objects.get(id=user_id)
            if authenticate_user.is_active:
                varified_user = authenticate_user
                user1 = authenticate_user.first_name
                profile_picture = authenticate_user.profile_picture
                email = authenticate_user.email
                city = authenticate_user.city
                region = authenticate_user.region
                country = authenticate_user.country
                is_adm=authenticate_user.is_admin
        except UserRegistration.DoesNotExist:
            pass  # user1 etc. remain None
    
    context = {
        'user1': user1,
        'profile_picture': profile_picture,
        'email': email,
        'city': city,
        'region': region,
        'country': country,
        'varified_user': varified_user,
        'is_adm': is_adm,
        'all_book': all_book,
        'all_category': all_category,
    }
    return render(request, 'dashboard.html', context)

    


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

from django.shortcuts import redirect
from django.contrib import messages
from .models import UserRegistration

def update_profile_picture(request):
    user_id = request.session.get("user_id")
    if user_id and request.method == "POST":
        try:
            user = UserRegistration.objects.get(id=user_id)
            if 'profile_picture' in request.FILES:
                user.profile_picture = request.FILES['profile_picture']
                user.save()
                messages.success(request, "Profile picture updated successfully!")
        except UserRegistration.DoesNotExist:
            messages.error(request, "User not found.")
    return redirect('dashboard')



def read_book(request, book_id):
    book = get_object_or_404(BookStoreModel, id=book_id)
    admin=UserRegistration.objects.get(is_admin=True)
    return render(request, 'read_book.html', {'book': book,'admin':admin})

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Category

def add_category(request):
    user_id = request.session.get("user_id")
    varified_user = UserRegistration.objects.get(id=user_id)
    user1=varified_user.first_name
    is_adm=varified_user.is_admin
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        is_active = request.POST.get("is_active")

        category_image = request.FILES.get("category_image")

        # Checkbox handling
        if is_active:
            is_active = True
        else:
            is_active = False

        # Create Category
        Category.objects.create(
            name=name,
            description=description,
            category_image=category_image,
            is_active=is_active
        )

        messages.success(request, "Category added successfully!")
        return redirect("add_category")
    context={
        'user1':user1,
        'is_adm':is_adm,
    }
    return render(request, "admin/add_category.html",context)


def show_category(request):
    user_id = request.session.get("user_id")
    varified_user = UserRegistration.objects.get(id=user_id)
    user1=varified_user.first_name
    is_adm=varified_user.is_admin
    all_category=Category.objects.all()
    context={
        'user1':user1,
        'is_adm':is_adm,
        'category':all_category,
    }
    return render(request, "category/category_list.html",context)
def show_stock(request):
    user_id = request.session.get("user_id")
    varified_user = UserRegistration.objects.get(id=user_id)
    user1=varified_user.first_name
    is_adm=varified_user.is_admin
    all_books=BookStoreModel.objects.all()
    context={
        'user1':user1,
        'is_adm':is_adm,
        'all_books':all_books,
    }
    return render(request, "category/stock_list.html",context)
