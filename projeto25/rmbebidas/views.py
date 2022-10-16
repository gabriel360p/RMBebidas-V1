from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404 as error404
from . import urls
from django.http import HttpResponse
from .models import TbProdutos, TbUsuarios

#######################################################
# Usuario padrão/inicial:
# email: user@user senha: root
#######################################################

def viewindex(request):
	return render(request,'index.html')

def viewtcadusuarios(request):
	return render(request,'tcadusuarios.html')

def viewtproduto(request):
	return render(request,'tproduto.html')

def viewtverproduto(request):
	return render(request,'tverproduto.html')


def viewtpainel(request):
	produtos=TbProdutos.objects.all()
	if produtos:
		return render(request,'tpainel.html',{'PRODUTO':produtos})
	else:
		return render(request,'tpainel.html',{'PRODUTO':produtos,'vazioAlert':"Estante vazia"})

def defbtnlogin(request):
	if request.method=="POST":
		email=request.POST.get('email')
		senha=request.POST.get('senha')
		
		# procurando se esse email já existe no banco
		try:
			busca=error404(TbUsuarios,usu_email=email)
			#aqui ele verifica se a variável está vazia ou  não, se estiver é pq o email inserido não exise no banco, se não estiver é pq vc existe no banco
			if busca:
				# se ele encontrar o email, ele vai verificar se a senha esta certa
				if senha == busca.usu_senha:
					return redirect('rmbebidas:tpainel')
				else:
					return render(request,'index.html',{'senhaAlert1':"Senha Errada",'keepEmail':email,'keepSenha':senha})
		
		except:
			return render(request,'index.html',{'emailAlert1':"Email não encontrado",'keepEmail':email,'keepSenha':senha})
	else:
		return render(request,'index.html',{'getERROR':"Acesso GET negado"})


def defbtnnvproduto(request):
	if request.method=="POST":
		nome = request.POST.get('nome')
		quantidade = request.POST.get('quantidade')
		descricao = request.POST.get('descricao')
		fornecedor = request.POST.get('fornecedor')
		preco = request.POST.get('preco')
		marca = request.POST.get('marca')

		produto=TbProdutos(pro_nome=nome,pro_quantidade=quantidade,pro_descricao=descricao,pro_fornecedor=fornecedor,pro_preco=preco,pro_marca=marca)
		produto.save()
		produtos=TbProdutos.objects.all()
		return render(request,'tproduto.html')
	else:
		return render(request,'tproduto.html',{'getERROR2':"Acesso GET negado"})


def defbtnverproduto(request,id):
	produto=TbProdutos.objects.get(pro_codigo=id) #pegando o produto através da sua chave
	produtos=TbProdutos.objects.all()
	return render(request,'tverproduto.html',{'PRODUTO':produto})

	# produtos=TbProdutos.objects.all()
	# return render(request,'tpainel.html',{'existProdutoAlert':"Produto não encontrado",'PRODUTO':produtos})


def defbtneditproduto(request,id):
	if request.method=="POST":
		produto=TbProdutos.objects.get(pro_codigo=id) #pegando o produto através da sua chave
		produto.pro_nome = request.POST.get('nome')
		produto.pro_quantidade = request.POST.get('quantidade')
		produto.pro_descricao = request.POST.get('descricao')
		produto.pro_fornecedor = request.POST.get('fornecedor')
		produto.pro_preco = request.POST.get('preco')
		produto.pro_marca = request.POST.get('marca')
		produto.save()
		
		produtos=TbProdutos.objects.all()
		return render(request,'tpainel.html',{'PRODUTO':produtos})


def defbtndellproduto(request,id):
	try:
		produto=TbProdutos.objects.get(pro_codigo=id) #pegando o produto através da sua chave
		produto.delete()
		
		produtos=TbProdutos.objects.all()
		return render(request,'tpainel.html',{'PRODUTO':produtos})
	except:
		produtos=TbProdutos.objects.all()
		return render(request,'tpainel.html',{'PRODUTO':produtos})


def defbtncadusuarios (request):
	if request.method=="POST":
		senha=request.POST.get('senha')
		nome=request.POST.get('nome')
		sobrenome=request.POST.get('sobrenome')
		
		email=request.POST.get('email')
		busca=TbUsuarios.objects.filter(usu_email=email)
		
		if busca:
			return render(request,'tcadusuarios.html',{'emailExiste':"Email já cadastrado",'keepEmail':email,'keepSenha':senha,'keepNome':nome,'keepSobrenome':sobrenome})
		else:
			usuario=TbUsuarios(usu_nome=nome,usu_sobrenome=sobrenome,usu_email=email,usu_senha=senha)
			usuario.save()			
			return render(request,'tcadusuarios.html',{'cadSucesso':"Usuario Cadastrado",'keepEmail':email,'keepSenha':senha,'keepNome':nome,'keepSobrenome':sobrenome})
	else:
		return render(request,'tproduto.html',{'getERROR3':"Acesso GET negado"})
