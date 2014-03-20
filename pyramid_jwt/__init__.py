import jwt
from zope.interface import implementer
from pyramid.httpexceptions import HTTPUnauthorized
from pyramid.authentication import CallbackAuthenticationPolicy
from pyramid.interfaces import IAuthenticationPolicy


@implementer(IAuthenticationPolicy)
class JwtAuthenticationPolicy(CallbackAuthenticationPolicy):

    def __init__(self, secret, callback=None, alg=None,
                 timeout=None, leeway=None, debug=False):
        self.secret = secret
        self.callback = callback
        self.alg = alg
        self.timeout = timeout
        self.leeway = leeway
        self.debug = debug

    def remember(self, request, payload):
        if self.timeout:
            payload['exp'] = self.timeout
        return jwt.encode(payload, self.secret, self.alg)

    def forget(self, request):
        return []

    def unauthenticated_userid(self, request):
        token = request.headers.get('Authorization', None)
        if token:
            try:
                data = jwt.decode(token, self.secret, self.leeway)
                return data
            except (jwt.DecodeError, jwt.ExpiredSignature):
                raise HTTPUnauthorized()
        return None
