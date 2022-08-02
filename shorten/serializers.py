from rest_framework import serializers

from shorten.models import ShortUrl


class ShortUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortUrl
        fields = ['complete_url', 'short_url',]
        read_only_fields = ('short_url',)
