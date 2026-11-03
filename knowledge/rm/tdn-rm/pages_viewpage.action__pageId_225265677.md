---
content_hash: 3f969caada3dbf6aebd8bb9c995cf7f36a53f9f146fa92f959d56150713c1f64
fetched_at: '2026-06-29T00:06:26.438092+00:00'
page_id: '225265677'
product: rm
source: tdn-rm
title: TUFCIZ_DT_Aumento_Contrato_apropriação_mensal_parcela
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=225265677
version: 116
---

# CONTABILIZAÇÃO POR COMPETÊNCIA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | **Educacional** |
| **Módulo:** | **Totvs Gestão Educacional** |
| **Função:** | *Gerar Contabilização* |
| **Situação/Requisito:** | *No novo modelo contábil, após proceder com um ‘Aumento’ no contrato, através da inclusão de uma parcela com novo serviço, e em seguida executar a contabilização da próxima competência, o sistema está gerando incorretamente uma apropriação mensal da parcela do aumento nas partidas do Evento contábil de Parcela. O correto seria gerar somente as partidas de aumento de contrato, utilizando o evento contábil de aumento de contrato.* |
| **Solução/Implementação:** | *Alterado processo "Gerar contabilização" no novo modelo contábil, quando ocorrer aumento de contrato, a contabilização da apropriação mensal do serviço será gravada na partida referente ao evento contábil de aumento de parcela.* |
| **Conversores e Parâmetros:** | *N/A.* |
| **Chamados relacionados:** | N/A |
| **Requisito (ISSUE):** | *N/A.* |
| **Versões/Release:** | *11.82.43* |
| **Versão Corrigida:** | *11.82.43* |
| **Versão Expedida:** | *11.82.43* |

divs
