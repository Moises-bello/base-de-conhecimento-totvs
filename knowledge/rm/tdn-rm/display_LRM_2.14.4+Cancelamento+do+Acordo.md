---
content_hash: ce85aff1b601ae23c6c92324a247add5f30959bcdf37a493b89941b3dc260481
fetched_at: '2026-06-29T00:10:58.826051+00:00'
page_id: '607324014'
product: rm
source: tdn-rm
title: 2.14.4 Cancelamento do Acordo
type: documentation
url: https://tdn.totvs.com/display/LRM/2.14.4+Cancelamento+do+Acordo
version: 2
---

Para cancelar um Acordo selecione o registro que deseja realizar o processo. Será possível realizar o cancelamento de duas formas:

* **Varredura de Lançamentos:** Será utilizada quando a primeira parcela do Acordo já estiver vencida em um número de dias maior que o prazo definido na execução, sendo assim o sistema varrerá os Lançamentos Financeiros identificando o Acordo e cancelando o mesmo.
* **Cancelamento pela visão de Acordo:** Será utilizado para um ou mais registros independentes se vencidos ou não. Em ambos os casos a regra para cancelamento será a mesma: Lançamentos gerados pelo Acordo não podem estar baixados nem cancelados. O cancelamento do Acordo irá disparar um processo para que o Módulo que fez o Acordo faça validações e também execute as regras de cancelamento em suas entidades (caso exista alguma). O cancelamento somente será possível se todos os Lançamentos gerados por Acordo atenderem a condição de cancelamento, do contrário o sistema não permitirá a conclusão do processo. Para Lançamento gerado via acordo com boleto atrelado é necessário cancelar o Acordo para que o (s) Lançamento (s) e Boleto (s) também seja cancelado (s).

Informar o motivo ao cancelar o acordo;

Acordo (lançamentos gerados pelo acordo) cancelados;

 Informações Complementares
