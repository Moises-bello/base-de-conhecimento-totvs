---
content_hash: 07d8b8ef998124d57aa452241099eb1733aade300b8784e76b1d2a675b476ca9
fetched_at: '2026-06-29T00:09:47.094160+00:00'
page_id: '435104919'
product: rm
source: tdn-rm
title: Encerrar/Rescindir - Processo - Efetivar
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435104919
version: 7
---

Ao efetivar um Encerramento/Rescisão, o contrato será encerrado ou rescindido conforme parametrizado pelo usuário.

* **Passo 1 -** Selecione o registro de Encerramento/Rescisão desejado;
* **Passo 2 -**No processos acione a opção "Efetivar";
* **Passo 3** - O Contrato de Locação será encerrado ou rescindido.
* **Passo 4** - Quando a "Ação divergência vencimento" da regra de vencimento do contrato de locação for do tipo "Fraciona / Acumula", a rescisão do contrato de locação irá excluir todas as parcelas "Em aberto" posteriores a data de rescisão do contrato e irá recriar a parcela correspondente a competência da data de rescisão com o valor proporcional a data de rescisão.
* **Passo 5** - A data de prorrogação do contrato será alterada para a data de encerramento.

Observações

* Após a efetivação do encerramento/rescisão do contrato, será gerada uma parcela referente ao mês do encerramento, calculada de forma proporcional à quantidade de dias em que o contrato permaneceu vigente.
* Os lançamentos de aluguel com status remetido / baixado não serão excluídos pelo processo. O sistema irá alertar o usuário sobre esses lançamentos.
* Restrição para quando se usa o módulo de condomínio: Para os imóveis associados à Subunidades, não será permitido encerrar o contrato de locação, caso haja fechamento de calculado ou integrado ao financeiro, para períodos iguais ou posteriores ao mês definido para o encerramento do contrato
