from typing import Final
from datetime import datetime
from django.contrib.sessions.backends.cached_db import SessionStore

from django.views.generic import TemplateView

KEY__COUNT_OF_VISITS: Final[str] = "count_of_visits"
KEY__DATE_OF_VISIT_NOW = "date_of_visit_now"
KEY__PREVIOUS_DATE_OF_VISITS: Final[str] = "previous_date_of_visits"


# Create your views here.
class SessionTaskView(TemplateView):
    template_name = "session_task/index.html"

    def get_context_data(self, **kwargs):
        session: SessionStore = self.request.session
        count_of_visits = session.get(KEY__COUNT_OF_VISITS, 0)
        count_of_visits += 1
        session[KEY__COUNT_OF_VISITS] = count_of_visits

        session[KEY__PREVIOUS_DATE_OF_VISITS] = session.get(KEY__DATE_OF_VISIT_NOW)
        session[KEY__DATE_OF_VISIT_NOW] = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        context = super().get_context_data(**kwargs)
        # используется в базовом шаблоне apps/templates/_helpers/_base.html
        context["title"] = "Session task"
        #
        context["session_id"] = session.session_key
        context["session_visit_now"] = session[KEY__DATE_OF_VISIT_NOW]
        context["previous_date_of_visits"] = session[KEY__PREVIOUS_DATE_OF_VISITS]
        context["count_of_visits"] = count_of_visits
        return context
