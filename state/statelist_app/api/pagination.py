from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


class EdificationPagination(PageNumberPagination):
    page_size = 2
    page_query_param = 'p'
    page_size_query_param = 'size'
    max_page_size = 10
    last_page_strings = 'end'


class EdificationLOPagination(LimitOffsetPagination):
    default_limit = 1
