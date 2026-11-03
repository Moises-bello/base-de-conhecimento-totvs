---
article_id: 28307238535831
category: Materiais - Compras (SIGACOM)
content_hash: 0e988530807fe7a44dcc9f4068087a8a38a10fb383a91ad27dd18931776d491a
fetched_at: '2026-06-28T22:41:17.134646+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Protheus - SIGACOM - Devolução de Nota Fiscal
  com a Mesma Numeração e Série
type: support-article
updated_at: '2024-12-06T13:41:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28307238535831-Cross-Segmentos-TOTVS-Backoffice-Protheus-SIGACOM-Devolu%C3%A7%C3%A3o-de-Nota-Fiscal-com-a-Mesma-Numera%C3%A7%C3%A3o-e-S%C3%A9rie
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28307238511511) Tempo aproximado para leitura: **00:03:SS min** **Dúvida**

É possível devolver Nota Fiscal com mesma Numeração e Série?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gest]ao de Compras - Versão 12  
  
**Solução**

A devolução só será permitida com o mesmo número e série quando o cliente for diferente.

No padrão da tabela SE1, a chave única é composta por "E1\_FILIAL+E1\_PREFIXO+E1\_NUM+E1\_PARCELA+E1\_TIPO", conforme mencionado acima.

Seguindo essa lógica, ao utilizar a mesma numeração e série, mas com um cliente diferente, o título será gerado com duas parcelas, (A e B) conforme a seguir;

**Nota de Devolução do Cliente 01**

E1\_FILIAL, E1\_PREFIXO,   E1\_NUM,       E1\_PARCELA  E1\_TIPO

01             01                   021220240    A                  NCC

**Nota de devolução do cliente 05**

E1\_FILIAL, E1\_PREFIXO,   E1\_NUM,       E1\_PARCELA  E1\_TIPO

01             01                   021220240    B                  NCC

![Dev-Cliente-Orig.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/28307248095255)

***Saiba Mais:***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
