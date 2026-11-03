---
article_id: 360026729232
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: b3484372b81b17e357d1990a5e647c58f0086b9be597a2600118d9dd55e39269
fetched_at: '2026-06-28T22:39:36.882172+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: 'CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como configurar
  alíquotas diferenciadas para PIS e COFINS importação? '
type: support-article
updated_at: '2021-06-24T13:29:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026729232-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-al%C3%ADquotas-diferenciadas-para-PIS-e-COFINS-importa%C3%A7%C3%A3o
---

**Dúvida**

Como configurar alíquotas diferenciadas para PIS e COFINS importação?   
  
**Ambiente**

Protheus - Livros Fiscais - A partir da versão 11.80  
  
**Solução**

Para lançar notas de importação com alíquotas de PIS e COFINS diferenciadas, crie uma exceção fiscal conforme abaixo:

Estado (F7\_EST)= EX  
Tipo (F7\_TIPOCLI)=  x - Importação  
Aliq. PIS (F7\_ALIQPIS)= conforme necessidade   
Aliq COF (F7\_ALIQCOF) = conforme necessidade   
Uf Busca (F7\_UFBUSCA) = Origem

Vincule a exceção ao produto. Sempre que lançar uma nota de importação com esse produto, o sistema irá acatar a alíquota da exceção fiscal.
