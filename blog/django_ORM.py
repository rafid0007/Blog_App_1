from blog.models import post
from django.contrib.auth.models import User

a = post.objects.all()
print(a)