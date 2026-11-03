---
article_id: 29984699112599
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: b5f2d4ee93649460ce5f0e3876b35520c9b0387e303b98d4b40748bf44112804
fetched_at: '2026-06-28T22:38:42.573789+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - stack depth overflow (A440GERAC9(FATXFUN.PRX))
type: support-article
updated_at: '2025-02-18T11:08:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/29984699112599-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-stack-depth-overflow-A440GERAC9-FATXFUN-PRX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29984737744791) Tempo aproximado para leitura: **00:01:00 min****Ocorrência**No módulo Faturamento, ao tentar realizar o faturamento é apresentado o error.log "stack depth overflow in function \_GETMVCACHED on \_GETMVCACHED(SUPERGETMV.PRW)  line"  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Causa**[Exemplo:  
Esse incidente ocorre, ao possuir 2 itens no documento de entrada, um com e outro sem poder terceiros com o parâmetro "MV\_GRVBLQ2 = T"

**Solução**1 - Aplique o pacote de acordo com sua respectiva versão:

12.1.2210: <https://suporte.totvs.com/portal/p/10098/download?e=1146521>

12.1.2310: <https://suporte.totvs.com/portal/p/10098/download?e=1146523>

12.1.33: <https://suporte.totvs.com/portal/p/10098/download?e=1146522>

2 - Teste novamente
