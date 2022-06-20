from django.http import HttpRequest, HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from typing import Any


class Logout(APIView):

    def get(
        self,
        request: HttpRequest,
        format_: Any = None
    ) -> HttpResponse:
        try:
            request.user.auth_token.delete()
        except AttributeError:
            pass
        return Response(status=status.HTTP_200_OK)
