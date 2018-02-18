from django.conf.urls import url
from django.conf.urls import include
from . import views


urlpatterns = [
	# Lista de Filmes
	url(r'^$', views.FilmeListView.as_view(), name='filmes'),

	# Detalhe de filme
	url(r'^filme/(?P<pk>\d+)/$', views.FilmeDetailView.as_view(), name='filme_detalhe_pk'),
	url(r'^filme/(?P<slug>[-\w]+)/$', views.FilmeDetailView.as_view(), name='filme_detalhe_slug'),

	# Detalhe de ator
	url(r'^ator/(?P<slug>[-\w]+)/$', views.AtorDetailView.as_view(), name='ator'),

	# Adicionar likes
	url(r'^adicionar/like/(?P<pk>\d+)/$', views.AdicionarLikeFilme, name='adicionar_like_filme_pk'),
	url(r'^adicionar/like/(?P<slug>[-\w]+)/$', views.AdicionarLikeFilme, name='adicionar_like_filme_slug'),
]