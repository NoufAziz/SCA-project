from django.conf.urls import url
from project import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #/StudentsClubAcademy
    url(r'^subject/(?P<Subject_id>\d+)/$', views.show_Subject, name='show_subject'),
    #/StudentsClubAcademy/Subject/1/
    url(r'^cource/(?P<Cource_id>\d+)/$', views.show_Cource, name='show_cource'),
    #/StudentsClubAcademy/Cource/1/
    url(r'^cource/(?P<Cource_id>\d+)/comment/$', views.C_comment, name='c_comment'),
    #/StudentsClubAcademy/Cource/1/comment/
    url(r'^lecture/(?P<Lecture_id>\d+)/$', views.show_Lecture, name='show_lecture'),
    #/StudentsClubAcademy/Lecture/1/
    url(r'^lecture/(?P<Lecture_id>\d+)/comment/$', views.L_comment, name='l_comment'),
    #/StudentsClubAcademy/Lecture/1/comment/

]
