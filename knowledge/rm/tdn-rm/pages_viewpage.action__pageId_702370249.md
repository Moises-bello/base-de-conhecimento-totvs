---
content_hash: e46e20e6036dbce48e1b222ced6c8fd251d89a377471884eed89d481159cca06
fetched_at: '2026-06-29T00:11:22.395606+00:00'
page_id: '702370249'
product: rm
source: tdn-rm
title: DT - RM Portal - Abono Pecuniário - Limite até 10 dias de abono dentro período
  aquisitivo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=702370249
version: 10
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | Plataforma RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | RM Portal |
| País: | Brasil |
| Ticket: | [11759110](https://totvssuporte.zendesk.com/agent/tickets/11759110) |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHCALCRM-1061](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-1061) |

## **02. SITUAÇÃO/REQUISITO**

Ao realizar a sugestão de férias através do RM Portal, com abono pecuniário, está sendo permitido informar mais de 10 (dez) dias de abono pecuniário em um mesmo período aquisitivo.

## **03. SOLUÇÃO**

Foi criado em **RH | Folha de Pagamento | Configurações | Parametrizador | RM Portal | Grupo de Acesso | Férias II** o parâmetro '**Limite até 10 dias de abono dentro período aquisitivo**'. Ao marcar este parâmetro, o sistema irá limitar a quantidade de dias de abono pecuniário em 10 (dez) dias dentro do mesmo período aquisitivo.

**Exemplo:**

**Funcionário com as férias de acordo com as datas:**

**Início Período Aquisitivo: 01/03/2021**

**Fim Período Aquisitivo: 28/02/2022**

**a) Período de 1ª Sugestão de Férias:**

**Data de Início:**

**Data de Fim:**

**Dias de férias: 14 dias**

**Dias de Abono: 9 dias**

**b) Período da 2ª Sugestão de Férias:**

**Data de Início:**

**Data de Fim:**

**Dias de férias: 9 dias**

**Dias de Abono: 2 dias**

**1) Com o parâmetro 'Limite até 10 dias de abono dentro período aquisitivo' - DESMARCADO:**

**Observação: Com o parâmetro desmarcado, ele permite a sugestão de férias com mais de 10 dias de abono de férias.**

**2) Com o parâmetro 'Limite até 10 dias de abono dentro período aquisitivo' - MARCADO:**

**a) Período de 1ª Sugestão de Férias:**

**Data de Início:**

**Data de Fim:**

**Dias de férias: 14 dias**

**Dias de Abono: 9 dias**

**b) Período da 2ª Sugestão de Férias:**

**Data de Início:**

**Data de Fim:**

**Dias de férias: 9 dias**

**Dias de Abono: 2 dias**

**Observação: Com o parâmetro marcado, ele impede a marcação de férias e apresentará a mensagem ' - Dias de abono não podem superar os xx dias.**

## **04. DEMAIS INFORMAÇÕES**

         O default do parâmetro será **desmarcado.** Caso o usuário queira utilizar o recurso, deverá editar os grupos de acesso existentes e marcar o parâmetro.

## **05. ASSUNTOS RELACIONADOS**

**[Parâmetros do RM Portal](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719215)**
