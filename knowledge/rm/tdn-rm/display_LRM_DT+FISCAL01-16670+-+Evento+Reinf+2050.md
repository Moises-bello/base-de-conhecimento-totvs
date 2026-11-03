---
content_hash: 3d930bfc648737d27fe75777ed006239cc22e21248af3945459c09057b8b1d4d
fetched_at: '2026-06-29T00:11:10.562560+00:00'
page_id: '644284627'
product: rm
source: tdn-rm
title: DT FISCAL01-16670 - Evento Reinf 2050
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+FISCAL01-16670+-+Evento+Reinf+2050
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | REINF - Rotina fiscal |
| País: | Brasil |
|  |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-16670 |

## **02. SITUAÇÃO/REQUISITO**

INTERPRETAÇÃO DE DEMANDA

Ao gerar o registro da REINF 2050, havendo mais de uma nota vinculada a processo de suspensão, os valores dos tributos suspensos não estão sendo somados.

TESTES REALIZADOS

Foram inseridas duas notas fiscais de saída, vinculando um mesmo processo judicial, ao gerar a rotina, o evento 2055 não soma os valores de suspensão dos tributos Funrural, é carregado o valor de apenas uma nota.

BENEFICIOS ALCANÇADOS

Correta geração e entrega da rotina

## **03. SOLUÇÃO.**

Correção do somatório de tributos suspensos nos lançamentos de saída da Reinf 2050 (funrural, gilrat e senar). É gerada apenas uma tag de informações de processo com o somatório de todos os tributos do Funrural (vlrCPSusp), Gilrat (vlrRatSusp) e Senar (vlrSenarSusp). 

Informações do processo:

xmlideEstab
         2
         00000001509700099970
         5
         696,29
         27,86
         69,64
]]>

### **Origem de dados**

| Elemento do XML | Origem |
| --- | --- |
| infoProc | Informações do processo judicial |
| tpProc | Tipo do processo judicial |
| codSusp | Código de suspensão relacionado aos tributos vinculados a um processo judicial |
| vlrCPSusp | Valor de retenção do tributo suspenso do Funrural |
| vlrRatSusp | Valor não retido pelo tributo Gilrat dentro do Funrural |
| vlrSenarSusp | Valor não retido pelo tributo Senar dentro do Funrural |
