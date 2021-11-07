from rest_framework import serializers
from .models import User, AdvisorModel, BookingAdvisorModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name','email','password']
        extra_kwargs = {'password':{'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdvisorModel
        fields = ("__all__")


class BookingSerializer(serializers.ModelSerializer):
    booking = AdvisorSerializer(read_only=True,many=True)
    class Meta:
        depth = 1
        model = BookingAdvisorModel
        fields = ("__all__")
