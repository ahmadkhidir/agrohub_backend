from rest_framework import serializers


class CropRecommendationRequestSerializer(serializers.Serializer):
    temperature = serializers.ListField(
        child=serializers.FloatField()
    )
    rainfall = serializers.ListField(
        child=serializers.FloatField()
    )
    humidity = serializers.ListField(
        child=serializers.FloatField()
    )
    wind = serializers.ListField(
        child=serializers.FloatField()
    )
    crop = serializers.ListField(
        child=serializers.CharField()
    )

    def validate(self, attrs):
        if not (len(attrs['temperature']) == len(attrs['rainfall']) == len(attrs['humidity']) == len(attrs['wind']) == len(attrs['crop'])):
            raise serializers.ValidationError("Fields must be of equal length")
        return attrs
