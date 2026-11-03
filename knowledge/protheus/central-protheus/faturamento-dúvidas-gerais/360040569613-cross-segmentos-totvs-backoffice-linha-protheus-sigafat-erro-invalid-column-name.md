---
article_id: 360040569613
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 3bcfd9e2874821549a91665ae68d1bfd1c811d12246753480f179c36a05de090
fetched_at: '2026-06-28T22:38:30.092722+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT - Erro Invalid column
  name
type: support-article
updated_at: '2023-06-07T12:20:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360040569613-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Erro-Invalid-column-name
---

**Dúvida**Ao gravar um registro no sistema, gera um erro log: **Invalid column name "XXXX"**

**Ambiente**Cross Segmentos-TOTVS Backoffice (Linha Protheus) - SIGAFAT - A partir da release 12.1.17;

**Causa**Este incidente ocorre quando há um **campo virtual de usuário na****estrutura "SX3"**, com uso da **função Posicione();**

Esse tipo de erro pode ocorrer em qualquer rotina (Pedido de vendas/Liberação do Pedido/Geração de documento de saída, etc.) e qualquer operação que esta rotina efetue (incluir/alterar/copiar/excluir, por exemplo). Um vez que existe o campo de usuário com a função Posicione, deve-se observar as premissas para tratar a função dentro do campo.

**Solução**Para solucionar essa ocorrência, realize os seguintes passos:

**Exemplo de incidente, "Pedido de Venda" - "Invalid column name 'A1\_NOME'.*";***

* Verifique como esta configurada a **função posicione**, caso esteja neste modelo (exemplo):
  + ***POSICIONE("SA1",1,XFILIAL("SA1")+M->C5\_CLIENTE,"A1\_NOME");***
* Realize alteração para este modelo:
  + **POSICIONE("SA1",1,XFILIAL("SA1")+SC5->C5\_CLIENTE+C5\_LOJACLI,"A1\_NOME")**

Devido algumas alterações no DBACCESS, a equipe de tecnologia da TOTVS está verificando a nova configuração descrita acima, valide se ao alterar a configuração o erro deixa de ocorrer.

**Obs: Cada Campo dentro da instrução deve ser associado ao seu devido aliás, no caso do A1\_NOME, que é o campo relacionado ao erro, ele deverá ser relacionado ao seu aliás de tabela, "SA1->A1\_NOME".**
