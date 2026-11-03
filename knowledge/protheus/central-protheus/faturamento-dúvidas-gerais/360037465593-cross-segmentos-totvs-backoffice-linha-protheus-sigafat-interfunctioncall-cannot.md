---
article_id: 360037465593
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: cb39ab71a2ffd31a577ec2495d507f2a09db431aef317415af915250950563b5
fetched_at: '2026-06-28T22:38:30.060002+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - InterFunctionCall:
  cannot find function OMSVALQBRE in AppMap on MA460PROC(MATA461.PRX)'
type: support-article
updated_at: '2021-10-07T14:22:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037465593-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-InterFunctionCall-cannot-find-function-OMSVALQBRE-in-AppMap-on-MA460PROC-MATA461-PRX
---

**Ocorrência**Ao gerar o documento de saída o sistema apresenta o errorlog abaixo:  
**InterFunctionCall: cannot find function OMSVALQBRE in AppMap on MA460PROC(MATA461.PRX) 23/09/2019 14:11:45 line : 1303**

**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT -  a partir da versão 12.  
  
**Causa**

O erro ocorre, devido a função **OMSVALQBRE**não estar Disponível no RPO ou a rotina pai, a qual a função pertence estar desatualizada.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Efetue o download do pacote de expedição contínua do módulo OMS, detentor da rotina **OMSXFUNA**, que contém a função **OMSVALQBRE**, conforme a release de sistema:

12.1.27: <https://suporte.totvs.com/portal/p/10098/download?e=979470>

12.1.25:<https://suporte.totvs.com/portal/p/10098/download?e=979469>  
12.1.23:<https://suporte.totvs.com/portal/p/10098/download?e=979468>

2. Aplique o pacote viaVs-Code, aceitando os fontes mais atualizados;

3. Posteriormente, inicialize o Smartclient e refaça o processo.

**OBS: O processo informado acima para ser realizado requer um analista com conhecimentos em estrutura de Protheus e uso do VS-Code. Qualquer dúvida no processo, acione a equipe de Advpl.**
