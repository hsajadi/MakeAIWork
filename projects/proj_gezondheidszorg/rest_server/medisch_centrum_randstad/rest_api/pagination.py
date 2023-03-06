from rest_framework import pagination

class CustomPageNumberPagination(pagination.PageNumberPagination):
    """Custom page number pagination."""

    def get_paginated_response(self, data):

        response = Response(
            {
                'status': status.HTTP_200_OK,
                'total_nr_of_records': self.page.paginator.count,
                'nr_of_pages': self.page.paginator.num_pages,
                'page_size': self.page_size,
                'results': data
            }
        )

        if (self.page.has_next()):
            response.data['next'] = self.get_next_link()
        
        if (self.page.has_previous()):
            response.data['previous'] = self.get_previous_link()

        response.data['data'] = data

        # return response

        return super(CustomPageNumberPagination, self).get_page_size(request)