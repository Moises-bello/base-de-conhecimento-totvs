---
content_hash: 45380c89ecdbf0e543a2d47a360ee981bc5a009ebd71124ec1dc857cbf81d61b
fetched_at: '2026-06-29T00:09:38.733497+00:00'
page_id: '430041953'
product: rm
source: tdn-rm
title: CONTROLADORIA01-2080 DT Importação Avaliação Patrimonial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=430041953
version: 3
---

# Processo de importação de avaliação patrimonial

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Totvs Gestão Patrimonial |
| **Função:** | Processo de importação de avaliação patrimonial |
| **Situação/Requisito:** | Ao importar uma avaliação patrimonial, do tipo implantação, o sistema estava zerando a taxa do bem, impedindo que ele continuasse a depreciar. Também foi observado que, em algumas situações, a depreciação ajustada estava ficando negativa. |
| **Solução/Implementação:** | Para solucionar essas questões foram realizadas as seguintes atividades:  1 - O processo de importação de avaliação foi alterado para que, ao selecionar a opção “Esta importação é para implantação”, a taxa do patrimônio não fique zerada.  2 - O processo também passou por alterações para que a depreciação acumulada, da avaliação patrimonial, seja calculada corretamente. |
| **Conversores e Parâmetros:** | N/A. |
| **Tickets relacionados:** | N/A. |
| **Requisito:** | N/A. |
| **Documento de Referência:** | N/A. |
| **Pacote:** | N/A. |
