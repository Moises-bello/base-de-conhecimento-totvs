---
article_id: 360031283914
category: Escrita Fiscal - Impostos - ISS
content_hash: c026b1d2a1ebca09f6e30d6fe6e15583f922781176daac7a9771a73236a7dfe7
fetched_at: '2026-06-28T22:39:35.211915+00:00'
product: protheus
section_id: 1500001549762
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Conceito do campo
  F1_RECISS habilitando o parâmetro MV_VISDIRF = 1
type: support-article
updated_at: '2021-06-15T13:28:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360031283914-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Conceito-do-campo-F1-RECISS-habilitando-o-par%C3%A2metro-MV-VISDIRF-1
---

**Dúvida**

Como utilizar o campo F1\_RECISS na nota fiscal de entrada com ISS?

**Ambiente**

Protheus – Compras – A partir da versão 11.80.  
  
**Solução**

O campo F1\_RECISS destaca uma condição de atalho para os casos em que o tomador do serviço pode ser ou não, o responsável pelo recolhimento do ISS, exemplo:

10 notas tomadas do Fornecedor XPTO, sendo:

7 notas o Tomador do serviço é o responsável pelo recolhimento do ISS;

3 notas o prestador/fornecedor é o responsável pelo ISS;

Cliente utiliza na tabela SA2 de forma fixa o campo A2\_RECISS = não (fornecedor não responsável pelo recolhimento).

Para as setes notas, não utilizar o campo F1\_RECISS ou mante-lo = NÃO;

Para as três notas, utilizar o campo F1\_RECISS = SIM (desta forma, o sistema vai priorizar a condição do campo F1\_RECISS = SIM).

Condição do campo:

F1\_RECISS:

1 - S, indica que o ISS será retido pelo prestador do serviço que possuirá a responsabilidade do pagamento.

2 - N, indica que o ISS será retido para o tomador do serviço que possuirá a responsabilidade do pagamento.
