---
article_id: 360041806273
category: Gestão de Transportes (TMS)
content_hash: 879bbffe87ae23f9baa8b30fe363f0f845fe96d83ce52d8cc84ea8f46f87e09b
fetched_at: '2026-06-28T22:45:32.503443+00:00'
product: protheus
section_id: 206956808
source: central-protheus
title: Logística - Linha Protheus - TMS - Quais status são listados na tela de liberação
  de contrato de carreteiro
type: support-article
updated_at: '2023-02-28T14:09:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041806273-Log%C3%ADstica-Linha-Protheus-TMS-Quais-status-s%C3%A3o-listados-na-tela-de-libera%C3%A7%C3%A3o-de-contrato-de-carreteiro
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:20 min  
  
Dúvida**Quais status são listados na tela de liberação de contrato de carreteiro?  
  
**Ambiente**TOTVS Logística - TOTVS TMS (Linha Protheus) - Gestão de Transportes (TMS) - Todas as versões

**Solução**São listados os contratos conforme pergunte :

* **Filtra Contratos ? 1=Aguard. Lib, 2=Liberados, 3=Ambos**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055971353/mceclip0.png)

1. Se for = 1 (Aguard. Lib) -> filtra **DTY\_STATUS = 2**
2. Se for = 2 (Liberados)    -> filtra **DTY\_STATUS = 3, 8 ou B**
3. Se for = 3 (Ambos)        -> filtra **DTY\_STATUS = 2, 3, 8 ou B**

* Sendo:
  + 1 - legenda VERDE - **Em Aberto**
  + 2 - legenda AMARELA - **Aguardando Liberação p/ Pagamento**
  + 3 - legenda LARANJA" - **Liberação p/ Pagamento**
  + 4 - legenda AZUL" - **Contrato Quitado com Ped. de Compra**
  + 5 - legenda VERMELHO" - **Contrato Quitado/Pagamento Realizado**
  + A - legenda VERDE\_ESCURO" - **Contr.Parcial/Pagto Parcial**
  + 6 - legenda CINZA" - **Titulo em Fatura**
  + 7 - legenda BRANCO" - **Aguardando Confirm.Web Service**
  + 8 - legenda MARRON" - **Aguardando Autoriz.Pagto**
  + B - F12\_MARROM' - **Contrato Quitado/Aguardando autorização Operadora**
  + 9 - legenda PRETO" - **Pagamento Bloqueado**

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360055087094/mceclip1.png)

Ou substituído pela informação do ponto de entrada **TM251FIL.**  
**[TM251FIL - Filtro na Tela de Liberação de Contratos](http://tdn.totvs.com/pages/releaseview.action?pageId=45225512)**
