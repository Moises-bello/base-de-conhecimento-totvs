---
article_id: 4409771452311
category: Financeiro - Consultas / Relatórios
content_hash: ed9af4b34b3b8864b8a98e33a32b14f66b51d91012f2a38c16f32e60618acab5
fetched_at: '2026-06-28T22:37:58.375401+00:00'
product: protheus
section_id: 1500001539561
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINR150 -  Não apresenta
  mais totalizadores por Filial
type: support-article
updated_at: '2026-03-27T11:34:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409771452311-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINR150-N%C3%A3o-apresenta-mais-totalizadores-por-Filial
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39332833085975) Tempo aproximado para leitura: **00:03 min**  
  
**Dúvida**  
Relatório FINR150 não apresenta mais totalizadores por filial.  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da versão 12.1.25.  
  
**Solução**

Em 15/04/2021, por meio da ISSUE DFINTES-15494 foi liberado um tratamento que, quando a SE2 estiver totalmente compartilhada, não haverá mais a quebra por filiais.

Ajuste realizado para que as quebras do relatório sejam respeitadas conforme compartilhamento da tabela SE2 (Contas a Pagar) e ordenação selecionada.

Também foram ajustados os parâmetros "Seleciona Filiais" e "Considera Filiais Abaixo" para que ambos sirvam apenas para determinar quais filiais serão executadas.

**Saiba mais**

[Títulos a Pagar - FINR150 - Financeiro P12](https://tdn.totvs.com/pages/releaseview.action?pageId=510498025)
