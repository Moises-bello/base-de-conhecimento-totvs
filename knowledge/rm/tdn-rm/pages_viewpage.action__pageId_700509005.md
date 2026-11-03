---
content_hash: 9bb0b9b184e40e68543141134054e392f6bfe0b1f34a7a98821092e053f1e983
fetched_at: '2026-06-29T00:11:22.227095+00:00'
page_id: '700509005'
product: rm
source: tdn-rm
title: DT - RM Portal - Sugestão de Férias - Impedir sugestão de férias após data
  limite início do gozo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=700509005
version: 8
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
| Ticket: | [14659528](https://totvssuporte.zendesk.com/agent/tickets/14659528) |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHCALCRM-2755](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-2755) |

## **02. SITUAÇÃO/REQUISITO**

Ao realizar a sugestão de férias através do RM Portal, com abono pecuniário, está sendo permitido informar a data de início das férias maior que a data limite de gozo de férias,  ocasionando pagamento de férias em dobro dos dias que ultrapassam a data limite de férias.

## **03. SOLUÇÃO**

Foi criado em **RH | Folha de Pagamento | Configurações | Parametrizador | RM Portal | Grupo de Acesso | Férias II** o parâmetro '**Impedir sugestão de férias após data limite início do gozo**'. Ao marcar este parâmetro, o sistema irá impedir a marcação de férias com a data de início que ultrapasse o limite de gozo de férias para que não seja pagas férias em dobro para o funcionário.

**Exemplo:**

**1) Funcionário com as férias de acordo com as datas:**

**Início Período Aquisitivo: 01/03/2021**

**Fim Período Aquisitivo: 28/02/2022**

**Data Limite Início de Gozo: 30/01/2023**

**Data de Início das férias: 31/01/2023**

**Data de Fim das férias: 19/02/2023**

**Dias de férias: 20 dias**

**Dias de Abono: 10 dias**

**1) Com o parâmetro 'Impedir sugestão de férias após data limite início do gozo' - DESMARCADO:**

**Observação: Com o parâmetro desmarcado, ele permite a marcação de férias.**

**2) Com o parâmetro 'Impedir sugestão de férias após data limite início do gozo' - MARCADO:**

**Observação: Com o parâmetro marcado, ele impede a marcação de férias e apresenta a mensagem ' - Data de início das férias dd/mm/aaaa ultrapassa o limite do gozo de férias dd/mm/aaaa.**

## **04. DEMAIS INFORMAÇÕES**

         O default do parâmetro será **desmarcado.** Caso o usuário queira utilizar o recurso, deverá editar os grupos de acesso existentes e marcar o parâmetro.

## **05. ASSUNTOS RELACIONADOS**

**[Parâmetros do RM Portal](https://tdn.totvs.com.br/pages/viewpage.action?pageId=452719215)**
