from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)
   
    def __str__(self):
        return self.name
    
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    avatar = models.ImageField(upload_to='author_avatars/', null=True, blank=True)

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_posted = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    categories = models.ManyToManyField(Category, related_name='blog_posts')
    tags = models.ManyToManyField(Tag, related_name='blog_posts')

    def __str__(self):
        return self.title

class Industry(models.Model):
    title = models.CharField(max_length=200)  # Yeni eklenen alan
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='industry_images/', null=True, blank=True)
    # Diğer alanları da buraya ekleyebilirsiniz.

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(BlogPost, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    website = models.CharField(max_length=50,default="")
    date_commented = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return f"{self.author.name} - {self.date_commented}"




# class Industry(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     image = models.ImageField(upload_to='Industry_images/')