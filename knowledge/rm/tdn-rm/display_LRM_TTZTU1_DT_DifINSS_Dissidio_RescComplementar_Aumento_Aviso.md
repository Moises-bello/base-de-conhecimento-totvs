---
content_hash: b9e36550ea2c5d3d9d9ae06ee68fb5043977f6bc48e3b49ea0c4f30b77fff97d
fetched_at: '2026-06-29T00:06:24.705182+00:00'
page_id: '224120289'
product: rm
source: tdn-rm
title: TTZTU1_DT_DifINSS_Dissidio_RescComplementar_Aumento_Aviso
type: documentation
url: https://tdn.totvs.com/display/LRM/TTZTU1_DT_DifINSS_Dissidio_RescComplementar_Aumento_Aviso
version: 2
---

# DIFERENÇA DE INSS POR DISSÍDIO NA RESCISÃO COMPLEMENTAR COM AUMENTO SALARIAL NO PERIODO DE AVISO PRÉVIO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Rescisão Complementar* |
| **Situação/Requisito:** | *Em uma Rescisão Complementar por dissídio, quando o aumento salarial é no mês seguinte ao da demissão, durante o periodo de aviso prévio indenizado, a diferença do evento de CC 62, Aviso Prévio, é paga proporcional aos dias posteriores ao reajuste do salário.*  *Entretanto, ao calcular a diferença de INSS a ser descontada no evento de CC 68, é considerado na base o valor integral da diferença do Aviso Prévio, considerando o total de dias de aviso.* |
| **Solução/Implementação:** | *Ajuste no cálculo da diferença de INSS na Rescisão Complementar por dissídio, para que no caso de um aumento salarial no mês seguinte ao da demissão, durante o periodo de aviso prévio indenizado, seja considerado na base de cálculo somente o valor da diferença de Aviso Prévio referente aos dias posteriores ao reajuste do salário.* |
| **Chamados   relacionados:** | *TTZTU1, TUDKL7* |
| **Versões/Release:** | *11.82.43* |
