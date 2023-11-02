from django.contrib.auth import get_user_model
from django.db import models

from posts.constants import STRING_LENGTH_LIMIT

User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey('Group', on_delete=models.SET_NULL, null=True)

    class Meta:
        default_related_name = 'posts'

    def __str__(self):
        return self.text[:STRING_LENGTH_LIMIT]


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        default_related_name = 'comments'

    def __str__(self):
        return f'{self.author} к {self.post}: {self.text[:STRING_LENGTH_LIMIT]}'


class Group(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=16)
    description = models.TextField()

    def __str__(self):
        return self.title[:STRING_LENGTH_LIMIT]


class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_user_following'
            )
        ]

    def __str__(self):
        return f'{self.user} подписан на {self.following}'
