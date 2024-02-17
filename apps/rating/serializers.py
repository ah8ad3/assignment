from rest_framework import serializers

from apps.rating.models import Rating


class RatingSerializer(serializers.ModelSerializer):
    def validate_rate(self, value):
        if value > 5 or value < 0:
            raise serializers.ValidationError("Rate must be in range of [0-5]")

        return value

    def create(self, validated_data):
        user = validated_data['user']
        content = validated_data['content']
        rate = validated_data['rate']
        
        # Check if a rating already exists for the user and content combination
        try:
            rating = Rating.objects.get(user=user, content=content)
            # Update the existing rating
            rating.rate = rate
            rating.save()
            return rating
        except Rating.DoesNotExist:
            # Create a new rating if it does not exist
            return Rating.objects.create(**validated_data)

    class Meta:
        model = Rating
        fields = ('content', 'rate', 'user')
