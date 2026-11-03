---
content_hash: 0867537e5e1177aa225bd0269c52088f2b65b37b5cd8aeb633acadc64cbea7c4
fetched_at: '2026-06-29T00:11:10.268335+00:00'
page_id: '642956022'
product: rm
source: tdn-rm
title: DT- RM Portal - Sugestão de Férias - Quantidade de dias com abono
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=642956022
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | RM |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | RM Portal - Sugestão de Férias |
| País: | Brasil |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHCALCRM-135](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-135) |

## **02. SITUAÇÃO/REQUISITO**

Ao cadastrar uma sugestão de férias, o sistema está considerando os dias de abono como férias gozadas para funcionários quando o parâmetro 'Ativar alterações da Reforma Trabalhista de acordo com a Lei Nº13.467 de 13 de Julho de 2017' está marcado. Com a nova edição do artigo 134 da CLT - '1º Desde que haja CONCORDÂNCIA DO EMPREGADO, as férias poderão ser usufruídas em até três períodos, sendo que um deles não poderá ser inferior a quatorze dias corridos e os demais não poderão ser inferiores a cinco dias corridos, cada um.'

## **03. SOLUÇÃO**

A validação do mínimo de dias permitidos para férias partidas passa a considerar somente os dias de férias , quando o parâmetro 'Ativar alterações da Reforma Trabalhista de acordo com a Lei Nº13.467 de 13 de Julho de 2017' estiver marcado. Quando o parâmetro estiver desmarcado os dias de férias será somando aos dias de abono.

## **04. DEMAIS INFORMAÇÕES**

**[Artigo 134 paragrafo 3 - Férias - Portal](https://tdn.totvs.com/pages/viewpage.action?pageId=307836391)**

## **05. ASSUNTOS RELACIONADOS**

**[Reforma Trabalhista 2017](https://tdn.totvs.com/display/LRM/Reforma+Trabalhista+2017)**

**[Sugestão de Férias - RM Portal FOP](https://tdn.totvs.com.br/pages/editpage.action?pageId=452718768)**
