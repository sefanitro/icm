from rest_framework import serializers

class ICMSerializer(serializers.Serializer):
    stacks = serializers.ListField( child = serializers.IntegerField() )
    payouts = serializers.ListField( child = serializers.FloatField() )

class ChanceSerializer(serializers.Serializer):
    chance = serializers.FloatField()

class ICMResponseSerializer(serializers.Serializer):
    chance = serializers.ListField( child = serializers.FloatField() )