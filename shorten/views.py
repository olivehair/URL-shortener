from rest_framework.generics import CreateAPIView, RetrieveAPIView

import hashlib

from shorten.models import ShortUrl
from shorten.serializers import ShortUrlSerializer


class CreateShortUrl(CreateAPIView):
    serializer_class = ShortUrlSerializer

    def perform_create(self, serializer):
        complete_url = serializer.validated_data['complete_url']
        short_url = "https://bitly/" + hashlib.md5(complete_url.encode('utf-8')).hexdigest()
        serializer.save(short_url=short_url)


class RetrieveShortUrl(RetrieveAPIView):
    serializer_class = ShortUrlSerializer
    queryset = ShortUrl.objects.all()
    lookup_field = 'complete_url'
