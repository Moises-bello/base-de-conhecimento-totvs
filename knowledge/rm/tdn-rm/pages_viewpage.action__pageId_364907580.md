---
content_hash: b8bf7f77707006bd2c0496a23f6f59ab6ed90e776589221a7acd42890d61bf60
fetched_at: '2026-06-29T00:08:59.576188+00:00'
page_id: '364907580'
product: rm
source: tdn-rm
title: Qual a diferença entre os eventos S-1200 e S-1210?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=364907580
version: 5
---

Para entendimento dos eventos S-1200 e S-1210  veja resumo de suas funcionalidades .

**S-1200**– **Remuneração de trabalhador vinculado ao Regime Geral de Previdência Social**

São as informações da remuneração de cada trabalhador conforme mês de apuração (Competência).

O sistema irá buscar os valores lançados do envelope de pagamento (ficha financeira/PFFINANC) conforme incidência dos eventos.

Para assistência de saúde dos dependentes, irá buscar os valores do histórico de assistência saúde do dependente.

**S-1210 – Pagamentos de Rendimentos do Trabalho**

São as informações prestadas relativas aos pagamentos dos rendimentos do trabalho (Imposto sobre a Renda Retido na Fonte – IRRF) verificando data de pagamento do evento e mês de apuração (Caixa).

O sistema irá buscar os valores lançados no envelope de pagamento (ficha financeira/PFFINANC), recibo de férias e autônomos do Fluxus (será calculado através do total do lançamento financeiro menos o total de INSS e IRRF).

Obs.: A data do pagamento será definida de acordo com a data que possuir maior reincidência no envelope de pagamento.

**Atenção:** S-1200 e S-1210: Quando a empresa utiliza tomador de serviço, serão considerados os valores da distribuição do SEFIP (PFMOVTOMADOR)

Maior detalhamento consulte : [Diferença Eventos S1200\_S1210](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004020232?flash_digest=8438112fe261d70dec1603737cc22f1168a5c446)
