from django.views.generic import ListView, DetailView

from .models import Post


class PostListView(ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    queryset = Post.objects.filter(is_published=True)
    paginate_by = 5


class PostDetailView(DetailView):
    template_name = 'blog/post_detail.html'

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Post.objects.filter(is_published=True, slug=slug)
