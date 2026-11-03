---
article_id: 360036628714
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 95691f28164a51edce0159ad2a3fe71b30655d5a7c3bcec23dd59e502ef2152f
fetched_at: '2026-06-28T22:38:31.164805+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP-FAT-array out of bounds [5] of [4] on TRATAFILT(MATR550.PRX)
type: support-article
updated_at: '2021-04-28T15:54:01Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036628714-MP-FAT-array-out-of-bounds-5-of-4-on-TRATAFILT-MATR550-PRX
---

**Ocorrência**

Ao gerar o relatório matr550 em modo sintético, ocorre o erro: **array out of bounds [5] of [4] on TRATAFILT(MATR550.PRX) 10/12/2018 14:03:14 line : 3692**  
   
 **Ambiente**

Microsiga Protheus - a partir da release 12.1.17.  
   
 **Causa**

O problema ocorria ao desmarcar a impressão da Página de Parâmetros no Relatório de Notas Fiscais e confirmar o processamento.  
   
 **Solução**  
 Para solucionar essa ocorrência, realize os seguintes passos:

1. Efetue o download do **matr550** conforme a versão do seu ambiente:

12.1.23:<https://suporte.totvs.com/portal/p/10098/download?e=742068> ;

12.1.17:<https://suporte.totvs.com/portal/p/10098/download?e=742067> ;

2. Aplique o pacote via TDS ou o antigo IDE, aceitando os fontes mais atualizados;

3. Posteriormente, inicialize o Smartclient e refaça o processo.

**OBS: O processo informado acima para ser realizado requer um analista com conhecimentos em estrutura de Protheus. Qualquer dúvida no processo, acione a equipe de Framework.**
