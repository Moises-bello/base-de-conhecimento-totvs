---
article_id: 360039347414
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: cf3ee8cee608762ed4533e0edb633092a25b32a0bbab964c77855a9edf4c04e0
fetched_at: '2026-06-28T22:38:31.201148+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'MP-FAT-erro no parâmetroaFields: IndexKey already exist on FWTABLESTRUCT:ADDINDEX(FWTABLESTRUCT.PRX)'
type: support-article
updated_at: '2021-04-28T15:53:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039347414-MP-FAT-erro-no-par%C3%A2metroaFields-IndexKey-already-exist-on-FWTABLESTRUCT-ADDINDEX-FWTABLESTRUCT-PRX
---

**Ocorrência**

Ao efetuar o retorno de compras no pedido de vendas (**MATA410**) gera o error.log: erro no erro no **parâmetroaFields: IndexKey already exist on FWTABLESTRUCT:ADDINDEX(FWTABLESTRUCT.PRX) 12/07/2019 17:27:31 line : 407**

**Ambiente**

Microsiga Protheus - a partir da release 12.1.17.  
   
 **Causa**

O erro ocorria quando o ambiente possuía um índice na tabela **SF1** (Cabecalho da Nf de Entrada) com algum campo do tipo Data e tentava-se utilizar a opção Retornar da rotina de Pedidos de Venda(**MATA410**).

**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:

1. Efetue o download do **MATN410a** , mais atual, conforme a release de sistema:

12.1.25:<https://suporte.totvs.com/portal/p/10098/download?e=808223> ; 12.1.23:<https://suporte.totvs.com/portal/p/10098/download?e=808222> ; 12.1.17:<https://suporte.totvs.com/portal/p/10098/download?e=808221> ;

2. Aplique o pacote via TDS ou o antigo IDE, aceitando os fontes mais atualizados;

3. Posteriormente, inicialize o Smartclient e refaça o processo.

**OBS: O processo informado acima para ser realizado requer um analista com conhecimentos em estrutura de Protheus. Qualquer dúvida no processo, acione a equipe de Framework.**
