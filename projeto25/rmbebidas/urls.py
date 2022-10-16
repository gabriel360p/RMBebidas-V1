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

	# btns
	path('defbtnlogin/',views.defbtnlogin,name="defbtnlogin"),
	path('defbtnnvproduto/',views.defbtnnvproduto,name="defbtnnvproduto"),
	path('defbtnverproduto/<int:id>',views.defbtnverproduto,name="defbtnverproduto"),
	path('defbtneditproduto/<int:id>',views.defbtneditproduto,name="defbtneditproduto"),
	path('defbtndellproduto/<int:id>',views.defbtndellproduto,name="defbtndellproduto"),
	path('defbtndellproduto/<int:id>',views.defbtndellproduto,name="defbtndellproduto"),
	path('defbtncadusuarios/',views.defbtncadusuarios,name="defbtncadusuarios"),
]
