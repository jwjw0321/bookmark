from django.db import models
from django.urls import reverse


class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    def __str__(self):
        #  객체를 출력할 때 나타날 값
        return "이름 : " + self.site_name + ", 주소 : " + self.url

    # 북마크 수정 기능 구현할 때, 수정을 완료한 후에 돌아갈 페이지의 값을 지정해준다.
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])