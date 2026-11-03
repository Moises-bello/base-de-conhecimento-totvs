---
article_id: 4409269053463
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: 3d41914eeb72760ae1a36984806ec38d8b590c2ce1d01d6c21890401a2b7f9b1
fetched_at: '2026-06-28T22:39:49.933382+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC -  Ponto de entrada
  no desembaraço para incluir campos nos itens
type: support-article
updated_at: '2021-09-23T14:11:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409269053463-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Ponto-de-entrada-no-desembara%C3%A7o-para-incluir-campos-nos-itens
---

**Dúvida**Temos algum ponto de entrada na rotina do Desembaraço (EICDI502) para incluir campos neste grid de manutenção dos itens, conforme abaixo?

![desembara_o.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409278889751/desembara_o.png)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – *Easy Import Control* – Todas versões  
  
**Solução**O ponto de entrada para colocar itens no grid de manutenção dos itens é o BROWSE\_SELECIONA.

| Nome | Tipo | Descrição |
| --- | --- | --- |
| BROWSE\_SELECIONA | Caracter | Possibilita controlar os campos que serão exibidos na tela de itens da manutenção de itens do embarque. |

**Saiba mais**  
[PE EICDI500 - Manutenção do Desembaraço](https://tdn.totvs.com/pages/releaseview.action?pageId=571998687)
