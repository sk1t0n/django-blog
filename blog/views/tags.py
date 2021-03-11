from django.views.generic import ListView
from django.http import Http404

from ..config import POSTS_PER_PAGE
from ..models import Post, Tag
from .utils import MixinFillContext


class PostListView(MixinFillContext, ListView):
    template_name = 'blog/tag_post_list.html'
    context_object_name = 'posts'
    paginate_by = POSTS_PER_PAGE

    def get_queryset(self):
        name = self.kwargs['name']
        tag = Tag.objects.filter(name__iexact=name).first()
        if tag:
            return Post.objects.filter(tags__in=[tag.id])
        raise Http404

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_name'] = self.kwargs['name']
        return context
