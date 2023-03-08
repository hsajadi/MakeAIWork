from rest_framework import pagination
from rest_framework.response import Response
from collections import OrderedDict
from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):

    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 5
    page_query_param = 'age'

    def get_paginated_response(self, data):

        response = Response(data)
        response["status"] = status.HTTP_200_OK
        response["count"] = self.page.paginator.count

        # (
        #     {
        #         'status': status.HTTP_200_OK,
        #         'page_number': self.get_page_number,
        #         'page_size': self.get_page_size,
        #         'links': {
        #             'next': self.get_next_link(),
        #             'previous': self.get_previous_link()
        #         },
        #         'count': self.page.paginator.count,
        #         'total_pages': self.page.paginator.num_pages
        #     }
        # )

        # response = Response(data)
        # response['count'] = self.page.paginator.count
        # response['next'] = self.get_next_link()
        # response['previous'] = self.get_previous_link()

        return response
