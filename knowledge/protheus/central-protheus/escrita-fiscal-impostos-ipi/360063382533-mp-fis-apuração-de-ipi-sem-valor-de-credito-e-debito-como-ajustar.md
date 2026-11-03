---
article_id: 360063382533
category: Escrita Fiscal - Impostos - IPI
content_hash: d9c7ee8d7ae362f732ef884cbd18a3b63d952d2edad968d11a80016a2cb49892
fetched_at: '2026-06-28T22:39:29.051639+00:00'
product: protheus
section_id: 1500001538641
source: central-protheus
title: MP - FIS - Apuração de IPI sem valor de credito e debito como ajustar?
type: support-article
updated_at: '2022-11-16T18:14:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063382533-MP-FIS-Apura%C3%A7%C3%A3o-de-IPI-sem-valor-de-credito-e-debito-como-ajustar
---

**Dúvida** Apuração de IPI sem valor de credito e debito como ajustar?

**Ambiente**Protheus - Fiscal -  A partir da versão 12   
  
**Solução**

Quando fazemos a apuração do IPI, o sistema Lê as tabelas de movimento SF3/SFT e também a tabela onde foi definido pelo cliente a alíquota de IPI, onde temos

1) exceção fiscal - SF7

2) cadastro de produtos - SB1

3) cadastro de indicador de produtos - SBZ

onde devem ser verificados os parâmetros

MV\_ARQPROD = definir onde o sistema busca as informações SB1 ou SBZ

MV\_ARQPROP = .F. considera o conteúdo do parâmetro MV\_ARQPROD , se .T. considera o preenchimento dos campos
