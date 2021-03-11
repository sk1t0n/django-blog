from django.views.generic import View

from ..service import get_recent_posts, get_all_tags


def fill_context(context: dict) -> dict:
    context['recent_posts'] = get_recent_posts()
    context['all_tags'] = get_all_tags()
    return context


class MixinFillContext(View):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        fill_context(context)
        return context
