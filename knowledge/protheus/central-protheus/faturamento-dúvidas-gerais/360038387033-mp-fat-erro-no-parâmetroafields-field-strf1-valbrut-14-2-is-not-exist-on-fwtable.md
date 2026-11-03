---
article_id: 360038387033
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: a75ba1ce8265a512edf90797a204e42f1794d14f3dff4ae376367442b4f1ac62
fetched_at: '2026-06-28T22:38:31.198009+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'MP-FAT-erro no parâmetroaFields: Field STR(F1_VALBRUT, 14, 2) is not exist
  on FWTABLESTRUCT'
type: support-article
updated_at: '2021-04-28T15:53:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360038387033-MP-FAT-erro-no-par%C3%A2metroaFields-Field-STR-F1-VALBRUT-14-2-is-not-exist-on-FWTABLESTRUCT
---

**Ocorrência**

Ao efetuar o retorno de documento de entrada na opção retornar do pedido de vendas (**MATA410**), ocorre o erro:

**erro no parâmetroaFields: Field STR(F1\_VALBRUT, 14, 2) is not exist on FWTABLESTRUCT:ADDINDEX(FWTABLESTRUCT.PRX) 14/10/2019 18:33:48 line : 380**

**Ambiente**

Microsiga Protheus - a partir da release 12.1.17.  
   
 **Causa**

O erro ocorria quando se tentava retornar a nota com a opção fornecedor marcada, devido ao uso da função **STR()**, na criação do índice da **SF1.**

**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:

1. Efetue o download do **MATN410A** , conforme a release de sistema:

      12.1.25:<https://suporte.totvs.com/portal/p/10098/download?e=829079> ;

      12.1.23:<https://suporte.totvs.com/portal/p/10098/download?e=829078> ;

      12.1.17:<https://suporte.totvs.com/portal/p/10098/download?e=829077> ;

2. Aplique o pacote via TDS ou o antigo IDE, aceitando os fontes mais atualizados;

3. Posteriormente, inicialize o Smartclient e refaça o processo.

**OBS: O processo informado acima para ser realizado requer um analista com conhecimentos em estrutura de Protheus. Qualquer dúvida no processo, acione a equipe de Framework.**
