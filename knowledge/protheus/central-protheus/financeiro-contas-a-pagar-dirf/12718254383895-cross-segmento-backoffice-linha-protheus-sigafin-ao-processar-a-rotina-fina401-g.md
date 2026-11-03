---
article_id: 12718254383895
category: Financeiro - Contas a Pagar - Dirf
content_hash: 04b710c775edf7fd3e8c9bf4a4974de366d10a8a7dda1ff6301e9c1a3ab023e0
fetched_at: '2026-06-28T22:38:10.689887+00:00'
product: protheus
section_id: 1500001550482
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Ao processar a rotina
  FINA401 Gera dados para DIRF o sistema não esta enviando o Rendimento tributável
  para o titulo de imposto IRF (1708)
type: support-article
updated_at: '2023-03-03T22:20:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12718254383895-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Ao-processar-a-rotina-FINA401-Gera-dados-para-DIRF-o-sistema-n%C3%A3o-esta-enviando-o-Rendimento-tribut%C3%A1vel-para-o-titulo-de-imposto-IRF-1708
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min****Ocorrência**Ao processar a rotina **FINA401 Gera dados para DIRF** o sistema não esta enviando o Rendimento tributável para o título de imposto **IRF** (1708)**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**Uma das causa é devido a utilização do mesmo código de natureza para os títulos de imposto **IRRF e PCC (PIS, COFINS, CSLL)**  
  
**Solução**Não recomendamos o uso da mesma natureza para os impostos **IRRF** e **PCC** **(PIS, COFINS, CSLL)**, pois no momento da geração dos dados para a DIRF a rotina não conseguirá diferenciar os tributos, afetará a composição de seu rendimento tributável, pedimos a utilização de códigos diferente para as naturezas de impostos.

**MV\_IRF** = deve estar preenchido com natureza do título de **IR**

**MV\_PISNAT** = deve estar preenchido com a natureza do título de **PIS**

**MV\_COFINS** = deve estar preenchido com a natureza do título de **COFINS**

**MV\_CSLL** = deve estar preenchido com a natureza do título de **CSLL**  
Saiba mais:   
[Informações sobre a DIRF?](https://tdn.totvs.com/pages/viewpage.action?pageId=43549271)  
[FIN0041\_CPAG\_Geração\_de\_Dados\_para\_DIRF\_(FINA401)](https://tdn.engpro.totvs.com.br/pages/releaseview.action?pageId=224126168)  
[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA050 - Qual a gravação correta dos campos no Financeiro para geração da DIRF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413978579223)
