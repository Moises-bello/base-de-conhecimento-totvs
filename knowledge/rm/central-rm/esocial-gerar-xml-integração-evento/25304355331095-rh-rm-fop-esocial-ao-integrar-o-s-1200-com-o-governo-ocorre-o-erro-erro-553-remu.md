---
article_id: 25304355331095
category: eSocial - Gerar XML/ Integração Evento
content_hash: 98b6e896b7601d975c5ccfb91af51ea359dfd381c04bf434a7515a89b0f33e76
fetched_at: '2026-06-28T22:47:11.987457+00:00'
product: rm
section_id: 1500000834381
source: central-rm
title: RH - RM - FOP - eSocial - Ao integrar o S-1200 com o governo, ocorre o erro
  Erro 553 - Remuneração em períodos anteriores não deve ser preenchido
type: support-article
updated_at: '2026-06-01T14:49:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25304355331095-RH-RM-FOP-eSocial-Ao-integrar-o-S-1200-com-o-governo-ocorre-o-erro-Erro-553-Remunera%C3%A7%C3%A3o-em-per%C3%ADodos-anteriores-n%C3%A3o-deve-ser-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25304355312023) Tempo aproximado para leitura: **00:02:00 min****Ocorrência**

Ao integrar o S-1200 com o governo, ocorre o erro Erro 553 - Remuneração em períodos anteriores não deve ser preenchido.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25304344669719)

**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Folha de Pagamento - eSocial - Todas as versões  
  
**Causa**O erro ocorre pois o governo só aceitará remuneração no período anterior quando for as categorias 1XX, 2XX, 3XX, 4XX, 721, 722, 771, 901, 902 e indicativo de apuração for mensal.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25304355314711)

**Solução**  
Para solucionar essa ocorrência, é necessário conferir se a categoria e indicativo de apuração atende ao que informa no leiaute.   
Caso não atenda, não será possível enviar o S-1200 com infoPerApur, sendo necessário retificar as verbas rescisórias.
