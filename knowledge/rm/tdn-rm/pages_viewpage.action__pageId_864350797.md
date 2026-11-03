---
content_hash: 2c58a2dfd567322486f6c1ee1c1ea5bea2292d54f92278eb660e9db442577b21
fetched_at: '2026-06-29T00:11:55.877129+00:00'
page_id: '864350797'
product: rm
source: tdn-rm
title: DT - Integração com TOTVS RH Orçamento - Adequações de Banco de Dados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=864350797
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | **RM** |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Gestão de Pessoas |
| Função: | Integração com TOTVS RH Orçamento |
| País: | Brasil |
| Ticket: | N/A |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHHCM-13105](https://jiraproducao.totvs.com.br/browse/DRHHCM-13105) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2410

## **03. SITUAÇÃO/REQUISITO**

Adequar estruturalmente as tabelas de Requisição e Pareceres que irão integrar com o TOTVS RH Orçamento.  
Adicionar novos Status para as requisições quando integradas com o TOTVS RH Orçamento.

## **04. SOLUÇÃO**

Adaptação do banco de dados nas tabelas abaixo:

* VREQAUMENTOQUADRO / VREQAUMENTOQUADROPARECER,

* VREQSUBSTITUICAO / VREQSUBSTITUICAOPARECER

* VREQPROMOCAO / VREQPROMOCAOPARECER

* VREQTRANSFERENCIA / VREQTRANSFERENCIAPARECER

* VREQTRANSFPROMOCAO / VREQTRANSFPROMOCAOPARECER

* VREQDESLIGAMENTO / VREQDESLIGAMENTOPARECER

| Campo | Descrição | Tipo | Tabelas |
| --- | --- | --- | --- |
| CODCCUSTO | Código do Centro de Custo | String | Relacionadas acima. |
| IDCLASSEVALOR | Identificador da Classe de Valor | Int | Relacionadas acima. |
| IDITEMCONTABIL | Identificador do Item Contábil | Int | Relacionadas acima. |
| TEMEXCECAOORCAMENTO | Tem exceção ativa no TOTVS RH Orçamento? | Int | Relacionadas acima. |

Adaptação no Banco adicionando novos Status (VREQSTATUS):

* 8 - Consultando orçamento
* 9 - Orçamento não aprovado
