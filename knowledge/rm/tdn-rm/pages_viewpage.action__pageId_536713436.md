---
content_hash: 371492fc12d8af0d7daa6874e6fad4ccd04c7d16842e5988dd0c48a5ecb6b95b
fetched_at: '2026-06-29T00:10:37.154621+00:00'
page_id: '536713436'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-6620 DT Cálculo dos Valores Auxiliares para Desconto por Antecipação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=536713436
version: 6
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | TOTVS Educacional |
| Função: | Inclusão/alteração lançamento financeiro |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DEDUINTEGRACOES-6620](https://jiraproducao.totvs.com.br/browse/DEDUINTEGRACOES-6620) |

## **02. SITUAÇÃO/REQUISITO**

Diante de alguns cenário apresentados pelos cliente surgiu a necessidade de controlar de forma paralela e especifica valores relacionados ao processamento do desconto por antecipação calculados durante geração do lançamento financeiro do aluno.

## **03. SOLUÇÃO**

Criamos o recurso de [valores auxiliares](https://tdn.totvs.com/display/LRM/Valor+Auxiliar) que serão processados durante a geração do laçamento financeiro da parcela.

Para cada vencimento do desconto por antecipação processado para a parcela do contrato do aluno o sistema executará as fórmulas vinculadas aos valores auxiliares cadastrados que são aplicados ao "Desconto por antecipação".

Importante

Serão processados somente os valores auxiliares ativos e inativo em que a validade seja inferior a data de vencimento da parcela.

Os valores retornadas pela fórmula previamente parametrizada no cadastro do valor auxiliar serão gravados na tabelas **SVALORAUXLANDESCPONTUAL**

A tabela **SVALORAUXLANDESCPONTUAL** tem como objetivo armazenar os valores auxiliares processados para cada vencimento do desconto por antecipação conforme os dados presentes na **SLANDESCPONTUAL**.

Exemplo:

* A Parcela possui uma bolsa condicional ( cód. bolsa 35)
* Valor auxiliar cadastrados  Id. 6 - VAUX002
* Desconto por antecipação com 4 vencimentos ( conforme a imagem abaixo )

Apos a geração do lançamento financeiro os valores auxilares processados serão gravados na tabela **SVALORAUXLANDESCPONTUAL** conforme o exemplo abaixo.

Importante

 O valor demonstrado acima será o valor retornado pela fórmula associada ao valor auxiliar, ou seja, contempla a regra pré estabelecida pelo cliente.
