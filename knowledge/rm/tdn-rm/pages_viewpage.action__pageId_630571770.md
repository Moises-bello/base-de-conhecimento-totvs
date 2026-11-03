---
content_hash: e8eb35f85148d2435037734e98aa7dedaf695aeb37c1e82a0643a45079f5c892
fetched_at: '2026-06-29T00:11:05.385964+00:00'
page_id: '630571770'
product: rm
source: tdn-rm
title: Kit de Lançamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=630571770
version: 6
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Lançando o Kit**
3. **Parâmetro**

itensVisão Geral

## **01. VISÃO GERAL**

O Kit de Lançamentos é uma rotina executada durante a gravação de um novo item na Elaboração de Contas, ao se lançar uma taxa, serviço, diária, honorário ou um exame, o sistema verifica se este item está vinculado a um kit.

Este item deve estar cadastrado no kit, na aba "Procedimento vinculado". Caso esteja, os itens que compõe o kit que podem ser diárias, taxas/serviços, materiais/medicamentos e exames, serão lançados nas suas respetivas abas. 

Consulte também nosso

Lançando o Kit

## **02.** **LANÇANDO O KIT**

**Menu Faturamento> Particular e Convênios> Elaboração de contas**

Ao lançar um item que esteja vinculado a um kit

Os demais itens do kit são lançados

Parâmetro

## **03.** **PARÂMETRO**

**Itens do kit de procedimentos com quantidade superior a 1**

****Menu cadastro>Faturamento>Condições contratuais> Parâmetros 2****

Durante a inclusão do Kit, a rotina irá lançar os itens conforme o parâmetro configurado.

Se o parâmetro **desmarcado**, será lançado num único lançamento respeitando a sua quantidade original informada no Kit.

Se o parâmetro **marcado**, os itens com quantidades superior a 1 serão lançados de forma separada com quantidade igual a 1 em cada um deles.

Tabelas Utilizadas

## **03.****TABELAS UTILIZADAS**

* SZKITLANC
* SZKITLANCITEM
* SZPROCKIT
