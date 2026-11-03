---
article_id: 360025942734
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: cd08b86f6f7f4bbb37c4d1415aae8721dcc30e8349b7e1106c4311b982da197f
fetched_at: '2026-06-28T22:38:31.242264+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP-FAT-InterFunctionCall - cannot find function OMSM011NFS in AppMap on MATA461IPG
type: support-article
updated_at: '2021-04-28T15:54:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025942734-MP-FAT-InterFunctionCall-cannot-find-function-OMSM011NFS-in-AppMap-on-MATA461IPG
---

**Ocorrência**

Ao faturar o pedido,gera o help: Nofuncw - Problema: Função : OMSM011NFS Calleb By MATA461IPG

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360040454354/mceclip0.png)**

Em alguns caso ao fechar gera o erro: InterFunctionCall: cannot find function OMSM011NFS in AppMap on MATA461IPG(MATA461.PRX) 

**Ambiente**

Microsiga Protheus -  a partir da versão 12.1.17.  
   
 **Causa**

O erro ocorre, devido a função **OMSM011NFS**não estar disponível no RPO ou a rotina pai, a qual a função pertence estar desatualizada.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Efetue o download do **OMSM011**, rotina pai da função **OMSM011NFS**, mais atual, conforme sua versão de ambiente:

**12.1.23: <https://suporte.totvs.com/portal/p/10098/download?e=740851>**

**12.1.17: <https://suporte.totvs.com/portal/p/10098/download?e=740850>**

2. Aplique o pacote via TDS ou o antigo IDE, aceitando os fontes mais atualizados;

3. Posteriormente, inicialize o Smartclient e refaça o processo.

**OBS: O processo informado acima para ser realizado requer um analista com conhecimentos em estrutura de Protheus. Qualquer dúvida no processo, acione a equipe de Framework.**
