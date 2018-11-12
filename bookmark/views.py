from django.shortcuts import render

# Create your views here.

# MTV: 디자인 패턴 -> 설계상의 문제를 해결하기 위해 나온 방법
# Model - DB를 쉽게 사용
# Template - HTML같이 프론트 코드와 연동
# View - 로직, 기능 같은 백엔드 코드

# 리스트 페이지
# DB에서 북마크 불러오기 - 모델
# 해당 북마크를 템플릿에 넣어 가공하기 - 로직
# 가공한 결과 코드를 사용자(브라우저)에게 전달하기 - 로직
# 3가지는 모두 뷰(view)에서 이루어짐

# 뷰
# 1. 클래스형 뷰: class 형태 -> 보통 하는 일
# 2. 함수형 뷰: def 형태 -> 내가 혼자 지지고 볶고 하고 싶을때
# 보통 하는 일을 하는 뷰는 장고가 미리 만들어 뒀음: Generic View
# Generic View -> CRUD(Create Read Update Delete) - Class based view

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Bookmark
from django.urls import reverse_lazy

# Generic 뷰의 기본 템플릿 규칙
# 1. 앱 폴더 하위 templates 폴더 안에 [모델이름] 폴더에서 찾음
# - bookmark/templates/bookmark/[모델이름]
# 2. ListView - 모델명_list.html(bookmark_list.html)
# 3. CreateView, UpdateView - 모델명_form.html(bookmark_form.html)


# Ajax 뷰 - JsonResponse, HttpResponse

# 클래스 뷰를 써도 옵션은 존재
class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 3

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list') # 'list'는 urls.py에 있음
    template_name_suffix = '_create'

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    # success_url = reverse_lazy('list')  # 'list'는 urls.py에 있음
    template_name_suffix = '_update'

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')
    template_name_suffix = '_delete'
    # reverse: URL 패턴 이름을 가지고 URL을 만드는 함수
    # reverse_lazy(지연 평가) : 똑같은데, //클래스형 뷰는 무조건 reverse_lazy//
    # 클래스 형 뷰가 URLConf 로드 전에 평가됨
    # 장고 애플리케이션 구동이 될 때 URLConf를 로드 해야함

