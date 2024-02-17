from rest_framework import serializers

from apps.content.models import Content


class ContentSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        context = kwargs.pop('context', None)
        self.user = context.get('user')
        super().__init__(*args, **kwargs)

    rating_count = serializers.ReadOnlyField()
    rating_average = serializers.ReadOnlyField()
    user_given_rate = serializers.SerializerMethodField(read_only=True)

    def get_user_given_rate(self, obj):
        from apps.rating.models import Rating
        rating = Rating.objects.filter(user=self.user, content=obj)
        if rating.exists():
            return rating.first().rate
        return None

    class Meta:
        model = Content
        fields = '__all__'
