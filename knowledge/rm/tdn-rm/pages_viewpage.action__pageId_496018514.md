---
content_hash: 9b4b2a4ae025d79a88021e924f9bb029aff49987d01f865688be4a7d36fc1705
fetched_at: '2026-06-29T00:10:22.002853+00:00'
page_id: '496018514'
product: rm
source: tdn-rm
title: Afastamento por Licença Paternidade
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=496018514
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | RH |
| Módulo: | Folha de Pagamento |
| Função: | Afastamento por Licença Paternidade |
| Ticket: | [Ticket #3316211](https://totvssuporte.zendesk.com/agent/tickets/3316211 "View ticket on the Zendesk portal") |
| Requisito/Story/Issue | [FOPCALCULO01-4276](http://jiraproducao.totvs.com.br/browse/FOPCALCULO01-4276) |

## **02. SITUAÇÃO/REQUISITO**

Hoje o sistema está lançando automaticamente 15 dias de licença paternidade relativos a extensão da licença de 5 dias, porém a legislação informa que algumas empresas não se encaixam na modalidade de empresa cidadã e por esse motivo não ofertam a seus funcionário a extensão de 15 dias, e como sendo um processo jurídico da empresa que utiliza a funcionalidade o sistema deveria dar três opções possiveis para o caso, 5,15 e 20 dias.

## **03. SOLUÇÃO**

Foi criado em Configurações > Parametrizador > folha normal > Licença maternidade 2/2 com dois campos, para que se informe os motivos que serão utilizados para o afastamento de 5 e 20 dias.

## **04. DEMAIS INFORMAÇÕES**

Para que o afastamento considere 5 ou 20 dias deverá ser informado no motivo da mudança de situação o mesmo motivo informado no parametrizador, caso contrário o sistema irá considerar o calculo padrão de 15 dias, e como informativo será emitida uma mensagem de alerta informando a quantidade de dias de afastamento cadastrados.
