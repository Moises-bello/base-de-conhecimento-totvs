---
content_hash: 342e70c92aa705c6a1eca2ed9fe1d3563e0bf403e7c3b9764042ae43ec387dac
fetched_at: '2026-06-29T00:09:16.960351+00:00'
page_id: '421388541'
product: rm
source: tdn-rm
title: Alteração Global de Extrato de Caixa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388541
version: 3
---

Através do processo de alteração global é possível atualizar a informação de alguns campos em mais de um registro ao mesmo tempo. Marque os registros e clique sobre a opção "Alteração Global" no menu "Processos". No Assistente de Atualização de Múltiplos Registros selecione o campo a ser atualizado, informe a nova informação e conclua a operação.

**Observações**

Registros Cancelados não podem ser alterados.

A alteração do campo "tipo de custódia" não estará disponível. Os campos de custódia poderão ser alterados desde que seja respeitado o "tipo de custódia" previamente selecionado para o registro.

A alteração global do campo "Data de Vencimento" (pasta Dados do Cheque) verifica o parâmetro "Datas do cheque em Finais de Semana e Feriados" (Assistente de Implantação de Processos | processo Baixa | etapa Recebimento/Pagamento em Cheque). Com a opção "Manter Mesmo Dia" marcada, a data poderá ser alterada para um dia que seja final de semana ou feriado. Com uma das opções "Primeiro dia útil posterior" ou "Primeiro dia útil anterior" marcada, a data não poderá ser alterada para um dia que seja final de semana ou feriado.

Para alterar a informação de "Tipo Contábil" para "Contábil" é necessário que o registro de Extrato de Caixa esteja preenchido com um registro de uma tabela default de Evento Contábil e que a contabilização seja preenchida corretamente, caso contrário, a alteração não será permitida.
