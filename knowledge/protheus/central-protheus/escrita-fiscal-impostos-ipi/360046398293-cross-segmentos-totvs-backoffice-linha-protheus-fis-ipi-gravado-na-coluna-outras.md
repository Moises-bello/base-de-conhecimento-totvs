---
article_id: 360046398293
category: Escrita Fiscal - Impostos - IPI
content_hash: 4e84bb8fd5a0a2309e938d678cb83b6ab1a1717300119f186e2684d35709648b
fetched_at: '2026-06-28T22:39:29.038398+00:00'
product: protheus
section_id: 1500001538641
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- IPI Gravado na Coluna
  Outras da Nota de Entrada Com Desconto ou Não no Valor do ITEM
type: support-article
updated_at: '2021-07-28T17:29:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360046398293-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-IPI-Gravado-na-Coluna-Outras-da-Nota-de-Entrada-Com-Desconto-ou-N%C3%A3o-no-Valor-do-ITEM
---

**Dúvida**  
Como configurar o sistema para que um documento de entrada que não teve o cálculo de IPI o valor gravado na coluna Outras da Nota de Entrada seja considerado com desconto ou Não no valor do item.  
  
 **Ambiente**  
Protheus  – Livro Fiscais  – A partir da versão 11.80  
  
**Solução**Para que o valor de IPI gravado na coluna Outras do documento de entrada seja considerado como desconto no item será necessário configurar o campo (F4\_TPIPI) IPI Bruto no cadastro de TES na aba Impostos = L - Liquido.

Caso precise que não seja considerado como desconto no item, será necessário configurar o campo (F4\_TPIPI) IPI Bruto no cadastro de TES na aba Impostos = B - Bruto.
