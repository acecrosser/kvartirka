from .views import PostSet, CommentsSet, CommentParentChildren, PostShowThreeComments
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'post', PostSet, 'post')
router.register(r'comment', CommentsSet, 'comment')
router.register(r'three_comments', CommentParentChildren, 'three_comments')
router.register(r'post_three_comments', PostShowThreeComments, 'post_three_comments')
urlpatterns =router.urls