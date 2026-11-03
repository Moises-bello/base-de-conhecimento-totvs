---
article_id: 4405654432535
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: ff64c76900da65b04a60fd36494b8cd47b1b8a2a5f06f994baad7307da99c5c6
fetched_at: '2026-06-28T22:38:38.447084+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - array out of
  bounds ( 0 of 80 )  on A410INCREM(FISXFUN.PRX)
type: support-article
updated_at: '2021-08-04T19:49:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405654432535-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-array-out-of-bounds-0-of-80-on-A410INCREM-FISXFUN-PRX
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00min****Ocorrência**

Ao clicar em outras ações, Amarração de NFS no pedido de vendas, gera o erro: **array out of bounds ( 0 of 80 )  on A410INCREM(FISXFUN.PRX)**  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT- Todas as versões  
  
**Causa**Erro de array out of bounds ocorre quando um campo do array não existe no dicionário de dados, ou não está marcado o uso ou mudou o nível do campo.  
  
A rotina **A410INCREM** está verificando se há integração com o projeto PMS e se os campos abaixo não estão vazios:  
  
**C6\_PROJPMS**  
**C6\_EDTPMS**  
**C6\_TASKPMS**

Desta forma, é necessário validar se os campos existem no dicionário de dados, configurador, tabela SC6, se estão marcados como usado e se estão com o nível igual a 1.

**Solução**

Para solucionar essa ocorrência, realize os seguintes passos:

1. Via configurador, dicionário de dados, tabela SC6, valide se os campos **C6\_PROJPMS,** **C6\_EDTPMS e**  
**C6\_TASKPMS** existem na tabela, se estão marcados como usado e se estão com nível igual a  1.

2. Caso não estejam, efetue a marcação dos campos como usado e deixe o nível igual a 1, salve o campo, salve a tabela sc6, atualize o dicionário de dados, reinicie o smartclient e efetue o processo novamente.
