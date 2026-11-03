---
content_hash: a4ebb96ab65b47823670a9ca67a10f941dca3fd1d887959260da3abcc3c85d62
fetched_at: '2026-06-29T00:09:18.699250+00:00'
page_id: '421388755'
product: rm
source: tdn-rm
title: Reajuste utilizando a Baixa do Totvs Gestão Financeira
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388755
version: 4
---

No momento da baixa, deverá escolher a data em que será feito o reajuste da parcela: Data da Baixa (data da baixa do lançamento financeiro) ou Vencimento da Parcela (data de vencimento do lançamento financeiro).   
Será criada uma aba "Saldo dos Valores de Integração" na baixa manual, onde serão exibidos os saldos dos valores caso exista valores de integração para o lançamento.

No Wizard de Baixa Implementado novo parâmetro: "Reajustar até (Lançamentos do SGI)Data da Baixa e Vencimento da Parcela".

A baixa exibirá o valor a ser baixado já considerando o reajuste até a data parametrizada, mas somente gravará os valores atualizados se a baixa for confirmada.

O reajuste será executado apenas na parcela a ser baixada conforme parametrização realizado no plano de financiamento.

No caso do cancelamento de baixa é chamado o reajuste do Totvs Imobiliário, onde será verificado a última data de reajuste do grupo, assim esta parcela será reajustada igual as demais parcelas do seu grupo de financiamento. Estes dados poderão ser visualizados na tela de edição de lançamento. O serviço de reajuste do TIN irá atualizar os valores de integração reajustado do lançamento na tabela FLANINTEGRACAO.

Os reajustes dos valores de integração podem ser visualizados na tela de baixa manual na aba : Saldo dos Valores de Integração.

Bloqueios

* Não será permitido realizar Baixa de Lançamento Financeiro com data de baixa inferior a última Baixa realizada.
* Não será permitido cancelar uma Baixa de Lançamento oriundo do TIN que não seja a última realizada.
* Não será permitido incluir novo valor de integração no Lançamento Financeiro que esteja quitado totalmente.

Será permitido incluir novo Valor de Integração no Lançamento Financeiro que não esteja quitado totalmente, o valor de integração será atualizado na tabela FHISTVALORESINTEGRACAO  atualizando o valor líquido para Lançamentos parcialmente baixados. O sistema irá incluir este novo Valor de Integração caso a sua ação seja diferente de nada.
