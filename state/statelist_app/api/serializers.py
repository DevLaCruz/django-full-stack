from rest_framework import serializers
from statelist_app.models import Edification, Company, Comentary


class ComentarySerializer(serializers.ModelSerializer):
    comentary_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comentary
        exclude = ['edification']
        # fields = '__all__'


class EdificationSerializer(serializers.ModelSerializer):
    comentaries = ComentarySerializer(many=True, read_only=True)
    company_name = serializers.CharField(source='company.name')
    # length_address=serializers.SerializerMethodField()

    class Meta:
        model = Edification
        fields = '__all__'
        # fields=['id', 'country', 'active', 'image']
        # exclude=['id']


class CompanySerializer(serializers.ModelSerializer):
    edificacionlist = EdificationSerializer(many=True, read_only=True)
    # edificacionlist=serializers.StringRelatedField(many=True, read_only=True)
    # edificacionlist = serializers.PrimaryKeyRelatedField(
    #    many=True, read_only=True)
    # edificacionlist = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='edification-detail'  # Asegúrate de que este nombre de vista sea correcto
    # )

    class Meta:
        model = Company
        fields = '__all__'

    # def get_length_address(self, object):
    #     char_quatity=len(object.address)
    #     return char_quatity

    # def validate(self, data):
    #     if data['address'] == data['country']:
    #         raise serializers.ValidationError(
    #             "Address and Country cannot be the same")
    #     else:
    #         return data

    # def validate_image(self, data):
    #     if len(data) < 2:
    #         raise serializers.ValidationError(
    #             "Image URL must be greater than or equal to 2 characters")
    #     else:
    #         return data


# def column_length(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("Length must be greater than or equal to 2")


# class PropertySerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     address=serializers.CharField(validators=[column_length])
#     country=serializers.CharField(validators=[column_length])
#     description=serializers.CharField(max_length=500)
#     image=serializers.CharField(max_length=250)
#     active=serializers.BooleanField(default=True)

#     def create(self, validated_data):
#         return Property.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.address=validated_data.get('address', instance.address)
#         instance.country=validated_data.get('country', instance.country)
#         instance.description=validated_data.get('description', instance.description)
#         instance.image=validated_data.get('image', instance.image)
#         instance.active=validated_data.get('active', instance.active)
#         instance.save()
#         return instance

#     def validate(self, data):
#         if data['address']==data['country']:
#             raise serializers.ValidationError("Address and Country cannot be the same")
#         else:
#             return data

#     def validate_image(self, data):
#         if len(data)<2:
#             raise serializers.ValidationError("Image URL must be greater than or equal to 2 characters")
#         else:
#             return data
