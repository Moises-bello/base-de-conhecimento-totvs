---
content_hash: 1b64ab608b9852c0d88fda8803c4c4e64f1d5a7ee9475c9857fa2897eb724263
fetched_at: '2026-06-29T00:11:54.975928+00:00'
page_id: '859580678'
product: rm
source: tdn-rm
title: DT - Finaliza Férias - Data Final
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=859580678
version: 10
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS RH |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | Finaliza Férias |
| País: | Brasil |
| Story | [DRHCALCRM-6780](https://jiraproducao.totvs.com.br/browse/DRHCALCRM-6780) |

## **02. VERSÃO**

Esta solução está disponível a partir dos patchs/release abaixo:

* 12.1.2402.192
* 12.1.2406.121
* 12.1.2410

## **03. SITUAÇÃO/REQUISITO**

Permitir que o processo de finalização de férias execute de forma agendada considerando os funcionários que tem retorno de férias até a data da execução

## **04. SOLUÇÃO**

Tratar no processo de finalização de Férias para que o mesmo considere a data da execução do processo como data final e execute a finalização das férias para o funcionários que estão retornando de férias conforme a data final. Para isto, foi criado o parâmetro 'Considera a data atual como a data final' no processo Finaliza Férias, para que, quando marcado considera a data final igual ao dia da execução no agendamento, para que o usuário não precise executar a finalização todos os dias de forma manual.  

Parâmetro Marcado, Parâmetro Desmarcado, Passo 03, Passo 04passo1,passo2yespasso1

Parâmetro marcado, a data final foi alterada para o dia de Hoje:

Na execução considerou a data final = 28/07/2024, no agendamento:

E criou o agendamento para o próximo dia, pois foi feito o agendamento diário:

nopasso2

Parâmetro desmarcado, permaneceu com a data fim o ultimo dia da competência:

Na execução considerou a data final = 31/07/2024, no agendamento:

E criou o agendamento para o próximo dia, pois foi feito o agendamento diário:

## **05. DEMAIS INFORMAÇÕES**

Quando a competência da base for anterior ao mês atual, o processo irá considerar a data fim como o ultimo dia da competência

Exemplo:

Competência 06/2024.

Data da execução: 28/07/2024

O processo com o parâmetro marcado, irá considerar os funcionário com retorno de férias até dia 30/06/2024

**Este parâmetro não contempla a finalização de Férias próximo mês. Somente as férias que estão finalizando na competência atual da base IMPORTANTE!**

## **06. ASSUNTOS RELACIONADOS**

* [Finaliza Férias](https://tdn.totvs.com.br/pages/releaseview.action?pageId=452719578)
