---
article_id: 115013175648
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 0dc9954103eeca37b07132e54f54b60e2011404bd47e0a9d8f7d9832e6378725
fetched_at: '2026-06-28T22:38:30.046559+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Variable does
  not exist c5_tipo on A410SNFORI
type: support-article
updated_at: '2021-09-21T20:26:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/115013175648-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Variable-does-not-exist-c5-tipo-on-A410SNFORI
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:02:00 min**

**Ocorrência**

Quando efetua a devolução/retorno de uma nota de entrada de beneficiamento, ocorre o erro: **variable does not exist c5\_tipo on A410SNFOR**  
  
**Causa**  
A mensagem ocorre por que o campo **D1\_IDENTB6** está em **branco** ou **diferente do conteúdo B6\_IDENT**, com isso, o sistema compara os campos que são chaves neste tipo de pedido, e como não encontra a informação correta retorna com o log de evento.  
  
**Linha de erro no índice:**

**Indice (1) : SB60102 B6\_FILIAL+B6\_PRODUTO+B6\_CLIFOR+B6\_LOJA+B6\_PODER3.**  
  
Uma possibilidade é ter utilizado um TES não condizente ao uso de uma nota de beneficiamento , exemplo, recebendo material para beneficiar, com TES configurado com ***poder de terceiros igual a devolução***, com isso **D1\_IDENTB6** não é alimentado.  
  
**Ambiente**  
Cross Segmentos-TOTVS Backoffice (Linha Protheus)-Faturamento (SIGAFAT) - todas as versões.

**Solução**  
Para solucionar, estorne a nota de entrada e lance-a novamente, utilizando um TES com **c*ontrole de* *poder de terceiros igual a remessa.***
