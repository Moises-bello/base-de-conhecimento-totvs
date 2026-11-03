---
article_id: 360061560414
category: RH - FGTS / SEFIP
content_hash: 8f9cf989281773f7a708eee746a6e518e541cffb5c0dc337fa858a1fd6a53a9f
fetched_at: '2026-06-28T22:43:41.238951+00:00'
product: protheus
section_id: 360003115651
source: central-protheus
title: RH - Linha Protheus - GPE - Erro 1245 na Sefip declaratória de 13º para funcionários
  em contrato determinado
type: support-article
updated_at: '2025-08-14T17:48:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061560414-RH-Linha-Protheus-GPE-Erro-1245-na-Sefip-declarat%C3%B3ria-de-13%C2%BA-para-funcion%C3%A1rios-em-contrato-determinado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34185843952151)** Tempo aproximado para leitura: **00:01:30 min**  
**Ocorrência**Ao simular a Sefip declaratória de 13º para funcionários em contrato determinado, Sefip apresenta o erro 1245:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003119722)  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17.  
  
**Causa**O problema ocorre por um erro no próprio validador da Sefip, pois conforme layout, para a competência 13 não deve ser informado código de movimentação:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360101998054)  
  
**Solução**Deve ser informada a movimentação diretamente no validador da Sefip, pois dessa forma o erro não ocorre ao realizar a simulação:  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500003161801)

**Saiba mais:**

[RH \_ FGTS/SEFIP](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360003115651-RH-FGTS-SEFIP)
