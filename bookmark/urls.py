from django.urls import path
# from .views import BookmarkListView, BookmarkCreateView, BookmarkDeleteView, BookmarkDetailView, BookmarkUpdateView
from .views import *

urlpatterns = [
    # 클래스형 뷰, 함수형 뷰는 path에 쓸 때 이름이 다름
    # path(url 패턴, 뷰, url패턴의 이름),

    # 함수형: 뷰이름만
    # path('', BookmarkListView, name='list'),

    # 클래스형: 뷰이름.as_view()
    path('',                    BookmarkListView.as_view(),     name='list'),
    path('add/',                BookmarkCreateView.as_view(),   name='add'),
    path('update/<int:pk>/',    BookmarkUpdateView.as_view(),   name='update'),
    # Primary Key: int:pk, 게시글 번호 같은거
    path('detail/<int:pk>/',    BookmarkDetailView.as_view(),   name='detail'),
    path('delete/<int:pk>/',    BookmarkDeleteView.as_view(),   name='delete'),
    # int, str, slug, path...: 필터 - Custom


]