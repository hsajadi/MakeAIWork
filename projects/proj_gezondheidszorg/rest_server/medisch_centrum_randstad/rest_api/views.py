#!/usr/bin/env python

from .models import Netlify
from .serializers import NetlifySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .pagination import CustomPageNumberPagination
import logging

logging.basicConfig(level="DEBUG")

# class CustomPagination(PageNumberPagination):
#
#     def get_paginated_response(self, data):
#         return Response({
#             'links': {
#                 'next': self.get_next_link(),
#                 'previous': self.get_previous_link()
#             },
#             'count': self.page.paginator.count,
#             'results': data
#         })
#
#     def get_paginated_response(self, data):
#         def get_paginated_response(self, data):
#             return Response({
#                 'links': {
#                     'next': self.get_next_link(),
#                     'previous': self.get_previous_link()
#                 },
#                 'count': self.page.paginator.count,
#                 'results': data
#             })
#
#         # response = Response(
#         #     {
#         #         'status': status.HTTP_200_OK,
#         #         'total_nr_of_records': self.page.paginator.count,
#         #         'nr_of_pages': self.page.paginator.num_pages,
#         #         'page_size': self.page_size,
#         #         'results': data
#         #     }
#         # )
#
#         # if (self.page.has_next()):
#         #     response.data['next'] = self.get_next_link()
#         #
#         # if (self.page.has_previous()):
#         #     response.data['previous'] = self.get_previous_link()
#
#         # response.data['data'] = data
#
#         return response


class NetlifyListApiView(APIView):

    def get(self, request, format=None):
        '''
        List all the netlify items
        '''

        netlifyList = Netlify.objects.all()
        results = netlifyList
        serializer = NetlifySerializer(results, many=True)

        customPagination = CustomPageNumberPagination()
        return customPagination.paginate_queryset(serializer.data, request)

        # return customPagination.get_paginated_response(customPagination.page)

        # return customPagination.get_paginated_response(serializer.data)

        # return self.get_paginated_response(serializer.data)
