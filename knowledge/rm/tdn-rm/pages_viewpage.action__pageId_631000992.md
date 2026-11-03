---
content_hash: 3330a8d17e20c93c34137920ad270e4211fa86c2617c01e1772f86bc7a3ca5ef
fetched_at: '2026-06-29T00:11:05.417720+00:00'
page_id: '631000992'
product: rm
source: tdn-rm
title: Cadastros do Kit de Lançamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=631000992
version: 8
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

itensVisão Geral

## **01. VISÃO GERAL**

Este cadastro consiste num conjunto de itens que podem ser lançados na conta do paciente.

Para que ocorra o lançamento desses itens, né necessário que se informe o procedimento vinculado. Ele é o gatilho para que os itens que compõem o kit, sejam lançados na conta.

Este cadastro deve ter como tabelas, as tabelas que compõem um padrão de faturamento e codificação.

No cadastro de itens, somente são permitidos os seguintes tipos: diárias, taxas e serviços, Matmed e exames.

No cadastro de procedimentos vinculados, só é possível vincular honorários, taxas, serviços, diárias e exames.

Exemplo de utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

Acesse o menu Cadastros > Faturamento >  Outros Cadastros > Kit de Lançamentos

* Selecione uma tabela de procedimento e uma de serviços que compõe o padrão de faturamento e codificação.
* Dê o nome ao kit
* Selecione o anexo "Item kit de Lançamento", inclua os itens
* No anexo "Procedimento vinculado", inclua o procedimento gatilho
* Kit que é utilizado no Pep, não possui procedimento vinculado

Itens do kit

Procedimento Vinculado

Tabelas Utilizadas

## **03.****TABELAS UTILIZADAS**

* SZKITLANC
* SZKITLANCITEM
* SZPROCKIT
