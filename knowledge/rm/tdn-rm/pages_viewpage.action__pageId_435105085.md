---
content_hash: 163cba056eef3b1bfe1322ed92351c2b8eae8d23b9f8f21bdbfc914727c9b571
fetched_at: '2026-06-29T00:09:47.844446+00:00'
page_id: '435105085'
product: rm
source: tdn-rm
title: Funções de Fórmula Reajuste em Memória para Relatórios
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105085
version: 2
---

**Funções de Fórmula Reajuste em Memória para Relatórios**  
 Implementado no sistema Totvs Incorporação algumas Funções de Fórmula para serem utilizadas nos Relatórios. Estas funções de fórmula tem por objetivo gerar relatórios com valores dos planos de financiamento atualizados até a data informada, simulando um reajuste de parcelas como é realizado no sistema.

* **GETVALORPARCELASALDODEVEDOR:** Valor do saldo devedor da parcela atualizado, já descontando valores pagos (baixa parcial) e considerando o saldo devedor da Correção monetária e dos Juros de Contrato. Sem considerar multa de atraso e juros de mora que ainda não foram incorporados ao plano. Essa função funciona no contexto das parcelas (XPARCELAPAGAMENTO), devem ser informados como parâmetro todos os campos que compõe a chave da parcela além da data para cálculo
* **GETMULTAATRASOPARCELA:** Valor total da multa de atraso calculada pelo financeiro para a parcela, baseado no valor atualizado (VALORPARCELASALDODEVEDOR) até a data informada no parâmetro da formula. Essa função funciona no contexto das parcelas (XPARCELAPAGAMENTO), devem ser informados como parâmetro todos os campos que compõe a chave da parcela além da data para cálculo
* **GETJUROSMORAPARCELA:** Valor total dos juros de mora calculado pelo financeiro para a parcela, baseado no valor atualizado (VALORPARCELASALDODEVEDOR) até a data informada no parâmetro da formula. Essa função funciona no contexto das parcelas (XPARCELAPAGAMENTO), devem ser informados como parâmetro todos os campos que compõe a chave da parcela além da data para cálculo
* **GETVALORVENDA:** Valor total da venda atualizado sem considerar multa de atraso e juros de mora que ainda não foram incorporados ao plano até a data informada no parâmetro da fórmula. Essa função funciona no contexto da venda (XVENDA), devem ser informados como parâmetro todos os campos que compõe a chave da venda além da data para cálculo (data corrente)
* **GETVALORVENDASALDODEVEDOR:** Valor saldo devedor da parcela atualizado sem considerar multa de atraso e juros de mora que ainda não foram incorporados ao plano e considerando as baixas parciais. Essa função funciona no contexto da venda (XVENDA), devem ser informados como parâmetro todos os campos que compõe a chave da venda além da data para cálculo
* **GETCORRECAOMONETARIAPARCELA:** Valor total do componente correção monetária da parcela atualizado até a data de pagamento. Essa função funciona no contexto das parcelas (XPARCELAPAGAMENTO), devem ser informados como parâmetro todos os campos que compõe a chave da parcela além da data para cálculo
* **GETJUROSCONTRATOPARCELA:** Valor total do componente de juros de contrato da parcela atualizado até a data de paramento. Essa função funciona no contexto das parcelas (XPARCELAPAGAMENTO), devem ser informados como parâmetro todos os campos que compõe a chave da parcela além da data para cálculo
* **GETCORRECAOMONETARIAPARCELASALDODEVEDOR:** Valor saldo devedor do componente correção monetária da parcela atualizado. Essa função funciona no contexto das parcelas (XPARCELAPAGAMENTO), devem ser informados como parâmetro todos os campos que compõe a chave da parcela além da data para cálculo
* **GETJUROSCONTRATOPARCELASALDODEVEDOR:** Valor saldo devedor do componente de juros de contrato da parcela atualizado. Essa função funciona no contexto das parcelas (XPARCELAPAGAMENTO), devem ser informados como parâmetro todos os campos que compõe a chave da parcela além da data para cálculo
