from django.views.generic import ListView, TemplateView

from apps.middleware_requests_logging.models import HttpRequestsLog

from django.contrib.sessions.backends.cached_db import SessionStore
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger


class RequestsLogsListView(ListView):
    paginate_by = 30
    model = HttpRequestsLog
    template_name = "middleware_requests_logging/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = HttpRequestsLog.objects.all().order_by("-id")
        paginator = Paginator(context["object_list"], self.paginate_by)

        page = self.request.GET.get("page")

        try:
            context["object_list"] = paginator.page(page)
        except PageNotAnInteger:
            context["object_list"] = paginator.page(1)
        except EmptyPage:
            context["object_list"] = paginator.page(paginator.num_pages)

        count_logs = HttpRequestsLog.objects.count()
        context["title"] = "List"
        context["count_logs"] = count_logs
        return context


class RequestsLogsListViewForSession(ListView):
    paginate_by = 30
    model = HttpRequestsLog
    template_name = "middleware_requests_logging/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        session: SessionStore = self.request.session
        session_id = session.session_key

        context["object_list"] = HttpRequestsLog.objects.filter(session_id=session_id).order_by("-id")
        paginator = Paginator(context["object_list"], self.paginate_by)

        page = self.request.GET.get("page")

        try:
            context["object_list"] = paginator.page(page)
        except PageNotAnInteger:
            context["object_list"] = paginator.page(1)
        except EmptyPage:
            context["object_list"] = paginator.page(paginator.num_pages)

        count_logs = HttpRequestsLog.objects.filter(session_id=session_id).order_by("-id").count()
        context["title"] = "List"
        context["count_logs"] = count_logs
        return context


class RequestsLogsListViewForUser(TemplateView):
    model = HttpRequestsLog
    template_name = "middleware_requests_logging/list.html"

    def get_context_data(self, username: str, **kwargs):
        context = super().get_context_data(user_id=username, **kwargs)

        context["object_list"] = HttpRequestsLog.objects.filter(user_id=username).order_by("-id")
        page = self.request.GET.get("page")

        paginator = Paginator(context["object_list"], 30)

        try:
            context["object_list"] = paginator.page(page)
        except PageNotAnInteger:
            context["object_list"] = paginator.page(1)
        except EmptyPage:
            context["object_list"] = paginator.page(paginator.num_pages)

        count_logs = HttpRequestsLog.objects.filter(user_id=username).order_by("-id").count()
        context["title"] = "List"
        context["count_logs"] = count_logs
        return context
