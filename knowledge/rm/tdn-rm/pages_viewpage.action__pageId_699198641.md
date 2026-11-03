---
content_hash: 1e236e41ea4583f6ea0a150c23f959a665e715c2929ac3ad486e5017791cb33c
fetched_at: '2026-06-29T00:11:22.129019+00:00'
page_id: '699198641'
product: rm
source: tdn-rm
title: DT FISCAL01-18322 - NFE - Chave de acesso com 43 dígitos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=699198641
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Envio de NF-e |
| País: | Brasil |
| Ticket: | [Ticket #14694869](https://totvssuporte.zendesk.com/agent/tickets/14694869 "View ticket on the Zendesk portal") |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-18322 |

## **02. SITUAÇÃO/REQUISITO**

Ao enviar notas fiscais de devolução a seguinte mensagem de erro é apresentada:  
   
**Mensagem Original: Element '** **[http://www.portalfiscal.inf.br/nfeinfNFe\*](http://www.portalfiscal.inf.br/nfeinfNFe* "Follow link") \*', attribute 'Id': [facet 'pattern'] The value 'NFe3122076510797100018055001000001020285976095' is not accepted by the pattern 'NFe[0-9]44'. Element '** **[http://www.portalfiscal.inf.br/nfeinfNFe\*](http://www.portalfiscal.inf.br/nfeinfNFe* "Follow link") \*', attribute 'Id': 'NFe3122076510797100018055001000001020285976095' is not a valid value of the local atomic type.**  
**Identificador do Movimento: 2649204, Chave de Acesso: 3122076510797100018055001000001020285976095**

## **03. SOLUÇÃO.**

Incluída validação para tratar Modalidade null no calculo da Chave de Acesso.  
Incluída validação para tratar Chave de Acesso calculada com menos de 44 dígitos.  
Incluído Alerta para recalcular chave de acesso inválida para notas enviadas em contingência.

Disponível a partir da versão 12.1.32.
