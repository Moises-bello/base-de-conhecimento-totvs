---
article_id: 7813907111447
category: Financeiro
content_hash: f55dc996fcac2bb6f84da5b6db312f0230af67403cf20e1a1a5fa17fc63fb17f
fetched_at: '2026-06-28T22:38:04.146828+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Vencimento Final de
  Semana
type: support-article
updated_at: '2025-03-17T13:50:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7813907111447-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Vencimento-Final-de-Semana
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30700787497495) Tempo aproximado para leitura: **00:03 min** **Dúvida**

Como gerar Título, com o vencimento no final de Semana, seja postergado para próximo dia útil ?  
  
**Ambiente**Cross Segmentos - Backoffice Linha Protheus - Financeiro - Todas as versões  
  
**Solução**Para que o vencimento do título seja postergado para próximo dia útil,  os parâmetros abaixo devem esta com conteúdo da seguinte forma:

**MV\_SABFERI = S**  (Considera Sábados como Feriado quando utilizada a função **DataValida() )**  
**MV\_DOMFERI = S** (Considera Domingos como Feriado quando utilizada a função **DtValid()**

Lembrando que para títulos de Imposto, no caso acima serão antecipado.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7896863850647)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7897161489431)

**Saiba mais**[FIN0041\_Cadastrar\_Feriado\_Tabelas\_Genericas\_63](https://tdn.totvs.com/display/public/PROT/FIN0041_Cadastrar_Feriado_Tabelas_Genericas_63)
