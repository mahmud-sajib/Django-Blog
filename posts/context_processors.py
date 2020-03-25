from .models import *

# Footer context processor
def footer_post(request):
    # Display latest posts.
    posts = Post.objects.order_by('-timestamp')[0:3]
    return {'footer_post':posts}