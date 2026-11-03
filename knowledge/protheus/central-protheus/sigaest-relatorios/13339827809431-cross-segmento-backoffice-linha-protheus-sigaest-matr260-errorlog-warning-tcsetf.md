---
article_id: 13339827809431
category: SIGAEST - RELATORIOS
content_hash: 6f433976a6eeb3ae087bb27d0c29daf138744e787c62512d01372b99ce3bffbe
fetched_at: '2026-06-28T22:39:06.072793+00:00'
product: protheus
section_id: 1500001538841
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATR260 - Error.log
  - : WARNING - TCSetField - Invalid field len: 21 on { | X | IIF( X[2] <> "C", TCSETFIELD(CALIASSB2,
  X[1], X[2], X[3], X[4] ), NIL ) }(MATR260.PRX)'
type: support-article
updated_at: '2023-03-24T16:35:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13339827809431-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATR260-Error-log-WARNING-TCSetField-Invalid-field-len-21-on-X-IIF-X-2-C-TCSETFIELD-CALIASSB2-X-1-X-2-X-3-X-4-NIL-MATR260-PRX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min****Ocorrência**Ao tentar emitir o relatório ***POSIÇÃO DE ESTOQUES ANALÍTICO (MATR260)*** apresenta o seguinte error.log em tela.

***: WARNING - TCSetField - Invalid field len: 21 on { | X | IIF( X[2] <> "C", TCSETFIELD(CALIASSB2, X[1], X[2], X[3], X[4] ), NIL ) }(MATR260.PRX)***

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13340079388055)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões  
  
**Causa**Esse incidente ocorre devido inconsistência nos tamanhos de campos das tabelas de Saldos e Movimentações no ambiente. Geralmente quando tem necessidade de alterar os campos e/ou decimais das ***tabelas SB2, SB6, SB9, SC2, SD1, SD2, SD3 entre outras*** que movimentam saldo dos produtos.

***Por exemplo:*** Os campos **B2\_QFIM** e **B9\_QINI** devem ter o mesmo tamanho. Veja abaixo mais detalhadamente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13341148557719)

**Solução** - Para solucionar essa ocorrência, realize os seguintes passos:

***- 1º -*** Revise o tamanho dos campos das tabelas SB2 e SB9 se estão incompatíveis, por exemplo B9\_QINI comparando com o B2\_QFIM. Nesse cenário **recomendamos que revise no link abaixo** as principais tabelas envolvidas e instruções dos campos que devem ser avaliados para ajustes de tamanhos. O link é uma referência para facilitar a identificação das tabelas que precisa revisar.

[***Como aumentar a quantidade de casas decimais para campos de custos e quais as principais tabelas envolvidas***](https://tdn.totvs.com/display/public/PROT/PEST06012+-+MATA330+-+Como+aumentar+a+quantidade+de+Casas+Decimais+para+os+campos+de+CUSTOS)

***- 2º -*** É extremamente importante efetuar o processo de ajustes dos campos pelo ***módulo Configurador (SIGACFG),*** e após alterados e ajustados os campos, antes de emitir o relatório [***reinstalar todas as STORED PROCEDURES***](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009382821-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-instalar-as-Stored-Procedures-) do ambiente.

***Saiba Mais:***  
[Clique aqui e veja mais artigos sobre Relatórios no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538841-SIGAEST-RELATORIOS)

[SIGAEST -Quais impactos da alteração de tamanho ou decimais em campos do Módulo Estoque/Custos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4413436322839-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Quais-impactos-da-altera%C3%A7%C3%A3o-de-tamanho-ou-decimais-em-campos-do-M%C3%B3dulo-Estoque-Custos-?source=search)
