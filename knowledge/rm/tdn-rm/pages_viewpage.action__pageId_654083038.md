---
content_hash: 47925e0733958a0543673217851cdd962aaa2822a023160adab62cd00d3cf583
fetched_at: '2026-06-29T00:11:12.513894+00:00'
page_id: '654083038'
product: rm
source: tdn-rm
title: Ajuste de transações PIX
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=654083038
version: 10
---

Este processo visa realizar atualizações nas transações PIX com base nas informações fornecidas pela instituição bancária. As atualizações podem ser realizadas de duas formas:

* **Pontual:**  é necessário acessar a visão de transações PIX, selecionar as transações desejadas e executar o processo.
* **Agendada**:. é possível agendar o processo para atualizar automaticamente as transações PIX da coligada, sendo necessário utilizar um ambiente em três camadas.

### Ajuste de Transação

O processo executado pela visão de transações PIX possibilita a atualização de uma ou mais transações. O requisito para que essa atualização ocorra é o status atual da transação, considerando apenas registros com os seguintes status: **Pagamento Solicitado, Pagamento Confirmado, Pagamento Expirado e Pagamento Cancelado.**

### Ajuste de Transação (Agendado)

Ao configurar o agendamento, o processo será executado automaticamente, respeitando as definições estabelecidas. Nesse caso, o sistema seleciona todas as transações da coligada em questão que possuem os status de **Pagamento Solicitado e Pagamento Confirmado**, procedendo à atualização.

### Atualização da Transação

Após identificar as transações elegíveis, considerando o processo previamente executado, o sistema realizará a atualização dos dados. Essa atualização é independente da origem do processo. Durante o processamento, o sistema verifica junto à instituição financeira o status atual da transação e, com base nesse retorno, procede com a atualização no sistema. Todas as operações serão registradas no Log/Histórico de Transações. Cada atualização aplicada à transação é registrada e pode ser consultada ao selecionar a transação e acessar o menu Anexos >> Histórico de Transações.

**Atualizações de Status para Transações com Pagamento Solicitado:**

| **Status Atual** | **Atualização** |
| --- | --- |
| **Aprovado** | Será feita a tentativa de baixa do lançamento. Se a baixa for concluída com sucesso, a transação terá seu status alterado para "**Pagamento Concluído**". Em caso de erro na baixa, o status será atualizado para "**Pagamento Confirmado**" |
| **Expirado** | A transação será atualizada para refletir o status de "**Pagamento Expirado**". |
| **Cancelado** | A transação será atualizada para refletir o status de "**Pagamento Cancelado**". |

**Atualização de Status para Transações com Pagamento Confirmado:**

| Status Atual | Atualização |
| --- | --- |
| **Confirmado** | O pagamento foi confirmado, mas a baixa não foi concluída, o sistema tentará realizar a baixa novamente. Caso a baixa seja bem-sucedida, o status será atualizado para "**Pagamento Concluído**". Se não, o status permanecerá como "Pagamento Confirmado". |

**Atualizações de Status para Transações com Pagamento Expirado:**

| Status Atual | Atualização |
| --- | --- |
| **Aprovado** | Será feito a tentativa de baixa do lançamento. Se a baixa for concluída com sucesso, a transação terá seu status alterado para "**Pagamento Concluído**". Em caso de erro na conciliação, o status será atualizado para "**Pagamento Confirmado**". |
| **Cancelado** | A transação será atualizada para refletir o status de "**Pagamento Cancelado**". |

**Atualização de Status para Transações com Pagamento Cancelado:**

| Status Atual | Atualização |
| --- | --- |
| **Cancelado** | Se cancelado no sistema, mas com status diferente na instituição bancária, será feita apenas uma atualização no Histórico das Transações, informando a discrepância. |
