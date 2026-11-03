---
content_hash: 2bd79cc88d38b0b60a086440bed63a29282e0eaa992825cf2ab46b19aebe63c8
fetched_at: '2026-06-29T00:11:56.602721+00:00'
page_id: '867162623'
product: rm
source: tdn-rm
title: Sincronizar PIX Bradesco
type: documentation
url: https://tdn.totvs.com/display/LRM/Sincronizar+PIX+Bradesco
version: 1
---

Processo disponível apenas para cliente específico. Outros clientes devem utilizar a solução [TOTVS Pagamento Instantâneo/Digital](https://tdn.totvs.com/pages/viewpage.action?pageId=577622236).

**Objetivo**

Efetuar a baixa dos boletos que tiveram o pagamento efetuado via PIX do banco Bradesco e que o banco notificou via Webhook.

**Configuração**

Necessário definir a segurança do fracionamento de Jobs, pois esse processo permite rodar múltiplos jobs em paralelo. Menu Ambiente | Segurança de Jobs Fracionáveis e incluir a classe de Job "FinBaixaPixBradescoProcess"

**Parâmetro do Processo**

É necessário informar um meio de pagamento PIX e se deseja contabilizar posteriormente

**Agendamento**

É possível definir em quantos jobs o processo será dividido e a recorrência para o agendamento

**Regras**

A baixa será efetuada apenas para os boletos que estão em aberto. Caso boleto não seja encontrado ou não esteja em aberto, será apresentado mensagem de erro e na próxima execução do processo, a transação que ocorreu o erro não irá mais ser executada.
