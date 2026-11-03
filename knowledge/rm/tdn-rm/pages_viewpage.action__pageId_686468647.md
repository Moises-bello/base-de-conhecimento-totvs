---
content_hash: e8b65ae7f2cd76dc3bb6dc39d54475a165d4db52e2c493caea166d4e6a295f2e
fetched_at: '2026-06-29T00:11:20.521205+00:00'
page_id: '686468647'
product: rm
source: tdn-rm
title: 7- Processo de Conciliação e validação do Extrato de Caixa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=686468647
version: 10
---

O processo de conciliação, é responsável por gerar o extrato de caixa demonstrando a movimentação entre o saque do valor da conta transitória e o valor transferido por repasse para a conta banco definida. O arquivo de conciliação é disponibilizado de segunda a sexta a partir das 7:00 horas.

[Instruções para Agendamento do Job](https://tdn.totvs.com/pages/viewpage.action?pageId=702382056)

Para execução do processo acessar:

**Movimentações Bancárias | Conciliação**

Após criar um filtro para exibir todos os registros referentes ao TOTVS Pagamento Digital, acessar Processos | Importação do Arquivo de Conciliação

Marcar o parâmetro TOTVS Pagamento Instantâneo, Importar e conciliar automaticamente  e TOTVS WebService

A data de Liquidação se refere a data do repasse, precisa ser informada somente quando existir a necessidade de realizar a conciliação de uma data específica. Do contrário, deixar conforme especificado acima, sem nenhuma data e seleção.

Após a execução do processo o extrato de caixa será criado, caso a instituição trabalhe com evento contábil para o extrato de caixa os valores serão respeitados conforme construção do evento.

Os repasses da conta transitória para a conta banco de destino ocorrem diariamente de hora e hora.

O Repasse ocorre com o valor líquido já com desconto da taxa.

No extrato é possível visualizar os registros com a seguinte estrutura:

* Uma linha com a operação depósito na baixa com o valor bruto da transação
* Uma linha com saque manual, referente ao valor de desconto da taxa
* Uma linha com o saque transferência onde é demonstrado o valor que saiu da conta transitória
* Uma linha com depósito transferência referente ao valor repassado para a conta banco do cliente.
