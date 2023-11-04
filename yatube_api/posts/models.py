from django.contrib.auth import get_user_model
from django.db import models

from posts.constants import STRING_LENGTH_LIMIT

User = get_user_model()


class AuthorTextModel(models.Model):
    """Abstract model with fields text and author."""

    text = models.TextField('Текст')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Автор')

    class Meta:
        abstract = True


class Post(AuthorTextModel):
    """Model to describe a post."""

    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True)
    image = models.ImageField(
        'Изображение', upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(
        'Group',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Сообщество'
    )

    class Meta:
        default_related_name = 'posts'
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ('pub_date',)

    def __str__(self):
        return self.text[:STRING_LENGTH_LIMIT]


class Comment(AuthorTextModel):
    """Model to describe comments of posts."""

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, verbose_name='Пост')
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        default_related_name = 'comments'
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return (f'{self.author} к посту {self.post.id}: '
                f'{self.text[:STRING_LENGTH_LIMIT]}')


class Group(models.Model):
    """Model to describe groups of posts."""

    title = models.CharField('Название', max_length=50)
    slug = models.SlugField('Короткое название', max_length=16)
    description = models.TextField('Описание')

    class Meta:
        verbose_name = 'сообщество'
        verbose_name_plural = 'Сообщества'

    def __str__(self):
        return self.title[:STRING_LENGTH_LIMIT]


class Follow(models.Model):
    """Model to describe follows of users."""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Пользователь',
        related_name='followers',
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Подписка'
    )

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'Подписки'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_user_following'
            ),
            models.CheckConstraint(
                check=~models.Q(user=models.F('following')),
                name='no_self_follows'
            )
        ]

    def __str__(self):
        return f'{self.user} подписан на {self.following}'
