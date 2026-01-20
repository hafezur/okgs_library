from django.db import models

# Create your models here.
from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=180, unique=True, blank=True)
    description = models.TextField(blank=True, null=True)
    category_image=models.ImageField(blank=True,null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Category.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

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
    

from django.db import models

class BookStoreModel(models.Model):
    CATEGORY = (
        ('Mystery','Mystery'),
        ('Thriller','Thriller'),
        ('Sci-Fi','Sci-Fi'),
        ('Humor','Humor'),
        ('Horror','Horror'),
    )

    id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="books")
    first_pub = models.DateTimeField(auto_now_add=True)
    last_pub = models.DateTimeField(auto_now=True)
    book_image = models.ImageField(blank=True,null=True)
    book_pdf = models.FileField(upload_to='book_pdfs/', blank=True,null=True)
    stock = models.IntegerField(blank=True,null=True)
    is_order = models.BooleanField(blank=True,null=True,default=False)
    price = models.IntegerField(blank=True,null=True)


    def __str__(self):
        return self.book_name

class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(UserRegistration, on_delete=models.CASCADE, related_name="orders")
    book = models.ForeignKey(BookStoreModel, on_delete=models.CASCADE, related_name="orders")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="orders")

    quantity = models.PositiveIntegerField(default=1)
    total_price = models.IntegerField()
    status = models.CharField(max_length=20, choices=STATUS, default='Pending')

    ordered_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.total_price = self.book.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.email} - {self.book.book_name}"
