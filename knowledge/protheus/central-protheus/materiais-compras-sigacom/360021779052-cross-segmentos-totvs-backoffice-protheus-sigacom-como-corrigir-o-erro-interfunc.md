---
article_id: 360021779052
category: Materiais - Compras (SIGACOM)
content_hash: 10abc3ed17272668be40ecf7f72ea271daa667b891a99b9e6b0f1421e7fbdbc1
fetched_at: '2026-06-28T22:41:07.583900+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como corrigir o erro
  InterFunctionCall: cannot find function _FWMBPICTV ?'
type: support-article
updated_at: '2022-05-16T22:17:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021779052-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-corrigir-o-erro-InterFunctionCall-cannot-find-function-FWMBPICTV
---

**Dúvida**Como corrigir o erro InterFunctionCall: cannot find function \_FWMBPICTV ?

**Ambiente**Proteus – Compras – A partir da versão 12.1.17  
  
**Solução**

Referente à ocorrência do erro abaixo:

***InterFunctionCall: cannot find function \_FWMBPICTV in AppMap on { || \_FWMBPICTVAR('SC7','C7\_CODITE','RTPICT("C7\_CODGRP") ')}(FWBRWMODELCONFIG.PRW)***,

No Compras pode ocorre em diversas tabelas, por exemplo: SC7, SC8, SC1, SD2.

Não é necessário remover nenhuma validação na tabela SX3. sendo necessário realizar a manutenção no profile do usuário que está apresentando o erro via configurador.

Para correção deve-se apagar todos os registros no profile.usr com o campo P\_TYPE contendo BROWSESA1, BROWSESC0, BROWSESC1, BROWSESC7, BROWSESC8 e BROWSESC9.
