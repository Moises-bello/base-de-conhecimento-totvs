---
article_id: 360034817274
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 56ff53165e159577129b87c570b4f9d76a1279d5f1dc0ffc03e3dad1776e3beb
fetched_at: '2026-06-28T22:38:31.268123+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: 'MP-FAT-InterFunctionCall: cannot find function M461ENTG in AppMap on '
type: support-article
updated_at: '2021-04-28T15:54:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034817274-MP-FAT-InterFunctionCall-cannot-find-function-M461ENTG-in-AppMap-on
---

**Ocorrência**Ao passar pelo parâmetro de "Agrupadores" na opção de menu Documento de saida, gera error.log:

**InterFunctionCall: cannot find function M461ENTG in AppMap on {|aResp| aResp := RetMvPar(), \_\_ReadVar := 'MV\_PAR16',lOk := M461ENTG(),aPergunta[16,8] := mv\_par16,RetMvPar(aResp,\_\_oDlg),lOk}(APLIB090.PRW) 02/04/2019 11:41:04**

**Ambiente**

Microsiga Protheus -  a partir da release 12.1.17.

**Causa**

O erro ocorre, devido a função **M461ENTG**não estar Disponível no RPO ou a rotina pai, a qual a função pertence estar desatualizada.

**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:  
1. Efetue o download do **MATA461**, rotina pai da função **M461ENTG**, mais atual conforme o ambiente utilizado:

**12.1.25:<https://suporte.totvs.com/portal/p/10098/download?e=787880> ;**

**12.1.23:<https://suporte.totvs.com/portal/p/10098/download?e=787879> ;**

**12.1.17:<https://suporte.totvs.com/portal/p/10098/download?e=787878> ;**

2. Aplique o pacote via TDS ou o antigo IDE, aceitando os fontes mais atualizados;

3. Posteriormente, inicialize o Smartclient e refaça o processo.

**OBS: O processo informado acima para ser realizado requer um analista com conhecimentos em estrutura de Protheus. Qualquer dúvida no processo, acione a equipe de Framework.**
