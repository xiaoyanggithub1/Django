from rest_framework import serializers

from upload_common.models import HomeIcon,Order


class HomeIconuSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeIcon
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

