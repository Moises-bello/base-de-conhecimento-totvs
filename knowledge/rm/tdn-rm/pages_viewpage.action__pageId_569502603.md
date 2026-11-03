---
content_hash: 57638c744bb97a2fc6676a9be73794c2fce99dc8881a47cb8db249c8401cac3c
fetched_at: '2026-06-29T00:10:51.665965+00:00'
page_id: '569502603'
product: rm
source: tdn-rm
title: Validação de MatMed e MatMed Terceiros com Código Específico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=569502603
version: 4
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Parâmetro nas Condições contratuais do convênio para utilizar Mat/Med terceirizados**
4. **Parâmetro na Tabela de Mat/Med para utilizar descrição específica**
5. **Tabelas utilizadas**

itensVisão Geral

## **01. VISÃO GERAL**

Ao executar o processo "Encerramento de Parcial" o sistema valida no contrato do convênio as tabelas de Materiais ou Medicamento quando estiverem configuradas para utilizar a opção "**Usar descrição específica somente no faturamento eletrônico**" selecionada.

* Caso algum Material ou Medicamento lançado na conta do paciente estiver com o código do especifico em branco, é exibida mensagem para validação: *O produto "XXXXXXXXXX" não possui o código específico na tabela MAT/MED do convênio. Cadastre o seu código específico, estorne este lançamento e inclua-o novamente.*
* Caso algum Material ou Medicamento Terceirizado lançado na conta do paciente estiver com o código do especifico em branco, é exibida mensagem para validação: *O produto "XXXXXXXXXX" não possui o código específico na tabela MAT/MED do prestador "X". Cadastre o seu código específico, estorne este lançamento e inclua-o novamente.*

Exemplo de Utilização

## **02. EXEMPLO DE UTILIZAÇÃO**

Parâmetro nas Condições contratuais do convênio para utilizar Mat/Med terceirizados

## **03. Parâmetro nas Condições contratuais do convênio para utilizar Mat/Med terceirizados**

Parâmetro na Tabela de Mat/Med para utilizar descrição específica

## **04. Parâmetro na Tabela de Mat/Med para utilizar descrição específica**

## **05. TABELAS UTILIZADAS**

* SZATENDMATMED
* SZLANCMMTERCEIRO
* SZCONDCONTRAT
* SZTABMATMAD
]]>
