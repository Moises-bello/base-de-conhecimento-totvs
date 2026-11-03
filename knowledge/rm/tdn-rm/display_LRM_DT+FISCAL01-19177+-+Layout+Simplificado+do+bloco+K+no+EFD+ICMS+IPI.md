---
content_hash: cb58409f34b13b83b30dff1ae09377d46f927abeda547c559bcd7b69d642be21
fetched_at: '2026-06-29T00:11:28.611736+00:00'
page_id: '732671619'
product: rm
source: tdn-rm
title: DT FISCAL01-19177 - Layout Simplificado do bloco K no EFD ICMS IPI
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+FISCAL01-19177+-+Layout+Simplificado+do+bloco+K+no+EFD+ICMS+IPI
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Geração do arquivo SPED EFD ICMS IPI |
| País: | Brasil |
| Ticket: | 15996939 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-19177 |

## **02. SITUAÇÃO/REQUISITO**

Na geração do arquivo EFD ICMS IPI, no Modelo Simplificado do bloco K, o Sistema está considerando os registros K255 e K292 , porém, no guia prático da escrituração esses blocos não devem ser considerados no Leiaute Simplificado, apenas no modelo de layout completo.

## **03. SOLUÇÃO.**

Alteração dos registros K255 e K292 para que não sejam gerados no modelo simplificado do bloco K.

Disponível a partir da versão 12.1.2209
