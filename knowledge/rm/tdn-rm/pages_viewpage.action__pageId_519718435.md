---
content_hash: 8144ad3cc35358d5ac511aaa23f079c0914a395bc27f203e0fc607af016409cd
fetched_at: '2026-06-29T00:10:30.310961+00:00'
page_id: '519718435'
product: rm
source: tdn-rm
title: Cobrança recorrente com cartão de crédito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=519718435
version: 12
---

A cobrança recorrente oferece recursos de recebimento com cartão de forma automática. A adesão ao pagamento recorrente poderá ser feita ao realizar um pagamento.

De forma periódica um processo é executado para selecionar os pagamentos de acordo com a regra de seleção parametrizada. Para cada solução há uma regra de seleção dos pagamentos a serem realizados de forma recorrente. Esse processo deve ser agendado para ser executado na periodicidade e horário conforme necessidade.

Se optar por não baixar o lançamento ao fazer o pagamento pode ser marcado no agendamento do processo a opção "*Baixar posteriormente*". Nesse caso deve ser agendado o processo de *Ajuste de transações*para que sejam realizadas as baixas dos títulos referentes as transações confirmadas.

Atenção

A recorrência processa somente os lançamentos do aluno. Lançamentos de bolsa de crédito não são baixados nesse processo.

**Parâmetros**

Os parâmetros financeiros para configuração da cobrança recorrente podem ser  acessados em ***"******Ambiente >> TOTVS Gestão Financeira >> Contas a Receber >> Baixas >> Cobrança Recorrente"***.

* Número máximo de tentativas no caso de pagamento não autorizado: default 3, mínimo 1 e máximo 3.

**Execução e agendamento**

O processo está disponível pelo menu "***Movimentações Bancárias >> Cartão de Crédito/Débito >> Mais >> Cobrança recorrente com cartão de crédito******"***, com opção de agendamento em ambientes três camadas.

**Controle de concorrência**

Quando existe mais de um agendamento em horários muito próximos, existe a possibilidade de processamento de um mesmo registro de boleto, o que poderia ocasionar em cobrança duplicada. Para impedir tal situação, foi criado o controle de concorrência. Quando um registro começa a execução é bloqueado para que outro processo não execute o mesmo, ao final é desbloqueado. Caso ocorra alguma interrupção do processamento, e o registro não ser desbloqueado, é possível liberar o mesmo através da opção disponível em "***Utilitários >> Ajustes na Base >> Corrigir Boletos Bloqueados por Concorrência******".***

**Observações:**

É possível consultar a execução dos processos "Cobrança recorrente com cartão de crédito" e "Conciliação das transações com cartão" através do monitor de jobs e no "Dashboard Financeiro de recebíveis" verificar a data de última execução com sucesso de tais processos: [Gestão de Recebíveis e Conciliação](https://tdn.totvs.com.br/pages/viewpage.action?pageId=540881707) / [DT Dashboard Financeiro - Visão Geral](https://tdn.totvs.com/display/LRM/DT+Dashboard+Financeiro+-+Visao+Geral).

**Importante:**Esse processo funciona somente para o modelo de pagamento CyberSource.
