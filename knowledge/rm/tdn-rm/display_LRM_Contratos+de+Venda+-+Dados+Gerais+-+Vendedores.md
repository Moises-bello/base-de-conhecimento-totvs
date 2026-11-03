---
content_hash: dc0764bb40f3de6ff2be1a69ad56f28e8ae969f93a1f8cdb11e5ff1874c2f712
fetched_at: '2026-06-29T00:09:48.552437+00:00'
page_id: '435105187'
product: rm
source: tdn-rm
title: Contratos de Venda - Dados Gerais - Vendedores
type: documentation
url: https://tdn.totvs.com/display/LRM/Contratos+de+Venda+-+Dados+Gerais+-+Vendedores
version: 6
---

ATENÇÃO!!!

A partir do momento em que a [Comissão 2.0](https://tdn.totvs.com/pages/viewpage.action?pageId=665033766) estiver ativa no TCGI, esta funcionalidade não estará mais disponível para acesso.

Através deste cadastro será possível vincular à Venda um Vendedor responsável. O Registro pode ser adicionado mesmo  em uma venda com a situação [Efetivado].  
O cadastro poderá ter o seu acesso efetuado também através do menu do TOTVS Incorporação, porém não contará com as opções [Incluir] e [Excluir].  
   
A validação do registro é feito através do código do vendedor, gerado automaticamente pelo sistema e o código do [Cliente/Fornecedor] ou [Chapa do Funcionário], sendo que o sistema não permite que um  novo registro que contemple os mesmos dados seja incluído novamente  na Venda.

* **Permissões necessárias:** Para acesso a funcionalidade é necessário que o usuário esteja vinculado  a um Perfil de Usuários, com a permissão a seguir habilitada:
  + 02.01.01.01 - Contratos: Incluir
  + 02.01.01.03 - Contratos: Editar
  + 02.01.01.26 - Contratos: Vendedor

* **Localização:**
  + Projetos/ Incorporação/ Contratos/ [Contratos - Contratos de Venda] / [Anexo-Vendedores]

* **Vinculado aos registros:**
  + [Coligada]
  + [Venda]
  + [Cliente/Fornecedor/ Ambos] ou [Funcionário]

* **Ações Permitidas:**
  + [Incluir]
  + [Editar]
  + [Pesquisar]
  + [Excluir]
  + [Visualizar]

* **Tipos  de Vendedores Permitidos:**
  + Vendedor do tipo [Cliente/Fornecedor/Ambos].
  + Vendedor do Tipo [Funcionário].

**Campos da tela:**

* **Campo Vendedor-**
  + Campo identificador do registro.
  + Gerado automaticamente pelo sistema.
  + Não permite alterações.

* **Campo Cliente/Fornecedor**
  + Campo responsável por criar um Vendedor do tipo [Cliente/Fornecedor/Ambos]
  + Habilitado para preenchimento com o [código do Cliente/Fornecedor] se o campo [Chapa do Funcionário] não for informado.
  + Capacidade para até 25 caracteres (A máscara do Cliente/Fornecedor/Ambos é criada nos parâmetros do sistema Financeiro).
  + Permite [Cliente/Fornecedor/Ambos] do tipo Global (Coligada = 0).
  + Preenchimento não obrigatório

* **Campo Chapa do Funcionário**
  + Campo responsável por criar um Vendedor do tipo [Funcionário].
  + Habilitado para preenchimento com a [Chapa do Funcionário] se o campo com o [código do Cliente/Fornecedor]] não for informado.
  + Capacidade para até 16 caracteres (A máscara do Cliente/Fornecedor/Ambos é criada nos parâmetros do sistema Financeiro).
  + Preenchimento não obrigatório.

**Informações Complementares**

---
