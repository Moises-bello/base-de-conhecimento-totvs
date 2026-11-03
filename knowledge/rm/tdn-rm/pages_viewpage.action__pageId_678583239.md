---
content_hash: 3aca2e533561a92992324c603cc4d42bcd49f52a9fe8cd393f8655483a0fcf01
fetched_at: '2026-06-29T00:11:17.264593+00:00'
page_id: '678583239'
product: rm
source: tdn-rm
title: PIX - Fluxo e Status de Transações
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=678583239
version: 8
---

**VISÃO GERAL**

Após o pagamento do QR Code, este fluxo auxilia na conferência das transações no RM TOTVS

**1-  Exibição da transação**

A partir do momento em que a geração do QR Code é realizada em um dos canais (Portal do Aluno, Sessão de Caixa, Processo Seletivo ou Meu eduCONNECT), é criada a transação no menu de Contas a Pagar/Receber:  
  
***Backoffice > Gestão Financeira > Contas a Pagar/Receber > Transações***

Nesta tela, são exibidas todas as transações e status de cada uma delas:

**Pagamento Solicitado** - QR Code gerado e ainda em prazo para pagamento

**Pagamento Confirmado** -  Pagamento realizado e confirmado pelo Banco e pendente ajuste de transação

**Pagamento Concluído** - Pagamento baixado

**Pagamento Expirado** - Transação com prazo de QR Code expirado

**Pagamento Cancelado** -  Transação cancelada

**2 - Baixa do título**

Após a confirmação do pagamento, para que ocorra a baixa do título, é necessário rodar o processo de ajuste de transação.

***Contas a Pagar/Receber > Mais > Ajuste de Transação***

Este processo pode ser realizado por meio de um *job* para a execução da rotina. Os intervalos serão conforme ambiente de cada cliente.

Nesta mesma tela em ***Anexo > Histórico de Transações ou Boleto***, é possível conferir mais detalhes da transação:

**3 - Extrato de Caixa**

Após a baixa, as transações geram o extrato de caixa.

Esta consulta é realizada pelo identificador da transação, que consta na coluna **TID** no menu de ***Contas a Pagar/Receber > Transações.***

Acesse ***Movimentações Bancárias > Extrato de Caixa*** e consulte pelo filtro ***ID da Transação.***

Na tela seguinte, é exibido o valor bruto recebido. Este valor fica pendente na conta transitória criada e indica também a taxa que será deduzida no repasse.

JANELAS DE REPASSES

As transferências entre o Banco Original e a conta caixa/banco de recebimento são realizadas diariamente nos horários:  
06:45 - 14:45 - 19:45 - 23:45

O limite diurno é de 5 milhões e noturno de 11 mil.

**4 - Conciliação Automática**

Os arquivos de conciliação estarão disponíveis no dia posterior (segunda a sexta) a partir das 07:00h

Confira orientações para executar o processo:

Este processo pode ser programado por meio de um *job* para a execução da rotina.

Após este processo, no extrato de caixa são exibidas as partidas de saque transferência, retirando da conta transitória, e de depósito transferência para a conta do Banco de destino, confirmando a compensação.
