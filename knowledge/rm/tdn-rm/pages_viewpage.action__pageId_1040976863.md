---
content_hash: 3f2bbaba18f8417a64f96d8ac750cd77dc55e93a86c2efbe061ecee95ddc55ad
fetched_at: '2026-06-29T00:05:49.378021+00:00'
page_id: '1040976863'
product: rm
source: tdn-rm
title: 5 - Agendamento do Job Atualizar Transação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1040976863
version: 4
---

O processo **Atualizar Transação** é responsável por consultar o status das transações junto à instituição bancária e atualizar automaticamente as informações no ERP.

Durante essa atualização, o sistema pode alterar o status das transações para:

* **Pagamento Concluído**
* **Pagamento Expirado**
* Outros status retornados pelo processamento

Esse processo pode ser **executado manualmente** ou **agendado como um Job automático**.

No menu do sistema, acesse:

**Contas a Pagar / Receber → Boleto Híbrido → Atualizar Transação**

O processo **Atualizar Transação** possui dois modos de execução:

## Diário

Modo recomendado para execução recorrente.

Nesse modo o sistema irá:

* Buscar atualizações ocorridas **no dia atual**
* Considerar também **transações do dia anterior**

Esse formato é ideal para **agendamento automático via Job**.

## Período

Modo recomendado quando for necessário **processar um intervalo específico de datas**, por exemplo:

* Quando o job ficou inativo
* Quando é necessário reprocessar transações de um período anterior

⚠️ Este tipo de execução **não permite recorrência**, pois o período informado é fixo.

No exemplo abaixo será demonstrado o **agendamento diário do processo**, utilizando o modo **Diário**.

Selecione a opção **Diário** e clique em **Avançar**.

Para configurar o job para execução **a cada 5 minutos**, preencha os campos conforme abaixo.

### Dividir o processo em

Informe:

10

Esse campo define em **quantas frações o processamento será dividido**, permitindo maior performance.

*(O valor pode ser ajustado conforme a capacidade do ambiente.)*

### Executar em

Defina:

* **Data:** Data atual
* **Horário:** 2 minutos após o horário atual

### Frequência de execução

Selecione a opção:

**Diariamente**

No campo **A cada intervalo (em horas)** informe:

00:05

Isso fará com que o processo seja executado **a cada 5 minutos**.

### Executar o agendamento

Após preencher os dados:

Clique em **Executar** para concluir o agendamento.

Com essa configuração, o sistema executará o processo **todos os dias, a cada 5 minutos**.

Após a execução do processo, as transações podem assumir os seguintes status:

### Pagamento Confirmado

O pagamento foi confirmado pela instituição bancária, porém **a baixa do boleto não foi realizada automaticamente no ERP**.

Isso pode ocorrer, por exemplo, quando existe algum problema na contabilização da baixa do lançamento financeiro.

### Pagamento Concluído

O pagamento foi confirmado pelo banco e **a baixa do boleto foi realizada com sucesso no ERP**.

### Pagamento Expirado

O registro do boleto **expirou junto à instituição bancária**.

### Pagamento Cancelado

O registro do boleto foi **cancelado no banco**.

O processo **Ajuste de Transações** é utilizado para corrigir inconsistências quando o pagamento foi confirmado, mas o sistema não conseguiu concluir a baixa automaticamente.

Para executar esse processo:

1. Acesse a **visão de Transações do Boleto Híbrido**
2. Selecione as transações desejadas

1. Acesse:

**Processos → Ajuste de Transação**

1. Execute o processo.

Esse procedimento irá atualizar o status de:

**Pagamento Confirmado → Pagamento Concluído**

# Diferença entre os processos

## Atualizar Transação

Processo **automático e recorrente** responsável por:

* Consultar a **API da instituição bancária**
* Atualizar o status das transações
* Realizar automaticamente a **baixa ou expiração das transações**

## Ajuste de Transações

Processo **corretivo**, utilizado quando ocorre alguma falha durante a baixa automática.

Ele atua especificamente quando:

* O pagamento foi confirmado pelo banco
* Mas o lançamento financeiro ou boleto **não foi baixado corretamente no ERP**

Nesse caso, o processo ajusta o status para **Pagamento Concluído**.

# Resumo dos Processos

| Processo | Finalidade |
| --- | --- |
| **Atualizar Transação** | Processo automático e recorrente que consulta a API para atualizar os status das transações |
| **Ajuste de Transações** | Processo corretivo utilizado para tratar falhas ocorridas durante a execução do Atualizar Transação |
