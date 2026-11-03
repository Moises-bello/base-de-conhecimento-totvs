---
content_hash: 7cc0721d3f8940e4446ba45f45dd57e04f14adc8f732ff164aa983e0ba848442
fetched_at: '2026-06-29T00:10:33.311498+00:00'
page_id: '528467192'
product: rm
source: tdn-rm
title: 7647750 FISCAL01-11814 DT Escriturar Movimentos relacionados
type: documentation
url: https://tdn.totvs.com/display/LRM/7647750+FISCAL01-11814+DT+Escriturar+Movimentos+relacionados
version: 3
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Fiscal |
| Função: | Processo de Escrituração Fiscal |
| Ticket: | 7647750 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11814 |

## **02. SITUAÇÃO/REQUISITO**

Ao realizar a Escrituração de um determinado Movimento ocorre a seguinte mensagem de Erro:

"Movimentos relacionados ao movimento que se deseja escriturar, ainda não foram todos escriturados."

## **03. SOLUÇÃO**

Este erro ocorre porque os Movimentos relacionados são de Filiais diferentes, e o Processo

de Escrituração só encontra o vinculo de Movimentos da mesma Filial.

Porem o Movimento que se deseja escriturar, está com Status "Cancelado".

Ajustado o Processo de Escrituração Fiscal para que quando o Movimento estiver

vinculado e no Processo de escrituração não for encontrado o Movimento de Origem no Fiscal, está validação não

será realizada caso o Movimento que se deseja escriturar esteja Cancelado.
