---
article_id: 360027099352
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 358671814455c59295fed3bf57afca1e1bb0c16ecdabdc306b7dabcb55ed227f
fetched_at: '2026-06-28T22:38:31.134172+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP-FAT-  InterFunctionCall- cannot find function CRMXPICTEL
type: support-article
updated_at: '2021-04-28T15:54:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027099352-MP-FAT-InterFunctionCall-cannot-find-function-CRMXPICTEL
---

**Ocorrência**

Ao incluir um contato (**TMKA070**) no cadastro de clientes (**MATA030**), ocorre o erro:

**InterFunctionCall: cannot find function CRMXPICTEL in AppMap on {|a,b,c| FWInitCpo(a,b,c),xRet:=(CRMXPicTel("2")),FWCloseCpo(a,b,c,.T.),xRet }(PROTHEUSFUNCTIONMVC.PRX) 15/02/2019 09:01:30**

**Ambiente**

Microsiga Protheus - a partir da release 12.1.17.

**Causa**

O erro ocorre por falta da função **CRMXPICTEL**no RPO ou mesmo por falta da atualização da rotina detentora da função em questão.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Efetue o download do pacote **CRMXFUNGEN**, rotina pai da função **CRMXPICTEL**para a release utilizada da versão 12:

    12.1.17:<https://suporte.totvs.com/portal/p/10098/download?e=732088>  ;

2. Aplique o pacote via TDS ou o antigo IDE, aceitando os fontes mais atualizados;

3. Posteriormente, reinicialize o Smartclient e refaça o processo.

**OBS: O procedimento informado acima para ser realizado requer um analista com conhecimentos em estrutura de Protheus. Qualquer dúvida no processo, acione a equipe de Framework.**
