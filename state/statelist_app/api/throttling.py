from rest_framework.throttling import UserRateThrottle


class ComentaryCreateThrottle(UserRateThrottle):
    scope = 'comentary_create'


class ComentaryListThrottle(UserRateThrottle):
    scope = 'comentary_list'
