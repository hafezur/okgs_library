from django.db import models

# Create your models here.
class BookStoreModel(models.Model):
    CATEGORY=(
        ('Mystery','Mystery'),
        ('Thriller','Thriller'),
        ('Sci-Fi','Sci-Fi'),
        ('Humor','Humor'),
        ('Horror','Horror'),
    )
    id=models.IntegerField(primary_key=True)
    book_name=models.CharField(max_length=30)
    author=models.CharField(max_length=30)
    category=models.CharField(max_length=30,choices=CATEGORY)
    first_pub=models.DateTimeField(auto_now_add=True)# akdom first date dakhabe
    last_pub=models.DateTimeField(auto_now=True) # erpor thaka joto updata korbo sei date dakhabe.
    book_image=models.ImageField(blank=True,null=True)
    


from django.db import models

class UserRegistration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    present_address = models.TextField()
    permanent_address = models.TextField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # store hashed later
    is_staff = models.BooleanField(default=False)
    profile_picture=models.ImageField(upload_to='photo/profile_picture',blank=True,null=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    def __str__(self):
        return self.email
    
    