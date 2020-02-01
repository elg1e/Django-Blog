from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm

def get_posts(request):
    """
    Create a view that will return a list
    of posts that were published prior to 'now'
    and render them in 'blogposts.html' template
    """

def post_detail(request, pk):
    """
    Create a view that returns a single 
    Post object based on the post id(pk) and 
    render it to the 'postdetail.html' template.
    Or return a 404 error if not found.
    """

