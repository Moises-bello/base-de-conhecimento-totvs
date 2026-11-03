---
content_hash: dbd0be489a1d787ebfc8d3a5ed27ec6934853d8c20b8512bd863f9ee0e885490
fetched_at: '2026-06-29T00:11:33.403097+00:00'
page_id: '759926535'
product: rm
source: tdn-rm
title: 10 - Processo Importar Dados e Sincronizar Transações - Responsável por baixar
  lançamentos a partir da versão 12.1.2302
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=759926535
version: 11
---

A partir da versão 12.1.2302 o processo de ajuste de transação, foi substituído pelos processos: importar dados e sincronizar transações, que serão responsáveis pela baixa dos lançamentos financeiros

**Após realizar os testes de pagamento de um lançamento pelo Portal do Aluno ou pelo Processo Seletivo, é necessário executar os processos de Importar dados e Sincronismo de Transações.**

Geração do QRCode no Portal do Aluno

A transação é criada com o status de **Pagamento Solicitado**. Após o pagamento, o status é alterado para **Pagamento Concluído** pelos processos de Importar Dados e Sincronizar Transações:

Para execução dos processos, acessar:

**Contas a Pagar/Receber | Sincronismo de Transações | Importar dados**

Log gerado após a execução do Processo

O log informa que nenhuma transação já importada anteriormente sofreu atualizações e que um novo registro foi incluído após a execução do processo.

A importação é a primeira parte do processo, para a baixa dos lançamentos financeiros é necessário executar o processo de **Sincronizar Transações**

Acessar:

**Contas a Pagar/Receber | Sincronismo de Transações | Sincronizar Transações**

Após clicar em executar, o processo será executado em segundo plano.

O Sincronismo realizará a baixa do lançamento financeiro e a alteração do status da transação.

O lançamento será exibido no menu financeiro do Portal do Aluno.

**Após a atualização para a versão 12.1.2302, é possível que já exista um job agendado para o processo de Ajuste de Transações, neste caso, será necessária a exclusão deste job.**

**A baixa automática dos lançamentos dependerá do agendamento dos novos jobs: Importar Dados e Sincronizar Transações.**

**Recomendamos o agendamento com execução diária em intervalos de 1 minuto.**
