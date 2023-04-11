from collections.abc import Callable

from apps.middleware_requests_logging.models import HttpRequestsLog


class LoggingRequestsMiddleware:
    def __init__(self, get_response: Callable):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        request_path = request.build_absolute_uri()
        session_id = request.session.session_key
        user_id = request.user.id
        http_requests_log = HttpRequestsLog.objects
        if http_requests_log.filter(
            request_path=request_path,
            session_id=session_id,
            user_id=user_id,
        ).exists():
            result = http_requests_log.get(
                request_path=request_path,
                session_id=session_id,
                user_id=request.user.id,
            )
            result.counter += 1
            result.save()
        else:
            http_requests_log.create(
                request_path=request_path,
                session_id=session_id,
                user_id=request.user.id,
                counter=1,
            )
        return response
