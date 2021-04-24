from rest_framework import serializers

from store.models import Store
from django.contrib.auth.models import User


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ('id','title', 'content', 'author')

    def delete(self):
        id = self.data.get('id')
        book = Store.objects.get(pk=id)
        book.delete()


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", 'email', "password", "password2"]

    def save(self, **kwargs):
        user = User(
            email = self.validated_data.get('email'),
            username = self.validated_data.get('username')
        )
        if self.validated_data.get('password') != self.validated_data.get('password2'):
            raise serializers.ValidationError({
                'password': 'passwords doesnt match'
            })
        else:
            user.set_password(self.validated_data.get('password'))
            user.save()
