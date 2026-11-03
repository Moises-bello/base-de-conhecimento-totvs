---
content_hash: 2416ca6e2b8161780fe8a897c2a967232d24e55d3af49657be959469ca93356d
fetched_at: '2026-06-29T00:11:45.646660+00:00'
page_id: '820561731'
product: rm
source: tdn-rm
title: 5- Agendamento do Job Ajuste de Transação - Responsável por baixar os lançamentos.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=820561731
version: 4
---

O Processo de Ajuste de Transações é responsável pela baixa dos lançamentos.

**Após realizar os testes de pagamento de um lançamento no Portal do Aluno, APP Meu eduCONNECT ou Processo Seletivo, o processo agendado Ajuste de Transações é responsável pela baixa dos lançamentos.**

**Contas a Pagar / Receber | Mais | Ajuste de Transação**

No parâmetro Executar em, informa o horário para a primeira execução e no parâmetro Diariamente. à cada intervalo, informe 00:01, assim o job será executado a cada 1 minutos para validar se houveram pagamentos via PIX.

Para validar se o Job foi devidamente agendado, acesse:

**Ambiente | Gerenciamento de Jobs**

Crie um novo filtro buscando os parâmetros:

Tipo de Recorrência IS NOT NULL

Finalizado em IS NULL

Status IS NULL

Salve e Execute o filtro, o agendamento de Job Ajuste de Transações do TOTVS Pagamento Instantâneo precisa ser listado ser listado

[Instruções para Agendamento de Jobs](https://tdn.totvs.com/pages/viewpage.action?pageId=702382056)

Para validação das Transações e confirmação da baixa dos lançamentos. acesse o Menu de transações e crie um filtro buscando o Meio de Pagamento PIX.

O registro da transação criado, na coluna status é possível validar a situação da transação, que precisa estar como Pagamento Concluído e em anexo ‘histórico de transações, temos os dados informando que o sistema foi acessado e que o link para o pagamento foi gerado com sucesso até a baixa do lançamento.

Após o Ajuste de transações os lançamentos no Portal do Aluno e Portal de inscrições foram baixados, 

Extrato Financeiro, no Portal do Aluno

Central de candidato - Portal de Inscrições - Processo Seletivo

APP Meu EduCONNECT

Processo de Ajuste de transação precisa ser agendado para execução automatica, somente o processo realiza a baixa dos lançamentos.
