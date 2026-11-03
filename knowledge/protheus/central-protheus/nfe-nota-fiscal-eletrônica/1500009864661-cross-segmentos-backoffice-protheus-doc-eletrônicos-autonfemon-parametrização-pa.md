---
article_id: 1500009864661
category: NFe - Nota Fiscal Eletrônica
content_hash: 040bac89c2da717fb67f77b8a9ecdbbb9502be1ca8bd39f993a4c975bd34d6b6
fetched_at: '2026-06-28T22:40:01.626818+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: ' Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Autonfemon, parametrização
  para ler registros de modelo 65- nfce '
type: support-article
updated_at: '2021-07-20T16:49:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009864661--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Autonfemon-parametriza%C3%A7%C3%A3o-para-ler-registros-de-modelo-65-nfce
---

**Dúvida**Como parametrizar o schedule Autonfemon, para ler registros de modelo 65- nfce, gerados na tabela de Livros Fiscais (SF3) a partir do Sigaloja e TOTVS PDV.  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Deverá ser informado no conteúdo do parâmetro **MV\_MODTAUT o modelo 65.**

* **Exemplo:**  
  **{"55","57","65"}** , e dessa maneira o schedule vai ser na SF3 os documentos com F3\_ESPECIE=NFCE.
