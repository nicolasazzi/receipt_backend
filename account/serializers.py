from rest_framework import serializers

from .models import Account

class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['first_name', 'last_name', 'phone_number', 'password']

        extra_kwargs  = {
            'password': {'write_only': True}
        }

    def save(self):
        account = Account(
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            phone_number=self.validated_data['phone_number'],
        )

        account.set_password(self.validated_data['password'])
        account.save()
        return account