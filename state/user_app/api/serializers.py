from rest_framework import serializers
from django.contrib.auth.models import User
from user_app.models import Account


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = ['username', 'email', 'password', 'password2', 'first_name', 'last_name', 'phone_number']  # Asegúrate de separar 'last_name' y 'phone_number' con una coma
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError(
                {'error': 'Passwords don\'t match'})

        if Account.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError(
                {'error': 'Email already exists'})

        account = Account.objects.create(
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            email=self.validated_data['email'],
            username=self.validated_data['username']
        )
        account.set_password(password)  # Esta línea establece la contraseña de forma segura
        account.phone_number = self.validated_data.get('phone_number')
        account.save()
        return account

