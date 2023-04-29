from rest_framework import serializers
class serializeremployee(serializers.Serializer):
    name=serializers.CharField(max_length=30 )
    email=serializers.EmailField(max_length=30)
    password=serializers.CharField(max_length=30)
    
    
class useremployee(serializers.Serializer):
    first_name=serializers.CharField(max_length=30)
    email=serializers.EmailField(max_length=30)
    password=serializers.CharField(max_length=30)