---
article_id: 360000806467
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: 0677386a7085ee56d2f49311a01391b30710a424d5f574096edc92ac02b79e73
fetched_at: '2026-06-28T22:38:41.088332+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Array out of
  bounds (0 of 107) on Aftercols (MATA410.prx)
type: support-article
updated_at: '2021-09-21T17:41:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000806467-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Array-out-of-bounds-0-of-107-on-Aftercols-MATA410-prx
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:03:00 min***

**Ocorrência**

Ao copiar o pedido, gera o erro: Ao copiar o pedido de venda gera error.log - **array out of bounds ( 0 of 107 )  on AFTERCOLS(MATA410.PRX).**

**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-Faturamento (SIGAFAT) - todas as versões.  
  
**Causa**

Este erro ocorre quando os campos que fazem parte do array, não existem no dicionário de dados ou não estão marcados o uso.

A grande parte das ocorrênciasestão relacionadas aos campos **C6\_PEDCLI** e/ou **C6\_ENTREG** não estão em uso ou não existem no **SX3** ou no banco de dados (tabela **SC6**).

Outras ocorrências deste erro foram relacionadas aos campos **C6\_NFORI** e/ou **C6\_SERIORIG,** que não estavam em uso no **SX3** e eram requeridos no processo.

Também pode ocorrer se o campo **C6\_IDENTB6** não estiver com o seu uso marcado, este campo é requerido na função **Aftercols**, assim também como os campo **C6\_GRADE**, **C6\_PRODUTO** e **C6\_QTDLIB**.

Também valide o **nível de campo,** que quando mudado do padrão 1, pode gerar problemas de array.

**Solução**  
Para solucionar essas ocorrências, realize os seguintes passos:  
1. Verifique se via configurador, se os campos estão em uso;  
2. Verifique se os campos existem na tabela SX3;  
3. Verifique se os campos existem dentro da tabela SC6.

Obs: Para o caso de falta de campo no Dicionário de Dados, é necessário efetuar o download do **Dicionário de Dados** no portal do cliente, conforme a sua release de uso e posteriormente, processar o **UPDDISTR** para que o ambiente assuma a atualização de Dicionário de Dados.

Feito o procedimento, reinicie o Protheus e efetue o processo novamente.

**Importante**: Na ***versão 12***, o erro na função **AFTERCOLS** é "**Array out of bounds ( 0 of 55 )  on AFTERCOLS(MATN410.PRW)"**, porém, as verificações de causa e a solução a ser aplicada, é exatamente a mesma.
