from django.views.generic import ListView, DetailView

from ..config import POSTS_PER_PAGE
from ..models import Post
from ..service import get_posts
from .utils import FillContextMixin


class PostListView(FillContextMixin, ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = POSTS_PER_PAGE

    def get_queryset(self):
        search_query = self.request.GET.get('search')
        return get_posts(search_query)


class PostDetailView(FillContextMixin, DetailView):
    template_name = 'blog/post_detail.html'

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Post.objects.filter(is_published=True, slug=slug)
