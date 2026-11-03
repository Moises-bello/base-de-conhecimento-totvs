---
article_id: 360021940952
category: Materiais - Compras (SIGACOM)
content_hash: 6eee1dae5a01629c9fe410bbeee8fe52eda16d4d56ba6751cf3d43d30f7b9ada
fetched_at: '2026-06-28T22:41:15.759922+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como diferenciar uma
  Pré Nota de um Documento de Entrada ?
type: support-article
updated_at: '2026-06-08T21:33:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021940952-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-diferenciar-uma-Pr%C3%A9-Nota-de-um-Documento-de-Entrada
---

**Dúvida**  
Como diferenciar uma Pré-Nota de um Documento de Entrada ?

**Ambiente**  
Microsiga Protheus – Compras – A partir da versão 11.80

**Solução:**

Por padrão, as rotinas de Pré Nota (**MATA140**) e Documento de Entrada (**MATA103**) possuem legendas de identificação.

A Prenota é o cadastro prévio dos dados básicos do Documento Fiscal, que será recebido pela empresa, o objetivo deste cadastro é facilitar e agilizar o recebimento de materiais registrados na rotina Documento de Entrada. Com os dados previamente cadastrados no Sistema, não é necessário digitar todas as informações relacionadas ao Documento Fiscal, basta apenas complementá-las. Não é gerado nenhum lançamento fiscal, contábil ou financeiro e nem é atualizado o estoque do produto.

Já a Nota ou Documento de Entrada inicia o processo de atualização online de dados financeiros, de estoques e custos. Além disso, essa rotina também permite que os materiais recebidos pelo Recebimento de Materiais sejam classificados e os devidos lançamentos efetuados.

Caso a consulta seja realizada através de queryes no Banco de Dados ou via tabela, o comportamento sistêmico é efetuado do seguinte modo:

Ao gerar uma Prenota, o sistema prepara os campos 'Status da NF'(**F1\_STATUS**), 'Data de Recebimento'(**F1\_RECBMTO**), 'Data de Digitação'(**F1\_DTDIGIT**), mantendo a legenda conforme conteúdo do campo 'Status da NF' (**F1\_STATUS**).

No caso da **Prenota**, o campo 'Status da NF' (**F1\_STATUS**) **ficará vazio**, o campo 'Data de Recebimento'(F1\_RECBMTO) manterá a data base em que a Pré nota foi incluída no sistema e o campo 'Data de Digitação' (F1\_DTDIGIT) considerará a data da digitação, sendo atualizado posteriormente com a data da classificação.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
