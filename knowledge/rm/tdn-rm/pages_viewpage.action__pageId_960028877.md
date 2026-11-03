---
content_hash: 952423174241ced1638cbaddefa457a1c0952f00b21967ab30887bc729cc56b3
fetched_at: '2026-06-29T00:12:13.503537+00:00'
page_id: '960028877'
product: rm
source: tdn-rm
title: Nível de Alerta SOD
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=960028877
version: 1
---

### **CONTEÚDO**

1. #### **Visão Geral**
2. #### **Exemplo de utilização**

#### **01. VISÃO GERAL**

#### Esta é uma funcionalidade administrativa de criação, exclusão, edição e listagem dos Níveis de Alerta que estarão disponíveis para a criação de Riscos da matriz SOD.

#### Os Níveis de Alerta podem ser contextualizados com a coligada do usuário logado ou global, condição essa que pode ser definida no campo "Visivel a todas coligadas". Portanto uma coligada somente tem acesso aos seus registros, seja ela do contexto ou GLOBAL.

#### **02. EXEMPLO DE UTILIZAÇÃO**

#### É possível acessar a tela de Gerenciamento da Matriz SOD:

* #### Ao abrir o RM.exe, clicando nas gerenciamento da matriz SOD;
* #### Pelo menu: Serviços Globais > Segurança > Matriz SOD > Cadastros > Níveis de Alerta;

## **LISTAGEM**

Na Listagem é possível ver as principais informações do Alerta sendo possível agrupar as colunas e gerenciar a tabela.

## **CADASTRO**

Durante o cadastro do Nível de Alerta, a coligada é determinada pelo parâmetro "Visível a todas coligadas", onde se for marcado "Sim", o registro será gravado vinculado a coligada GLOBAL, caso "Não", o registro será gravado vinculado a coligada do contexto do usuário logado.

O campo "Prioridade" deve ser preenchido com valores inteiros determinando o nível de prioridade do Alerta.

Todos os campos editáveis da tela são obrigatórios.

## **EDIÇÃO**

Durante o cadastro do Nível de Alerta, a coligada é determinada pelo parâmetro "Visível a todas coligadas", onde se for marcado "Sim", o registro será gravado vinculado a coligada GLOBAL, caso "Não", o registro será gravado vinculado a coligada do contexto do usuário logado.

O campo "Prioridade" deve ser preenchido com valores inteiros determinando o nível de prioridade do Alerta.

## **EXCLUSÃO**

ATENÇÃO

#### A EXCLUSÃO SOMENTE É PERMITIDA CASO NÃO EXISTAM RISCOS VINCULADOS AO NÍVEL DE ALERTA.

#### 

#### 

#### **4. DICIONÁRIO DE TERMINOLOGIAS**

#### **Código****:** Representa o código da coligada.

#### **Visível a todas coligadas****:** É o controlador de visibilidade do risco, nele é possível realizar vínculos ou filtrar com base na coligada do contexto do usuário logado ou global (0).

**Nome do Alerta:** Nome que irá representar o Alerta.

**Prioridade:** Valor inteiro para determinar o nível de prioridade do Alerta.

#### 

false

**Versão:** 12.01.2506 ou superior
