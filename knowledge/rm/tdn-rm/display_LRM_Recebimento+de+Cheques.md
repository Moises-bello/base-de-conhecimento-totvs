---
content_hash: 70e4eefd1b39788b34fb1f40d397e98320c7f213b62eb3d57bc73be92703cc89
fetched_at: '2026-06-29T00:10:30.512816+00:00'
page_id: '520102412'
product: rm
source: tdn-rm
title: Recebimento de Cheques
type: documentation
url: https://tdn.totvs.com/display/LRM/Recebimento+de+Cheques
version: 4
---

**Devolução de Cheque**

A devolução do cheque será processada através da Visão de Lançamento, em seu anexo | Baixas do Lançamento no menu de processos | Devolver Cheque Recebido.  
Ao executar a operação devolver cheque será necessário informar a data e o motivo de devolução. O sistema inclui o registro na tabela de processos de cheques e no Histórico de cheques devolvidos com status Devolvido.

**Reapresentação**

Após devolvido o cheque poderá ser reapresentado pelo Anexo da Visão de Lançamentos | Cheques Devolvidos em Processos | Reapresentar Cheque. Ao executar o processo o sistema inclui novo registro de reapresentação na tabela de processos do cheque e no Histórico de cheques recebidos com o respectivo status.

**Devolver Cheque pela segunda vez**

Após reapresentado o cheque poderá ser devolvido pela segunda vez pelo Anexo da Visão de Lançamentos | Cheques Devolvidos em Processos | Devolver Cheque pela Segunda Vez. Ao executar este processo será necessário informar a data e motivo da devolução do cheque.   
O sistema inclui novo registro de devolução pela segunda vez na tabela de processos do cheque e no histórico de cheques recebidos com o respectivo status.   
Caso ocorra erro operacional, os processos de Devolução, Reapresentação e Segunda Devolução do Cheque poderão ser cancelados.

**Finalizar Cheque**

O processo de “Finalizar Cheque" tem como objetivo concluir o processo devolução de cheques recebidos onde deverá ser executado quando não houver mais motivos para ser representado de acordo com o Cadastro de Motivos de Devolução em anexos da Visão de Lançamentos, menu Histórico de Devolução de Cheques Recebidos |Processos.

**Observações:**

* Ao finalizar o cheque, a baixa do lançamento é automaticamente cancelada.
* Após finalizar o cheque, todas as operações executadas ficarão registradas no histórico de devolução.
* Os cheques finalizados não poderão mais ser devolvidos ou reapresentados.
* O cheque poderá ser finalizado também durante a execução dos processos de Devolução do Cheque e na Segunda Devolução.

**Cancelamento do Cheque**

Se o cheque foi gerado no processo de Recebimento via Cheque o cancelamento do cheque recebido será manual.  
O processo de “Cancelamento de Cheque” está disponível na Visão de Lançamentos através do anexo “Baixas do lançamento” menu Processos.   
Caso a Baixa tenha sido com meio de pagamento “Cheque”, o sistema cancela automaticamente a emissão do cheque.

**Cancelamento do Lançamento**

O lançamento só poderá ser cancelado/excluído se o cheque emitido estiver cancelado.

**Observações:**

* A tabela de Motivos de Devolução foi cadastrada na base de dados com os principais motivos de devolução de cheques relatados pelo Banco Central e poderá ser alterada, se necessário.
* Os processos executados na devolução e reapresentação não geram contabilização. Somente a baixa do lançamento é contabilizada.
