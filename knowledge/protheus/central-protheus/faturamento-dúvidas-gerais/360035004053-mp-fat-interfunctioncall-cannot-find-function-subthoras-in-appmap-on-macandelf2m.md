---
article_id: 360035004053
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 618cdd5a3a0fa020fc0d5c18dd57efbb488dc71d52c7ac6c894bc4ea563a4af7
fetched_at: '2026-06-28T22:38:31.276675+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'MP-FAT-InterFunctionCall: cannot find function SUBTHORAS in AppMap on MACANDELF2(MATA521.PRX)'
type: support-article
updated_at: '2021-04-28T15:54:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035004053-MP-FAT-InterFunctionCall-cannot-find-function-SUBTHORAS-in-AppMap-on-MACANDELF2-MATA521-PRX
---

**Ocorrência**

Ao tentar excluir uma nota no faturamento está ocorrendo o seguinte erro:

**InterFunctionCall: cannot find function SUBTHORAS in AppMap on MACANDELF2(MATA521.PRX)**  
   
 **Ambiente**

Microsiga Protheus - a partir da release 12.1.17.  
   
 **Causa**

O erro ocorre, devido a função **SUBTHORAS** não estar Disponível no RPO ou a rotina pai, a qual a função pertence estar desatualizada.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Efetue o download do **Tecxfun**, rotina pai da função **SUBTHORAS** , mais atual:  [**https://suporte.totvs.com/portal/p/10098/download?e=759569**](https://suporte.totvs.com/portal/p/10098/download?e=759569) ;  
2. Aplique o pacote via TDS ou o antigo IDE, aceitando os fontes mais atualizados;  
3. Posteriormente, inicialize o Smartclient e refaça o processo.

**OBS: O processo informado acima para ser realizado requer um analista com conhecimentos em estrutura de Protheus. Qualquer dúvida no processo, acione a equipe de Framework.**
