---
article_id: 360039277454
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: b39a19abb39e4c097cd9aeff2ce043cc17b48220fa2a16327902c3ce73896f54
fetched_at: '2026-06-28T22:38:31.287278+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP-FAT-Invalid data type on (F0A_FABRIC)
type: support-article
updated_at: '2021-04-28T15:53:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039277454-MP-FAT-Invalid-data-type-on-F0A-FABRIC
---

**Ocorrência**

Ao faturar um pedido com itens que possuem controle por rastreabilidade, o sistema apresenta o erro:

**Invalid data type on (F0A\_FABRIC)**

**in file d:\bamboo-agent-5.7.2\xml-data\build-dir\tp11-tecx17v3-tecxwin64\advpl\instrvar.inl at line 587**  
**on ATUCOMP (MATA926.PRW) 14/05/2019 19:13:37 line : 9639**

**Ambiente**

Microsiga Protheus- a partir da release 12.1.17.  
   
 **Causa**

 Ao faturar as notas, o campo **B8\_DFABRIC** (Data de Fabricação Lote) possuía o conteúdo em formato data, exemplo 20/08/2019 e o campo **D2\_DFABRIC** (Data de Fabricação Lote) vinha com o conteúdo em formato texto, "20190820", causando a  inconsistência no momento de gravar no campo **F0A\_FABRIC**(Data de Fabricação) com a informação da tabela **SD2**.  
   
 **Solução**

Para solucionar essa ocorrência, realize os seguintes passos:  
1. Efetue o download do **MATA926**mais atual, conforme a release de sistema:

12.1.25:<https://suporte.totvs.com/portal/p/10098/download?e=792482> ;

12.1.23:<https://suporte.totvs.com/portal/p/10098/download?e=792481> ;

12.1.17:<https://suporte.totvs.com/portal/p/10098/download?e=792480> ;

2. Aplique o pacote via TDS ou o antigo IDE, aceitando os fontes mais atualizados;

3. Posteriormente, inicialize o Smartclient e refaça o processo.

**OBS: O processo informado acima para ser realizado requer um analista com conhecimentos em estrutura de Protheus. Qualquer dúvida no processo, acione a equipe de Framework.**
