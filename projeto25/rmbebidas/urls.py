from django.urls import path
from . import views

app_name="rmbebidas"

urlpatterns=[
	path('',views.viewindex,name="index"),
	path('index/',views.viewindex,name="index"),
	path('tpainel/',views.viewtpainel,name="tpainel"),
	path('tproduto/',views.viewtproduto,name="tproduto"),
	path('tverproduto/',views.viewtverproduto,name="tverproduto"),
	path('tcadusuarios/',views.viewtcadusuarios,name="tcadusuarios"),
	path('tusuarios/',views.viewtusuarios,name="tusuarios"),
	path('teditusuario/<int:id>',views.viewteditusuario,name="teditusuario"),
	path('tprecos/',views.viewtprecos,name="tprecos"),
	

	# btns
	path('defbtnlogin/',views.defbtnlogin,name="defbtnlogin"),
	path('defbtnnvproduto/',views.defbtnnvproduto,name="defbtnnvproduto"),
	path('defbtnverproduto/<int:id>',views.defbtnverproduto,name="defbtnverproduto"),
	path('defbtneditproduto/<int:id>',views.defbtneditproduto,name="defbtneditproduto"),
	path('defbtndellproduto/<int:id>',views.defbtndellproduto,name="defbtndellproduto"),
	path('defbtndellproduto/<int:id>',views.defbtndellproduto,name="defbtndellproduto"),
	path('defbtncadusuarios/',views.defbtncadusuarios,name="defbtncadusuarios"),
	path('defbtndellusuario/<int:id>',views.defbtndellusuario,name="defbtndellusuario"),
	path('defbtneditusuario/<int:id>',views.defbtneditusuario,name="defbtneditusuario"),
]
