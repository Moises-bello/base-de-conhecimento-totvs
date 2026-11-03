---
article_id: 360044212913
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 532ad2cf60d6b5035439f6a11b3840fe2ed718a3c8d086f5c353f35d7f332b27
fetched_at: '2026-06-28T22:38:43.856229+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Bloqueio de
  alteração do número da Nota Fiscal de Saída
type: support-article
updated_at: '2023-05-16T14:57:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044212913-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Bloqueio-de-altera%C3%A7%C3%A3o-do-n%C3%BAmero-da-Nota-Fiscal-de-Sa%C3%ADda
---

**Dúvida**

Como bloquear a alteração do número da nota fiscal de saída no momento da sua preparação (**MATA461**)?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Solução**

Retire o acesso do usuário via configurador, desta forma, o usuário não poderá efetuar a alteração do número da nota no momento da preparação:

![](https://totvssuporte.zendesk.com/attachments/token/iU7WN3ma5EtN7i2BGYtowt556/?name=inline1608136237.png)​  
Altere também o parâmetro **MV\_MUDANUM** para não permitir alteração.

Saiba mais: **[FAT0049 Controle de Numeração de Documento de Saída no Protheus](https://tdn.totvs.com/pages/viewpage.action?pageId=329024579)**
