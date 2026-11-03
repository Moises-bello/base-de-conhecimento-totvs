---
article_id: 19965090085015
category: Financeiro
content_hash: b9e8069fd1f31e29a3ad3b4714fb334926f96c2e7830491a959a185e9d6b55c5
fetched_at: '2026-06-28T22:38:02.982769+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA100 - Transferência
  entre C/C Ajuda: F100DTCRD - Data de crédito inválida. Verifique se a data informada
  é maior ou igual à data base do sistema'
type: support-article
updated_at: '2023-12-19T13:38:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19965090085015-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA100-Transfer%C3%AAncia-entre-C-C-Ajuda-F100DTCRD-Data-de-cr%C3%A9dito-inv%C3%A1lida-Verifique-se-a-data-informada-%C3%A9-maior-ou-igual-%C3%A0-data-base-do-sistema
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19965090053655) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**

No módulo Financeiro, na rotina **FINA100 - Movimentos Bancários** ao tentar fazer uma transferência entre bancos, através da opção Transferência entre C/C, *F100DTCRD* **Problema:***Data de crédito inválida.* **Solução:***Verifique se a data informada é maior ou igual à data base do sistema.*

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19965090055831)

**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus - FINANCEIRO - Todas as versões

**Causa**Esse Help é apresentado porque você está tentando inserir uma movimentação registrada com data posterior à data do crédito que está sendo informada na transferência.  
  
**Solução**O Help será apresentado, por exemplo, se o login for datado de 13/02/2023 e a data de crédito informada for anterior à data base do sistema (11/02/2023).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19965067141143)

Para solucionar a ocorrência é necessário informar uma data de crédito igual ou superior à data base do sistema. Se você estiver logado com a data **13/02/2023**, deverá informar uma data de crédito igual ou superior a 13/02/2023.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/19965090061847)
