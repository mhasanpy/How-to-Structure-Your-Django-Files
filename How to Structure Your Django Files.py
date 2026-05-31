# my_project/                   # Your project's root directory
# ├── manage.py                 # Command-line utility
# ├── db.sqlite3                # Default database file
# ├── static/                   # Global CSS, JS, images
# ├── templates/                # Global HTML templates
# ├── apps/                     # Folder to hold all your apps
# │   └── my_app/               # A specific app (e.g., 'blog')
# │       ├── migrations/       # Database change history
# │       ├── admin.py          # How the app looks in the admin panel
# │       ├── apps.py           # App configuration
# │       ├── models.py         # Defines your database tables
# │       ├── urls.py           # App-specific URL routes
# │       └── views.py          # Handles HTTP requests and logic
# └── my_project/               # Project settings package
#     ├── settings.py           # Main configuration file
#     └── urls.py               # Main URL routes




INSTALLED_APPS = [
    'django.contrib.admin',
    # ... other default apps ...
    'apps.my_app', # Add your new app here
]



print("------- Code Examples: Creating a Simple "Member" App--------")
# apps/my_app/models.py
 from django.db import models

   class Member(models.Model):
    name = models.CharField(max_length=100)  # A text field
    email = models.EmailField(unique=True)   # An email field, must be unique

    def __str__(self):
        # This defines how a member object is displayed in the admin panel
        return self.name
    

    print("---------3. Write the View Logic (views.py)-----")
    # apps/my_app/views.py
from django.shortcuts import render
from .models import Member # Import the model we just created

def member_list(request):
    # Fetch all member objects from the database
    all_members = Member.objects.all()
    # Pass the data to a template
    return render(request, 'my_app/member_list.html', {'members': all_members})


print("-------4. Define URLs (urls.py)-------")
# apps/my_app/urls.py
from django.urls import path
from . import views

# 'app_name' is used for namespacing, allowing you to reference this URL easily
app_name = 'my_app'

urlpatterns = [
    # When a user goes to '', the 'member_list' view will be called.
    # 'name' is a unique identifier for this URL.
    path('', views.member_list, name='member_list'),
]

print("-------5. Connect to Main Project (my_project/urls.py)---")

# my_project/urls.py
from django.contrib import admin
from django.urls import path, include # Don't forget to import 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    # Any URL that starts with 'members/' will be handled by the 'my_app' urls
    path('members/', include('apps.my_app.urls')),
]



print("------- Handling File Uploads--------")
# models.py
class YourModel(models.Model):
    # 'upload_to' defines the subdirectory within your media folder
    python_file = models.FileField(upload_to='user_files/')
    # ... other fields ...



    