---
content_hash: f6b02597fb96c408102fd484e09e24167fe9629a628f7032c98392d1d9ce0110
fetched_at: '2026-06-29T00:11:22.412475+00:00'
page_id: '702382056'
product: rm
source: tdn-rm
title: 8 - Parametrização de Jobs - Ajuste de Transações do TOTVS Pagamento Digital
  e Importação do Arquivo de Conciliação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=702382056
version: 14
---

O Job de ajuste de transações é responsável pelas baixa dos lançamentos e criação dos extratos de caixa.

**Para a baixa automática dos lançamentos e a criação do extrato de caixa é necessário o agendamento do processo.**

Acessar: 

**O modulo Gestão Financeira**

**Contas a Pagar / Receber | Mais | Ajuste de Transação**

Job precisa ser agendando para execução diariamente com intervalos de 1 a 5 minutos

Na opção ***Hora da execução,*** informar a data e hora para a primeira execução.

Na opção ***Repetir a execução*** informar que a execução será repetida diariamente a cada 1 minuto.

**Após execução, o processo será agendado.**

Acessar:

**Ambiente | Gerenciamento de Jobs**

Criar um filtro para listar os jobs agendados

**Agendamento do Job de conciliação**

Acessar:

**Contas a Pagar / Receber | Movimentações Bancárias | Conciliação**

Criar um filtro para listar todas as conciliações do Pix selecionado Cód. Operadora = TOTVS Pagamento Instantâneo, Adicionar e Salvar.

Após a criação do filtro clicar em processos → Importação do Arquivo de Conciliação  
  
  
  
Marcar as opções TOTVS Pagamento Instantaneo, Importar e conciliar automaticamente e TOTVS Web Service  
  
  
  
Deixar a data inicial e final em branco, pois o processo busca sempre os últimos 15 dias desmarcar a opção considerar data de liquidação.

Na opção ***Hora da execução,*** informar a data e hora para a primeira execução, recomendamos que seja o próximo dia útil as 07:00

Na opção ***Repetir a execução*** selecionar todas as semanas, no mesmo horário, no(s) dia(s), marcar as opções de 2ª feira a 6ª feira.

**Após execução, o processo será agendado.**

Acessar:

**Ambiente | Gerenciamento de Jobs**

Criar um filtro para listar os jobs agendados
