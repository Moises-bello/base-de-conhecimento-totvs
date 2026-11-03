---
content_hash: 491a936d7216a20faf3394a400054673271372b4b179d111aa2f532a846ef4c0
fetched_at: '2026-06-29T00:11:32.033497+00:00'
page_id: '743687201'
product: rm
source: tdn-rm
title: FISCAL01-19427 - DT -  Eventos R-4080 e R-4020 Alterações de comportamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=743687201
version: 2
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | EFD Reinf |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-19443 |

## **02. SITUAÇÃO/REQUISITO**

**R-4080**  
Este evento deve passa a ser gerado para Lançamento de Saída, 

**R4020**  
Ao gerar o Evento R-4020, com o Tributo IRRFPJ e o Tipo de Recolhimento igual a "IRRF Devido pelo Prestador" deve ser gerada somente a Tag vlrBruto.

## **03. SOLUÇÃO**

**R-4080**  
O evento passa a ser gerado para Lançamento de Saída desde que tenha a Natureza Rendimento informada na Linha Outros Tributos.

**R-4020**  
As Tags de valores vlrBaseIR, vlrIR e demais tags do grupo Retenções não não vão ser geradas caso o tipo de recolhimento do IRRFPJ seja "Devido".

Disponível a partir da biblioteca 12.1.2205
