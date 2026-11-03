---
article_id: 360024679351
category: Materiais - Compras (SIGACOM)
content_hash: aa43cf94e3fc9f94bdc000c28b183f9e8d1e77c0e62c15ef13622844fab41f87
fetched_at: '2026-06-28T22:41:07.427987+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Ao efetuar o lançamento
  de Documento de Entrada, ocorre o Help A103TOKSEV
type: support-article
updated_at: '2022-05-16T22:07:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024679351-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Ao-efetuar-o-lan%C3%A7amento-de-Documento-de-Entrada-ocorre-o-Help-A103TOKSEV
---

**Ocorrência**Ao efetuar o lançamento de Documento de Entrada, ocorre o Help A103TOKSEV  
  
**Ambiente**Protheus – Compras – A partir da versão 11.80  
  
**Causa**A mensagem "A103TOKSEV" é apresentada quando a somatória do rateio das múltiplas naturezas não está de acordo.

**Solução**Se adicionada a Natureza no lado Esquerdo da rotina de Documento de Entrada - MATA103, é considerado como Natureza Simples, agregando o valor total para esta Natureza, ou seja, 100%.  
  
Já do lado Direito é considerado como Múltiplas Natureza, ou seja, é possível efetuar o Rateio entre as natureza, divisão de valores/percentual.  
  
E este help é apresentado na seguinte condição:  
*Não adicionando um percentual em sua totalidade de 100%, seja para uma natureza ou várias naturezas.*  
Desta forma, é preciso adicionar o percentual de 100% para que sistema não apresente help em questão.
