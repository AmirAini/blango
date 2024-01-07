from rest_framework.throttling import AnonRateThrottle, UserRateThrottle

class AnonSustainedThrottle(AnonRateThrottle):
    #long-term
    scope = "anon_sustained"


class AnonBurstThrottle(AnonRateThrottle):
    #short-term
    scope = "anon_burst"

class UserSustainedThrottle(UserRateThrottle):
    scope = "user_sustained"


class UserBurstThrottle(UserRateThrottle):
    scope = "user_burst"