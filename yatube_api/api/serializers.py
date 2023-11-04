from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator


from posts.models import Comment, Follow, Group, Post, User


class BaseAuthorSerializer(serializers.ModelSerializer):
    """Base serializer with read only field 'author'."""

    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )


class PostSerializer(BaseAuthorSerializer):
    """Serializer for posts."""

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(BaseAuthorSerializer):
    """Serializer for comments."""

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):
    """Serializer for groups."""

    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    """Serializer for follows with unique validation."""

    user = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')
        # Check unique combination of fields
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following')
            )
        ]

    def validate(self, data):
        """Check inequality fields."""
        if data['user'] == data['following']:
            raise serializers.ValidationError(
                'Подписаться на самого себя нельзя!')
        return data
