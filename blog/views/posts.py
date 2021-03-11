from django.views.generic import ListView, DetailView

from ..config import POSTS_PER_PAGE
from ..models import Post
from .utils import MixinFillContext


class PostListView(MixinFillContext, ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    queryset = Post.objects.filter(is_published=True)
    paginate_by = POSTS_PER_PAGE


class PostDetailView(MixinFillContext, DetailView):
    template_name = 'blog/post_detail.html'

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Post.objects.filter(is_published=True, slug=slug)
