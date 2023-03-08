#!/usr/bin/env python

from .models import Netlify
from .serializers import NetlifySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
import logging

logging.basicConfig(level="DEBUG")

class CustomPageNumberPagination(PageNumberPagination):

    def get_paginated_response(self, data):

        response = Response(
            {
                'status': status.HTTP_200_OK,        
                'total_nr_of_records': self.page.paginator.count,
                'nr_of_pages': self.page.paginator.num_pages,
                'page_size': self.page_size,
            }
        )
        
        if (self.page.has_next()):
            response.data['next'] = self.get_next_link()

        if (self.page.has_previous()):
            response.data['previous'] = self.get_previous_link()

        response.data['data'] = data
        
        return response
    
# class CustomPagination(PageNumberPagination):

#     def get_paginated_response(self, data):
#         return Response({
#             'links': {
#                 'next': self.get_next_link(),
#                 'previous': self.get_previous_link()
#             },
#             'count': self.page.paginator.count,
#             'results': data
#         })


class NetlifyListApiView(ListAPIView):

    # def get(self, request, format=None):
    #     queryset = Netlify.objects.all()
    #     serializer_class = NetlifySerializer
    #     pagination_class = CustomPageNumberPagination

    #     return pagination_class.get_paginated_response(self, queryset)

    def get_queryset(self):
        return Netlify.objects.all()

    def get(self, request, format=None):
        '''
        List all the netlify items
        '''

        netlifyList = self.get_queryset()
        results = NetlifySerializer(netlifyList, many=True).data
        return Response(results)

    #     # return customPagination.get_paginated_response(customPagination.page)

    #     return CustomPageNumberPagination.get_paginated_response(serializer.data)

    #     # return self.get_paginated_response(serializer.data)
