---
content_hash: f11cf19355407d6517932a398e9b1adc935eab44c69170945b633999dab24558
fetched_at: '2026-06-29T00:06:10.353754+00:00'
page_id: '203762095'
product: rm
source: tdn-rm
title: TTEHZL_DT_Homolognet
type: documentation
url: https://tdn.totvs.com/display/LRM/TTEHZL_DT_Homolognet
version: 1
---

# Homolognet

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e projetos* |
| **Módulo:** | *Folha de pagamento* |
| **Função:** | *Homolognet* |
| **Situação/Requisito:** | Ao consultar rescisão emitida via rotina homolognet, é apresentada a seguinte inconsistência:  181 - A informação referente ao salário líquido foi removida pois a data de afastamento não se encontra entre o primeiro e o sexto dia do mês |
| **Solução/Implementação:** | Otimizada rotina homolognet, implementada regra para que a tag VLSalarioLiquidoMesAnteriorRescisao só vá para o arquivo caso a data de  afastamento esteja entre o primeiro e o sexto dia do mês |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TTEHZL |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.41* |

Ao consultar rescisão emitida via rotina homolognet, é apresentada a seguinte inconsistência:

181 - A informação referente ao salário líquido foi removida pois a data de afastamento não se encontra entre o primeiro e o sexto dia do mês
