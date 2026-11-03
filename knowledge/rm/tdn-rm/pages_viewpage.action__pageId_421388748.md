---
content_hash: 9f3ae0fe859e26e54e568100c99720f9b77703502b4d5005f02b5c3831be0ed5
fetched_at: '2026-06-29T00:09:18.684842+00:00'
page_id: '421388748'
product: rm
source: tdn-rm
title: Rateios por Centro de Custo/Natureza Orçamentária Financeira e por Departamento
  do Lançamento Financeiro
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388748
version: 6
---

As informações dos Rateios podem ser preenchidas manualmente ou automaticamente.

**Manualmente**

Ao utilizar o botão de "Rateio" localizado na pasta "Dados Adicionais" é apresentada a janela de rateios.

Inclusão

* Ícone "Incluir"
* Informar Centro de Custo ou Departamento
* Informar "Valor" ou "Percentual" (Percentual é aplicado sobre o "Valor Original")
* Se for rateio para apenas um registro, utilizar o botão "OK"
* Se for rateio para mais de um registro, utilizar o botão "Confirma" e repetir o processo

Edição

Na grid de rateios é possível realizar a edição dos campos "Valor", "Percentual" e "Histórico".

* Clicar três vezes sobre o campo na grid
* Clicar sobre qualquer outro campo da grid

Exclusão

* Clicar sobre o registro na grid
* Ícone "Excluir"

**Automaticamente**

Existem duas formas:

1ª) Rateio de acordo com registro informado no campo "Centro de Custo" ou "Departamento":

* Informar registro no campo "Centro de Custo" ou "Departamento";
* Ao pressionar a tecla "tab" ou acessar outra pasta da edição, o sistema sugere o preenchimento do rateio de acordo com o registro informado, respondendo "Sim" o preenchimento é realizado automaticamente.

2ª) Rateio de acordo com os Defaults do Cliente/Fornecedor:

* Ao informar um Cliente/Fornecedor no lançamento as informações de rateio são preenchidas automaticamente.

**Observação**  
 O valor "Total" do rateio deve ser igual ao "Valor Original" do lançamento, se houver "diferença" a edição do lançamento não será realizada.

**Dicas**  
 Ao clicar sobre o nome do Centro de Custo, da Natureza ou do Departamento é possível acessar a janela de edição do seu cadastro.

**Permissão para Visualização, Inclusão, Alteração ou Exclusão**

As permissões para visualização, inclusão, alteração ou exclusão dos Rateios não possuem vínculos com as permissões do lançamento financeiro, ou seja, mesmo o usuário não tendo permissão para Incluir, Editar, Cancelar ou Excluir lançamentos, ele poderá incluir, alterar ou excluir os Rateios, ou vice-versa.

As permissões para visualização, inclusão, alteração ou exclusão dos Rateios devem ser configuradas somente através da funcionalidade de permissão de "Acesso a Campos" das Tabelas FLANRATCCU (Rateio por Centro de Custo) e FLANRATDEP (Rateio por Departamento), no cadastro de Perfil.

Ao definir que o Perfil não pode "Alterar" os campos do Rateio, o usuário vinculado ao Perfil não poderá incluir, excluir ou alterar o Rateio.

Caso seja retirada a permissão para "Alterar" qualquer um dos campos do Rateio, os outros também não poderão ser alterados. O campo "Histórico" do Rateio por Centro de Custo só não poderá ser alterado se ele não permitir alteração, ou seja, se algum outro campo não tiver permissão para alterar, os outros também não poderão ser alterados, exceto o campo "Histórico".

Veja Também

* [Procedimento para utilizar Rateios](http://tdn.totvs.com/pages/viewpage.action?pageId=4811902)
