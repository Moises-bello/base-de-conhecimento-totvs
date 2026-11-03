---
article_id: 4404434911895
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: bc45cd43dd7dfa2bee2ba1b030e948455a3a31cd135b1e0a3ca795689bc94a01
fetched_at: '2026-06-28T22:38:38.393586+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento - array out
  of bounds ( 0 of 120 ) on MA410IMPOS(MATN410B.PRW)
type: support-article
updated_at: '2021-07-16T19:53:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4404434911895-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-Faturamento-array-out-of-bounds-0-of-120-on-MA410IMPOS-MATN410B-PRW
---

**Ocorrência**

Ao acessar a planilha financeira, gera o erro: **array out of bounds ( 0 of 120 )  on MA410IMPOS(MATN410B.PRW) 11/12/2020 15:20:00 line : 614**

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Faturamento - Todas as versões  
  
**Causa**O erro de array out of bounds significa que está sendo procurado um campo utilizado no array que não existe no dicionário, ou não está marcado para uso ou teve seu nível de campo mudado.  
  
Neste caso o sistema está tentado encontrar o campo **c6\_clasfis** que alimentará o array **aCols[nX,nPClasFis** e não está encontrando, gerando o erro em questão.  
  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Via configurador, dicionário de dados, tabela SC6, valide se o campo **C6\_CLASFIS** existe na tabela, se está marcado como usado e se está com nível igual a  1. Caso não esteja, efetue a marcação do campo como usado e deixe o nível igual a 1, salve o campo, salve a tabela sc6, atualize o dicionário de dados, reinicie o smartclient e efetue o processo novamente.
