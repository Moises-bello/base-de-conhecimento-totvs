---
article_id: 360025604591
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 208555a055b7ac38b418129dd2e20b185350d4530c1b247fb8d3e8932a8c049d
fetched_at: '2026-06-28T22:38:31.248160+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'MP-FAT-InterFunctionCall cannot find function GCTSOLIC '
type: support-article
updated_at: '2021-04-28T15:54:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025604591-MP-FAT-InterFunctionCall-cannot-find-function-GCTSOLIC
---

**Ocorrência**Ao gerar o pedido de venda (**mata410**), ocorre o erro:**InterFunctionCall: cannot find function GCTSOLIC in AppMap on A410DELETA(MATA410.PRX)**  
   
 **Ambiente**

Microsiga Protheus - a partir da versão 12.

**Causa**

O erro ocorre por falta da função **GCTSOLIC** no RPO ou mesmo por falta da atualização da rotina detentora da função em questão.  
   
 **Solução**  
 Para solucionar essa ocorrência, realize os seguintes passos:

1. Efetue o download do pacote **CNTXFUN** para a release utilizada da versão 12:

    12.1.17:<https://suporte.totvs.com/portal/p/10098/download?e=742132> ;

    12.1.23:<https://suporte.totvs.com/portal/p/10098/download?e=742133> ;

2. Aplique o pacote via TDS ou o antigo IDE, aceitando os fontes mais atualizados;

3. Posteriormente, reinicialize o Smartclient e refaça o processo.

**OBS: O procedimento informado acima para ser realizado requer um analista com conhecimentos em estrutura de Protheus. Qualquer dúvida no processo, acione a equipe de Framework.**
