---
content_hash: 2a147898c376b59a8244322c757e6a19572896e7ebaf77a84a3f53db1e8455ea
fetched_at: '2026-06-29T00:09:55.144237+00:00'
page_id: '447086891'
product: rm
source: tdn-rm
title: CONTROLADORIA01-2206 DT Importação Avaliação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=447086891
version: 1
---

# Importação de Avaliação

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Totvs Gestão Patrimonial |
| **Função:** | Importação de avaliação |
| **Situação/Requisito:** | No grid da tela de patrimônios existe um campo chamado  "Reavaliado", esse campo mostra se um patrimônio sofreu avaliação ou não. Entretanto, ao realizar uma avaliação do tipo "Implantação" via importação o campo não "Reavaliado" não exibe que o patrimônio sofreu avaliação. É necessário que após após a execução da avaliação do tipo implantação o campo seja modificado e mostre que o patrimônio envolvido sofreu avaliação. |
| **Solução/Implementação:** | Foram realizadas as seguintes modificações no processo de importação de avaliação:    1 - A rotina de importação de avaliação foi alterada para que, ao selecionar a opção "Implantação", o processo atualize o patrimônio para reavaliado.    2 - O cálculo da taxa de depreciação, do cenário avaliado, estava sendo realizado incorretamente quando o valor realizado da avaliação (coluna 4 do arquivo de importação) era superior a zero. O valor realizado não estava sendo considerado no cálculo da taxa, porém houveram modificações para solucionar essa questão. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | N/A. |
| **Documento de Referência:** | N/A. |
| **Pacote:** | N/A. |
