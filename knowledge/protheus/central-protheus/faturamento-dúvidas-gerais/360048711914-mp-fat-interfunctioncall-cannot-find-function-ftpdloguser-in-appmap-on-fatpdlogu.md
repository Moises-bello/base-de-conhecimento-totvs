---
article_id: 360048711914
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 18aa2b683cd607b3600721174d1896f7a8a2ebce44fd12789786d231653fc7eb
fetched_at: '2026-06-28T22:38:31.262128+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'MP-FAT-InterFunctionCall: cannot find function FTPDLOGUSER in AppMap on FATPDLOGUSER(MATN410.PRW)'
type: support-article
updated_at: '2021-04-28T15:53:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048711914-MP-FAT-InterFunctionCall-cannot-find-function-FTPDLOGUSER-in-AppMap-on-FATPDLOGUSER-MATN410-PRW
---

**Ocorrência**Ao tentar realizar a inclusão ou copia de um pedido de venda o erro que esta anexo ocorre:

**InterFunctionCall: cannot find function FTPDLOGUSER in AppMap on FATPDLOGUSER(MATN410.PRW) 23/04/2020 09:39:52 line : 6166**  
   
 **Ambiente**

Microsiga Protheus - a partir da release 12.1.17.

**Causa**

O erro ocorre, devido a função **FTPDLOGUSER ,** relacionada ao tratamento para **LGPD (Lei de Proteção de Dados Sensíveis)**não estar disponível no RPO ou a rotina pai, a qual a função pertence estar desatualizada.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Efetue o download do **FATCRMPD**, rotina pai da função **FTPDLOGUSER** , mais atual, conforme a release de sistema:

**12.1.27:<https://r.totvs.io/p/949607> ;**

**12.1.25:<https://r.totvs.io/p/949606> ;**

**12.1.23:<https://r.totvs.io/p/949605> ;**

**12.1.17:<https://r.totvs.io/p/949604> ;(garantia estendida)**

2. Aplique o pacote via TDS ou o VS CODE, aceitando os fontes mais atualizados;

3. Posteriormente, inicialize o Smartclient e refaça o processo.

**OBS: O processo informado acima para ser realizado requer um analista com conhecimentos em estrutura de Protheus. Qualquer dúvida no processo, acione a equipe de Framework.**

**Caso o ambiente este em Cloud Totvs, o atendimento para atualização será efetuado via atendimento integrado.**
