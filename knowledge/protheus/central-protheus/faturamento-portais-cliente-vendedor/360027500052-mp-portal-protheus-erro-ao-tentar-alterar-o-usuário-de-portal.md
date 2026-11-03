---
article_id: 360027500052
category: FATURAMENTO - PORTAIS (Cliente, Vendedor)
content_hash: 3d84bbee141eb526febab57c934e868522a3c8ca43249578df6ab842dbc48964
fetched_at: '2026-06-28T22:38:23.998763+00:00'
product: protheus
section_id: 1500001539321
source: central-protheus
title: MP- Portal Protheus - Erro ao tentar alterar o usuário de portal
type: support-article
updated_at: '2021-04-28T15:15:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027500052-MP-Portal-Protheus-Erro-ao-tentar-alterar-o-usu%C3%A1rio-de-portal
---

**Ocorrência**

Ao alterar o cadastro de usuário de portal.

**Ambiente**

Microsiga Protheus - a partir da versão 12.

**Causa**

O erro gerado é : **array out of bounds ( 0 of 0 ) on {|a,b,c| FWInitCpo(a,b,c),xRet:=(IIF(!INCLUI .AND. !EMPTY(ACOLS[LEN(ACOLS)][2]),POSICIONE("SA1",1,XFILIAL("SA1")+AI4->AI4\_CODCLI+AI4->AI4\_LOJCLI,"A1\_NOME"),"")),FWCloseCpo(a,b,c,.T.),FwSetVarMem(a,b,xRet),xRet }(PROTHEUSFUNCTIONMVC.PRX) 23/10/2018 18:06:52**

Este erro ocorre em razão da validação do inicializador padrão (x3\_relação) do campo **AI4\_NOMCLI** estar incorreto.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1-Acesse o dicionário de dados via configurador;

2-Selecione a tabela AI4 e altere o x3\_relação (inicializador padrão) do campo **AI4\_NOMCLI**:

De: **IIF(!INCLUI .AND. !EMPTY(ACOLS[LEN(ACOLS)][2]),POSICIONE("SA1",1,XFILIAL("SA1")+AI4->AI4\_CODCLI+AI4->AI4\_LOJCLI,"A1\_NOME"),"")**

Para: **IIF(!INCLUI .AND. !EMPTY(AI4->AI4\_CODCLI),POSICIONE("SA1",1,XFILIAL("SA1")+AI4->AI4\_CODCLI+AI4->AI4\_LOJCLI,"A1\_NOME"),"")**

![Altera__o_da_AI4_Nomcli.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360027438052/Altera__o_da_AI4_Nomcli.gif)
