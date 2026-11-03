---
content_hash: cb4741482c4768ef753eed3508bfb7c2b9fbdb5f61a452d6ee1f9f7d4a583749
fetched_at: '2026-06-29T00:11:22.107365+00:00'
page_id: '698615972'
product: rm
source: tdn-rm
title: FISCAL01-18305 - DT - Ajustes na Rotina Federal -  DCTF
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-18305+-+DT+-+Ajustes+na+Rotina+Federal+-++DCTF
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Rotina Federal DCTF |
| País: | Brasil |
| Ticket: | [Ticket #14537471](https://totvssuporte.zendesk.com/agent/tickets/14537471 "View ticket on the Zendesk portal") |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-18263 |

## **02. SITUAÇÃO/REQUISITO**

**Item 1** - Ao validar o arquivo txt da rotina DCTF mensal é apresentado a inconsistência:  
Registro 000019 - Pagamento Campo 11 - Dia/Semana/Quinzena/Decêndio do Período de Apuração Erro - Campo difere do Dia do Período de Apuração informado no Registro tipo R10 respectivo.

**Item 2** - Ajustar campo 19 "Nº de referência" do registro R11 para que seja gerado em branco quando não for usado o código de receita pertinente, o mesmo está sendo gerado com zeros.

**Item 3** - Ajustar campo campo 15 do registro R11 para considerar o último dia do período, o mesmo está considerando o primeiro dia.

**03. SOLUÇÃO**

**Ajuste Item 1** - Foram realizados os ajustes necessários para que a rotina atenda as seguintes regras para geração do campo 11 nos registros R10\R11:

| REGRAS |
| --- |
| ***Em se tratando de impostos ou contribuições com período de apuração mensal, este campo é preenchido automaticamente pelo programa. Nos demais casos, observar*** ***- diário, informar o dia da ocorrência do fato gerador.***  ***- semanal, informar a semana (1 a 5) em que ocorreu o fato gerador (ver exemplo do Atenção).*** ***- decendial, informar o decêndio (1 a 3) em que ocorreu o fato gerador.*** ***- quinzenal, informar a quinzena (1 ou 2) em que ocorreu o fato gerador.*** ***- mensal (preenchido automaticamente pelo programa).*** ***Os valores correspondentes a fatos geradores cujo início e término do período de apuração recaírem em meses diferentes devem ser informados na DCTF do mês a que o último dia do período de apuração pertencer.*** |

**Ajuste Item 2** - Campo 19 do registro R11 passa a ser gerado em branco caso não seja usado o código de receita 4028.

**Ajuste Item 3** - Campo Campo 15 do registro R11 passa a ser gerado com o último dia do período.

Ajustes realizados no Layout DCTF - com data 13/07/2022 - Disponível no [Totvs Compartilhamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035128774-Cross-Segmentos-Linha-RM-Fis-Como-realizar-a-importa%C3%A7%C3%A3o-de-layouts-utilizando-o-TOTVS-Compartilhamento-).
