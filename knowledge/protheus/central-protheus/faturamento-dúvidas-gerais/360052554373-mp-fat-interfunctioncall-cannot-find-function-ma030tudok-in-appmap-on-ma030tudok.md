---
article_id: 360052554373
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: bfe34c4ea9b09bcbb746dc5448f4fb0f6dc4add6a40eb94984e531e4181461e8
fetched_at: '2026-06-28T22:38:31.273376+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'MP-FAT-InterFunctionCall: cannot find function MA030TUDOK in AppMap on { ||
  MA030TudOk(nOpc)}(MATXATU.PRX) '
type: support-article
updated_at: '2021-04-28T15:53:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052554373-MP-FAT-InterFunctionCall-cannot-find-function-MA030TUDOK-in-AppMap-on-MA030TudOk-nOpc-MATXATU-PRX
---

**Ocorrência**Ao alterar o cadastro do cliente, gera o erro:

InterFunctionCall: cannot find function MA030TUDOK in AppMap on { || MA030TudOk(nOpc)}(MATXATU.PRX) 06/04/2020 15:39:35

**Ambiente**

Microsiga Protheus: a partir da release 12.1.17.

**Causa**

O erro ocorre, devido a função **MA030TUDOK**não estar Disponível no RPO ou a rotina pai, a qual a função pertence estar desatualizada.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Efetue o download do **MATV030** , rotina pai da função **MA030TUDOK**, mais atual, conforme a release de sistema:

12.1.27: correção dentro do pacote de acumulados do módulo: **<https://suporte.totvs.com/portal/p/10098/download#detail/954520>** ;

12.1.25: correção dentro do pacote de acumulados do módulo: <https://suporte.totvs.com/portal/p/10098/download#detail/801245> ;

12.1.23:correção dentro do pacote de acumulados do módulo: **<https://suporte.totvs.com/portal/p/10098/download#detail/754646>** ;

12.1.17:correção dentro do pacote de acumulados do módulo: **<https://suporte.totvs.com/portal/p/10098/download#detail/783264>.**

Caso os links diretos, não abram, segue o link da página geral de faturamento, onde as atualizações de encontram**: <https://tdn.totvs.com/x/Iw4dHw>**

2. Aplique o pacote via TDS ou o VS-CODE, aceitando os fontes mais atualizados;

3. Posteriormente, inicialize o Smartclient e refaça o processo.

**OBS: O processo informado acima para ser realizado requer um analista com conhecimentos em estrutura de Protheus. Qualquer dúvida no processo, acione a equipe de Framework.**
