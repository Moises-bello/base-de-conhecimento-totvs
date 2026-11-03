---
content_hash: a3257919164671eb48435465cea47696405aa4188190601077031fd27e2365b7
fetched_at: '2026-06-29T00:09:48.348031+00:00'
page_id: '435105129'
product: rm
source: tdn-rm
title: Parcela de Despesa - Processo - Gerar Movimento de Despesa
type: documentation
url: https://tdn.totvs.com/display/LRM/Parcela+de+Despesa+-+Processo+-+Gerar+Movimento+de+Despesa
version: 7
---

Esse processo é o responsável por gerar os movimentos das parcelas de despesas.

**Pré-requisitos:**

* Tipo de Despesas cadastrada;
* Parâmetro de Movimento cadastrado;
* Despesa cadastrada com status "Em Preparação"
* Parcela de Despesa criada;

**Como executar:**

Acesse a visão de Despesas através do caminho: TOTVS Incorporação >> Outros >> Despesa;

* O processo pode ser executado de 2 formas, são elas:

* + **Através da visão da despesa ou da edição da despesa:** Ao executar dessa forma, será exibida uma tela onde será possível informar qual o período desejado para que os movimentos sejam gerados. Caso não seja informado um período, será gerado os movimentos de todas as parcelas de despesa vinculadas as despesas selecionadas;
  + **Através da visão da parcela de reembolso ou da edição da parcela reembolso:** Ao executar dessa forma, será gerado os movimentos de todas as parcelas de reembolso selecionadas;

**Observações:**

* Os movimentos serão gerados de acordo com a configuração do parâmetro de movimento vinculado a despesa a ser processada;
* Para que os lançamentos gerados pelos movimentos possuam as datas de vencimento definidas na despesa, é necessário realizar a parametrização abaixo no tipo de movimento.

1) Acesse a parametrização do tipo de movimento desejado e em **Mov - Datas 1/2>Data Entrega>Edição da Data de Entrega**, informar o valor "Edita".

2) Em **Fin - Faturamento 2/6>Vencimento a Partir**, informe o valor "Data de Entrega". O TOTVS Incorporação utilizará este campo para enviar a data de vencimento da parcela  de despesa para o TOTVS Gestão de Estoque, Compras e Faturamento, que por sua vez gerará o lançamento no TOTVS Gestão Financeira  com esta data de vencimento.

* O sistema não permite gerar movimento para parcela de despesa que já possua movimento gerado;
* A despesa pode ser gerada para subunidades que estejam associadas também à uma venda em qualquer situação (Em preparação, efetivada, quitada, distratada ou bloqueada).

Veja Também

---
