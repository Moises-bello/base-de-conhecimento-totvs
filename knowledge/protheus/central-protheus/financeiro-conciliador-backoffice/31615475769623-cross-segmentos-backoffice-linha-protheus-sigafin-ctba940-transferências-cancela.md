---
article_id: 31615475769623
category: Financeiro - Conciliador Backoffice
content_hash: 4995c700808b16c7db3f9611973d5d6a010c2412f692734793ca8d51b1741dfb
fetched_at: '2026-06-28T22:37:47.232439+00:00'
product: protheus
section_id: 30769054561431
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - CTBA940 - Transferências
  canceladas não respeitam filtro no novo conciliador backoffice
type: support-article
updated_at: '2026-01-07T18:03:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31615475769623-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-CTBA940-Transfer%C3%AAncias-canceladas-n%C3%A3o-respeitam-filtro-no-novo-conciliador-backoffice
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31615475741207) Tempo aproximado para leitura: **00:05 min**  
  
**Dúvida**  
Transferências bancárias geradas e canceladas via FINA100, devem ser consideradas no filtro de remover estornados dentro do novo conciliador backoffice?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/31615485511575)  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - CTBA940 - Todas as versões  
  
**Solução**  
Quando é realizada a operação de estorno de uma transferência bancária **(FINA100)** na prática, ocorre o lançamento inverso das contas e não propriamente o cancelamento dos movimentos anteriores.

Portanto, para esse cenário, a chave para "remover estornados" no conciliador não terá efeito, visto que tecnicamente não ocorre um estorno, mas sim um lançamento contrário para "anular" a transferência anterior.
