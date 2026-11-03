---
article_id: 9221081956375
category: Faturamento - Cenários de Venda
content_hash: 0ac2dbca843b3d96c6d813cb055bdb1f3e48ecd55c56c136fc5448dc38f5d1e5
fetched_at: '2026-06-28T22:38:33.961345+00:00'
product: protheus
section_id: 1500001550382
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Parâmetros relacionados
  a reajuste de tabela de preço
type: support-article
updated_at: '2022-09-29T17:05:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9221081956375-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Par%C3%A2metros-relacionados-a-reajuste-de-tabela-de-pre%C3%A7o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Descrição sobre os parâmetros relacionados a reajuste de tabela de preço.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Solução**

Para reajuste de uma tabela usando a opção de Outras Ações, Reajuste é possível selecionar os seguintes parâmetros:

* Produtos da tabela de preços a serem reajustados (**Produto inicial**/**Produto Final**);
* Grupos de Produtos da tabela de preços a serem reajustados (**Grupo Inicial**/**Grupo Final**);
* Tipos de Produtos da tabela de preços a serem reajustados (**Tipo Inicial**/**Tipo Final**);
* Tabelas de Preços a serem reajustadas (**Tabela Inicial**/**Tabela Final**);
* Fator de Reajuste a ser utilizado (**Fator de Reajust**.) - Caso não informado valor de reajuste, o sistema apenas irá atualizar o preço de venda da tabela de preços, caso os valores contidos entre a tabela de preços e a Planilha de preços forem diferentes, e o parâmetro (**Reaplica Fator**) estiver como Preço tabela. Caso o parâmetro (**Reaplica Fator**) estiver como Preço base o sistema não realizará nenhum ajuste, desconsiderando também o parâmetro (**Atualiza Preço Base (Produto).**
* conforme o valor contido na Planilha se estiverem diferentes.
* Número de decimais para arredondamento no calculo do reajuste (**Número de Decimais**);
* Se os pedidos já gravados devem ser reajustados (**Pedidos em Carteira**);
* Se o reajuste será aplicado na tabela base (Cadastro de Produtos) ou na Tabela de Preços (**Reaplica Fator**);
* Nome da planilha de formação de preços no qual será reajustado (**Planilha**); A planilha utilizada neste parâmetro é a **Standard.pdv** da consulta formação de preço;
* Se o preço base do cadastro de produtos será ou não atualizado (**Atualiza Preço Base (Produto)**);
* Grades de Produtos da tabela de preços a serem reajustadas (**Referencia de Grade Inicial**/**Referencia de Grade Final**).

**Saiba mais: [Tabelas de Preço - OMSA010 - Faturamento - P12](https://tdn.totvs.com/x/BwEtDw)**
