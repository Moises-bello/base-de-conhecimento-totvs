---
article_id: 360006903391
category: Contabilidade Gerencial - Rateio
content_hash: 0c40977770073fbf4266df6b24bb753430354ce089627e4d8bf54bfc9204b7c4
fetched_at: '2026-06-28T22:40:35.530748+00:00'
product: protheus
section_id: 1500001548962
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGACTB- CTBA100 - Rateio Online
type: support-article
updated_at: '2023-11-16T11:37:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006903391-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA100-Rateio-Online
---

**Dúvida**

Como funciona a rotina de Rateio Online?

**Ambiente**Cross Segmento - Backoffice Linha Protheus – Contabilidade Gerencial – 12.1.17

**Solução**

Esta opção permite cadastrar regras de rateios que serão normalmente executados ao final de um período, e pode ser utilizada no processo de apuração de custos, em conjunto com o ambiente de Estoque e Custos, para apurar os custos de produção/produtos.

Através dessa opção, é possível ratear valores por saldo ou  por movimento mensal.

O sistema também possibilita armazenar o histórico dos rateios processados, ficando a consulta disponível através da opção "Histórico", que armazena detalhes do rateio. Esta opção será apresentada somente se o parâmetro MV\_CTBHRAT estiver configurado como T (True).

Outro tratamento possível no rateio off-line é o cálculo automático do percentual de rateio baseado em quantidades, através dos campos "Unidade" (CTQ\_UM) e "Valor" (CTQ\_VALOR). Ao informar o valor e a quantidade, os percentuais de rateio serão atualizados automaticamente, tomando como base o valor informado na linha em que está posicionado o cursor, contra a somatória de todas as linhas, para atingir 100%.

Documentação Completa:

[Rateio On-line (CTBA100)](https://tdn.totvs.com/pages/releaseview.action?pageId=694111158)

[Rateio off-line (CTBA270)](http://interno.totvs.com/mktfiles/tdiportais/helponlineprotheus/p12/portuguese/ctba270.htm)
