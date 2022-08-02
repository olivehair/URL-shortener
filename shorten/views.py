import logging

from django.db import IntegrityError
from rest_framework.generics import CreateAPIView, RetrieveAPIView

import hashlib
import base64

from shorten.models import ShortUrl
from shorten.serializers import ShortUrlSerializer

logger = logging.getLogger(__name__)


class CreateShortUrl(CreateAPIView):
    serializer_class = ShortUrlSerializer

    def perform_create(self, serializer):
        hash_size = 8
        while True:
            try:
                complete_url = serializer.validated_data['complete_url']
                short_url = self.create_short_url(complete_url, hash_size)
                serializer.save(short_url=short_url)
                break
            except IntegrityError:
                hash_size += 1
                logger.exception('Short url is not unique')

    @staticmethod
    def create_short_url(complete_url, hash_size):
        hasher = hashlib.sha1(complete_url.encode('utf-8'))
        truncate_hash = base64.urlsafe_b64encode(hasher.digest()[:hash_size]).decode()
        short_url = "https://bitly/" + truncate_hash
        return short_url


class RetrieveShortUrl(RetrieveAPIView):
    serializer_class = ShortUrlSerializer
    queryset = ShortUrl.objects.all()
    lookup_field = 'complete_url'
