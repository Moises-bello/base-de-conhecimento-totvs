---
article_id: 13636205811863
category: Materiais - Compras (SIGACOM)
content_hash: e3365e72e570ee83787b7f3bff8d5ecc4a8da547b092baff3dd1ec9d27a0f608
fetched_at: '2026-06-28T22:41:18.645280+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Existe um Ponto de
  Entrada para gerar um Número de série exclusiva para Documentos de entrada?
type: support-article
updated_at: '2023-04-06T11:36:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13636205811863-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Existe-um-Ponto-de-Entrada-para-gerar-um-N%C3%BAmero-de-s%C3%A9rie-exclusiva-para-Documentos-de-entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Existe um Ponto de Entrada para gerar um Número de série exclusiva para Documentos de entrada?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus  Compras- Todas as versões  
  
**Solução**O ponto de entrada M103ALTS sugere séries diferentes baseados o Arrays informados.

Quando o lançamento do Documento for efetuado manualmente, a rotina sugere a alteração, caso selecione a opção Sim a série é alterada, caso contrário não é permitido o lançamento.  
Quando utilizado rotina automática o tratamento será automático ou seja, caso o documento já exista cadastrado ele tentará a próxima combinação, se estiver disponível utiliza, caso contrário tentará a próxima, caso não haja nenhuma disponível abortará o processo como ocorria anteriormente.

**Sabia mais:**

* [M103ALTS - Séries alternativas para o Documento de Entrada](https://tdn.totvs.com/pages/releaseview.action?pageId=89622425)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
