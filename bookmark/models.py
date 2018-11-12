from django.db import models

# Create your models here.

# 모델: 데이터베이스의 묘사 - 어떤 테이블, 어떤 컬럼, 어떤 제약 조건 등등
# 회원관리: 유저DB


# models.Model
# 장고에서 모델은 ORM이란 기능을 통해서 프로그래머가 SQL을 몰라도 DB를 사용할 수 있도록 도와줌
# Object Related Management
# models.Model은 실제적인 기능 함수를 가지고 있음

# 모델까지 만들었을 경우, 아직 DB에 반영 안된 상태
# makemigrations, migrate
# python manage.py makemigrations bookmark
# python manage.py sqlmigrate bookmark 0001 (필수는 아님)
# python manage.py migrate bookmark 0001

# DB에 직접 전근하는 방법: python manage.py dbshell
# 데이터베이스에 간접적으로 접근하는 방법(모델을 이용): python manage.py shell


class Bookmark(models.Model):

    # 클래스 변수, 속성: DB 칼럼
    # 문자열, 숫자, Boolean, Binary ...
    # 각 필드의 제약 조건: 컬럼의 제약 조건

    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')


    # CharField, TextField ...
    # 필드 종류: 프론트 페이지에서 어떤 폼 태그를 사용할 것인지, 폼 태그에서 제약 조건

    def __str__(self):
        # 객체를 출력할 때 나타날 값
        return "Name: " + self.site_name + ", Address: " + self.url

    # 모델 내부의 methods는 필드처럼 사용될 수 있음

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('detail', args=[str(self.id)])

    # 다양한 정보를 갖는 클래스, 해당 모델의 옵션값 설정
    class Meta:
        ordering = ['site_name']


