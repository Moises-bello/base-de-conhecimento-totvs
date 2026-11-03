---
article_id: 360041234634
category: Escrita Fiscal - Impostos - IR
content_hash: bc9ef8d002a574bd12edc95cfbf57e5e6aae0e8786572ab49dddcd0bb7c4dac7
fetched_at: '2026-06-28T22:39:31.911452+00:00'
product: protheus
section_id: 1500001549802
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como destacar o código
  de retenção do IRRF de forma automática
type: support-article
updated_at: '2023-12-14T19:07:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041234634-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-destacar-o-c%C3%B3digo-de-reten%C3%A7%C3%A3o-do-IRRF-de-forma-autom%C3%A1tica
---

**Dúvida**Gerar o código de retenção nas notas de entradas do IR de forma automática (1708) via documento de entrada.

**Ambiente**Protheus – Compras – A partir da versão 12.1.17

**Solução**

**MV\_VISDIRF**

Habilita a informação se os impostos farão parte da DIRF e a digitação do código da Retenção do IR na entrada.

1=Habilita;

2=Não habilita (Default).

**MV\_AUTOISS**

Preencher automaticamente os dados de cobrança do ISS e DIRF em notas fiscais de entrada. Informar:

{"Fornecedor","Loja","Gera DIRF","Cod. Retenção"} .

**Importante:** As duas primeiras posições são do ISS, a terceira e quarta tem relação com o IR, exemplo:

{"Fornecedor","Loja","SIM","1708"}

Esse procedimento é somente para o IR 1708, para os demais impostos será necessário utilizar o ponto de entrada abaixo:

<https://tdn.totvs.com/pages/releaseview.action?pageId=200908697>

Caso tenha dificuldades em relação ao ponto de entrada, favor abrir um chamado com a equipe de ADVPL.
