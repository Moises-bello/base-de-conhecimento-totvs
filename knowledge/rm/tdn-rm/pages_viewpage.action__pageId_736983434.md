---
content_hash: dbccee7f88beba5a39f68be16bfc75df47f59e3dfcf35b04003f26143e27e94d
fetched_at: '2026-06-29T00:11:29.432832+00:00'
page_id: '736983434'
product: rm
source: tdn-rm
title: FISCAL01-18918 - DT Evento de Fechamento e Reabertura do período REINF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=736983434
version: 1
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
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-18918 |

## **02. SITUAÇÃO/REQUISITO**

Evoluir o processo que transmite os Eventos R-2099 e R-2098 para também transmitir o Evento R-4099 (Fechando e Reabrindo o período)

## **03. SOLUÇÃO**

Foi alterado o fechamento e reabertura dos eventos REINF R-2098 e R-2099 para geração de apenas um evento R-4099, onde o campo “fechRet” será o indicativo de fechamento ou reabertura. Implementada a geração do novo registro, de acordo com as regras da versão [2.1.1 da EFD Reinf](http://sped.rfb.gov.br/arquivo/show/6042)

Disponível a partir da biblioteca 12.1.2205
