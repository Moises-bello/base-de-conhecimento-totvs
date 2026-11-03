---
article_id: 360018816911
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 773146bc73b102b12626580614ac8bbf33ee9ac4c7bc256f86d1a776e5c7d18b
fetched_at: '2026-06-28T22:38:39.900245+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Nota sobre o campo C6_PROGRAM
type: support-article
updated_at: '2025-06-20T13:26:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018816911-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Nota-sobre-o-campo-C6-PROGRAM
---

**Dúvida**

Nota sobre o uso do campo C6\_PROGRAM.

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da versão 11.  
  
**Solução**

O campo **C6\_PROGRAM** não é novo, ele existe desde a versão 11.8, este campo é alimentado através da tabela **SHN**, campo **HN\_PROGRAM**, que são os itens de programa de produção, módulo PCP, a informação é utilizada no relatório **matr816** - relatório de pedidos de venda por família.  
Por se tratar de um campo que recebe informações de um campo de sistema que não pode ser alterado, com integração com outro módulo, é recomendável não efetuar nenhuma alteração no mesmo.
