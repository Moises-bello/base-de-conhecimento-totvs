---
content_hash: bdf01d58dd06659eec2688cd875ce71b19cc4965dcb3dad2224f770d49d0c3c9
fetched_at: '2026-06-29T00:09:48.518145+00:00'
page_id: '435105179'
product: rm
source: tdn-rm
title: Vendedores
type: documentation
url: https://tdn.totvs.com/display/LRM/Vendedores
version: 20
---

**Vendedores**

Atenção!

Após habilitar a [Comissão 2.0](https://tdn.totvs.com/pages/viewpage.action?pageId=665033766), o cadastro de Vendedores não estará mais acessível devido ao conceito de [Funções](https://tdn.totvs.com/pages/viewpage.action?pageId=773517906) da comissão.

Agora na verão 12.1.29 é permitido definir na venda um vendedor principal, assim como já pode ser feito nos compradores.

O objetivo é a utilização dessa informação em relatórios do cliente.

O menu [Vendedores] permite  a visualização e edição dos registros de Vendedor que foram vinculados às vendas. Através deste menu, a visualização dos  ícones [Incluir] e [Excluir] são suprimidos, permitindo apenas que o usuário edite um registro que já foi vinculado à uma venda.  
Através da edição, será possível alterar o [Cliente/Fornecedor/Ambos]  ou [Funcionário] que foi vinculado  à uma venda.  
   
Para que registros sejam incluídos nesta tela, é necessário que  este vendedor tenha sido vinculado ao anexo da venda previamente.  
   
O sistema permite  que os vendedores sejam alterados, mesmo que vinculados à uma venda já efetivada, pois  a finalidade deste cadastro é gerar comissões , tanto no momento da venda, quanto posteriormente.  
 

* **Permissões  necessárias:** Para acesso a funcionalidade é necessário que o usuário esteja vinculado  a um Perfil de Usuários, com a permissão a seguir habilitada:

* + 02.01.01.26- Contratos: Vendedor

* **Localização:**
  + Projetos/ Incorporação/ Contratos/ [Contratos - Vendedor]

* **Vinculado aos registros:**
  + [Coligada]
  + [Venda]
  + [Cliente/Fornecedor/ Ambos]    ou [Funcionário]

* **Ações Permitidas:**
  + [Pesquisar].
  + [Visualizar] .
  + [Editar].

* **Tipos  de Vendedores Permitidos:**
  + Vendedor do tipo  [Cliente/Fornecedor/Ambos].
  + Vendedor do Tipo [Funcionário].

**Campos da tela:**

* **Campo Vendedor-**
  + Campo identificador do registro.
  + Gerado automaticamente pelo sistema.
  + Não permite alterações.

* **Campo Cliente/Fornecedor-**
  + Campo responsável por criar um Vendedor do tipo [Cliente/Fornecedor/Ambos]
  + Habilitado para preenchimento com o [código do Cliente/Fornecedor] se o  campo [Chapa do Funcionário] não for informado.
  + Capacidade para até 25 caracteres(A máscara do Cliente/Fornecedor/Ambos é criada nos parâmetros do sistema Financeiro).
  + Preenchimento não obrigatório
  + Permite [Cliente/Fornecedor/Ambos]  do tipo Global(Coligada = 0).

Informando um Fornecedor como Vendedor, a comissão será integrada com o módulo de Gestão de Estoques, Compras e Faturamento.

* **Campo Chapa do Funcionário-**
  + Campo responsável por criar um Vendedor do tipo [Funcionário].
  + Habilitado para preenchimento com a [Chapa do Funcionário] se o  campo com o [código do Cliente/Fornecedor]] não for informado.
  + Capacidade para até 16 caracteres(A máscara do Cliente/Fornecedor/Ambos é criada nos parâmetros do sistema Financeiro).
  + Preenchimento não obrigatório.

Informando a chapa do Funcionário, a comissão será gerada para o módulo de Folha de Pagamento (labore).

 **Informações Complementares  - Anexos**

---

* Comissões
* Log do Vendedor
* Contratos de Venda
* Contratos de Venda - Revitalização
