---
content_hash: 3b294613be702500bc87097932054555b937709d071dd7b3727ba69a1db2c448
fetched_at: '2026-06-29T00:11:38.300411+00:00'
page_id: '784217581'
product: rm
source: tdn-rm
title: Conflitos SOD
type: documentation
url: https://tdn.totvs.com/display/LRM/Conflitos+SOD
version: 6
---

## **01. VISÃO GERAL**

       Esta é uma funcionalidade administrativa de criação, exclusão, edição e listagem dos conflitos que estarão disponiveis para a utilização da matriz SOD.

       Os Conflitos podem ter a coligada contextualizada com o usuário logado ou globais, condição essa que pode ser definida no Switch "**Visível a todas coligadas**". Portanto uma coligada somente tem acesso aos seus registros, sejam da coligada do contexto ou global.

O Conflito tem a premissa de registrar quais conjuntos de TAGMENU e POLICIES não devem coexistir.

## **02. EXEMPLO DE UTILIZAÇÃO**

   É possível acessar a tela de Gerenciamento da Matriz SOD:

* Pelo menu: Serviços Globais > Segurança > Matriz SOD > Cadastros > Conflitos;

**LISTAGEM**

A Listagem é composta com filtros simples e avançados baseados no padrão OData, que podem ser combinados para buscas mais elaboradas.

O Switch "**Visível a todas coligadas**" determina se os resultados devem respeitar a coligada do contexto do usuário logado ou global.

**CADASTRO e EDIÇÃO**

Durante o cadastro ou edição do conflito, a coligada é determinada pelo Switch "**Visível a todas coligadas**" que determina se os resultados devem respeitar a coligada do contexto do usuário logado ou global.

Todos os campos editáveis da tela são obrigatórios.

O campo "Risco" é um lookup para os riscos que foram cadastrados previamente, respeitando a informação no Switch "**Visível a todas coligadas**".

Para selecionar as permissões, é necessário informar o módulo onde a permissão se encontra, logo após pode ser utilizada a arvore de busca de permissões do modulo selecionado.

**Exemplo:**

**DETALHES**

É possível visualizar todas as informações e realizar a **Exclusão** ou **Edição** do registro.

## **03.** **DICIONÁRIO DE TERMINOLOGIAS**

**Código****:** Representa o código da coligada.

**Visível a todas coligadas****:** Indica a condição que deve ser respeitada, informado se a coligada é por contexto ou global.

**Nome do Conflito:** Nome que irá representar o risco.  
**Risco:** Representa o risco que será vinculado ao conflito.

**Module 1:** Identifica o nome do módulo do sistema.  
**Tag Menu 1:** Representa o código da primeira TAG MENU.  
**Permissão 1:** Representa o codigo da primeira POLICY.  
**Nome 1:** Descrição da permissão selecionada.

**Module 2:** Identifica o nome do módulo do sistema.  
**Tag Menu 2:** Representa o código da segunda TAG MENU.  
**Permissão 2:** Representa o codigo da segunda POLICY.  
**Nome 2:** Descrição da permissão selecionada.
