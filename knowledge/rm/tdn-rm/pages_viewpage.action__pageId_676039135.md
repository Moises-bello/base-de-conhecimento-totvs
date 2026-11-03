---
content_hash: 30d291d3b57a3a9df3582d9566945398cc340638a8da300b81f5d7a17a09fd7a
fetched_at: '2026-06-29T00:11:17.022007+00:00'
page_id: '676039135'
product: rm
source: tdn-rm
title: 13776836 FISCAL01-17663 - DT - Período Apuração Pagamento DARF DCTF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=676039135
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Rotinas Fiscais - Gerador de Saídas |
| País: | Brasil |
| Ticket: | [13776836](https://totvssuporte.zendesk.com/agent/tickets/13776836 "View ticket on the Zendesk portal") |
| Requisito/Story/Issue (informe o requisito relacionado) : | [FISCAL01-17663](https://jiraproducao.totvs.com.br/browse/FISCAL01-17663) |

## **02. SITUAÇÃO/REQUISITO**

**INTERPRETAÇÃO DE DEMANDA**

Cliente informa que ao gerar a rotina na nova MDI o layout está levando as informações do registro R11 com data de apuração como 01/01/0001, incorretamente.

Registro **R11** - Posição 71 a 78

**TESTES REALIZADOS**

Foi gerado o arquivo da rotina em nossa ambiente com o último layou disponibilizado e verificado que realmente o registro R11 posição 71 a 78 está sendo gerado com o valor de 01010001.

 ​

**BENEFÍCIOS ALCANÇADOS**

Correção do sistema para que seja apresentada a correta data de apuração no registro.

## **03. SOLUÇÃO**

Foi alterado o **campo** informado na **Ligação** do campo Período de Apuração. Antes o valor passado era o **CodPer**, agora é o **InicioPeriodo**.

**Arquivo gerado**

Disponível a partir da versão 12.1.34
