---
content_hash: 003a8609e7f7f70f9432e49266a30c3bda002c02642c9653d5271c0e3c4f9ae3
fetched_at: '2026-06-29T00:11:38.295272+00:00'
page_id: '784217562'
product: rm
source: tdn-rm
title: Riscos SOD
type: documentation
url: https://tdn.totvs.com/display/LRM/Riscos+SOD
version: 3
---

### **CONTEÚDO**

1. #### **Visão Geral**
2. #### **Exemplo de utilização**

#### **01. VISÃO GERAL**

#### Esta é uma funcionalidade administrativa de criação, exclusão, edição e listagem dos riscos que estarão disponiveis para a criação de conflitos da matriz SOD.

#### Os Riscos podem ser contextualizados com a coligada do usuário logado ou global, condição essa que pode ser definida no campo "Visivel a todas coligadas". Portanto uma coligada somente tem acesso aos seus registros, seja ela do contexto ou GLOBAL.

#### **02. EXEMPLO DE UTILIZAÇÃO**

#### É possível acessar a tela de Gerenciamento da Matriz SOD:

* #### Ao abrir o RM.exe, clicando nas gerenciamento da matriz SOD;
* #### Pelo menu: Serviços Globais > Segurança > Matriz SOD > Cadastros > Riscos;

## **LISTAGEM**

A Listagem é composta com filtros simples e avançados baseados no padrão OData.

Caso seja marcado como "Sim" na opção de "Visivel a todas coligadas", será realizada a busca dos riscos de vinculo GLOBAL, caso "Não", será realizada a busca dos riscos baseado na coligada do contexto do usuário logado.

## **CADASTRO**

Durante o cadastro do risco, a coligada é determinada pelo parâmetro "Visível a todas coligadas", onde se for marcado "Sim", o registro será gravado vinculado a coligada GLOBAL, caso "Não", o registro será gravado vinculado a coligada do contexto do usuário logado.

O campo "Tipo do Alerta" possui valores contextualizados de alertas, ao realizar a troca de visibilidade do registro, os valores do campo "Tipo do Alerta" também são alterados para respeitar o contexto.

Todos os campos editaveis da tela são obrigatórios.

## **EDIÇÃO**

Durante a edição do risco, a coligada é determinada pelo parâmetro "Visível a todas coligadas", se for marcado "Sim", o registro terá seu vinculo alterado para coligada GLOBAL, caso "Não", o registro registro terá seu vinculo alterado para coligada do contexto do usuário logado.

O campo "Tipo do Alerta" possui valores contextualizados de alertas, ao realizar a troca de visibilidade do registro, os valores do campo "Tipo do Alerta" também são alterados para respeitar o contexto.

Todos os campos editaveis da tela são obrigatórios.

## **EXCLUSÃO**

ATENÇÃO

#### A EXCLUSÃO SOMENTE É PERMITIDA CASO NÃO EXISTAM CONFLITOS VINCULADOS AO RISCO.

#### 

#### 

#### **4. DICIONÁRIO DE TERMINOLOGIAS**

#### **Código****:** Representa o código da coligada.

#### **Visível a todas coligadas****:** É o controlador de visibilidade do risco, nele é possivel realizar vinculos ou filtrar com base na coligada do contexto do usuário logado ou global (0).

**Nome do Risco:** Nome que irá representar o risco.

**Tipo do Alerta:** Representa o tipo do alerta e grau de criticidade do risco, este campo é contextualizado, portanto podem existir alertas especificos somente para a coligada GLOBAL assim como as coligadas do contexto do usuário logado.

#### 

false

**Versão:** 12.01.2310 ou superior
