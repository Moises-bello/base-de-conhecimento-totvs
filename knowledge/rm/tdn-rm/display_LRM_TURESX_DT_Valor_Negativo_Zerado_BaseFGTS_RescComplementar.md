---
content_hash: dcb2c12ddbded249d85bdec21b0dd1dcbdb2d4305315d28825545bcfd64b5ddc
fetched_at: '2026-06-29T00:08:05.976000+00:00'
page_id: '236424941'
product: rm
source: tdn-rm
title: TURESX_DT_Valor_Negativo_Zerado_BaseFGTS_RescComplementar
type: documentation
url: https://tdn.totvs.com/display/LRM/TURESX_DT_Valor_Negativo_Zerado_BaseFGTS_RescComplementar
version: 2
---

# VALOR NEGATIVO QUE FOI ZERADO ESTÁ SENDO ABATIDO NA BASE DE FGTS DE RESCISÃO COMPLEMENTAR

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Rescisão Complementar* |
| **Situação/Requisito:** | *No cálculo da Rescisão Complementar, quando está marcado o parâmetro "Zerar evento de diferença quando o valor ficar negativo", e ocorre a situação de valor negativo, ao calcular o valor do FGTS da Base de diferença, está abatendo o valor negativo que foi zerado.*  *Se o valor negativo do evento foi zerado de acordo com o parâmetro, este valor não pode ser abatido na Base de FGTS do mês.* |
| **Solução/Implementação:** | *Ajuste no cálculo da Rescisão Complementar, para considerar na Base de FGTS do mês somente os valores realmente lançados no envelope do funcionário.*  *Caso a diferença resulte em um valor negativo, e este é zerado, o valor não irá compor a Base de FGTS do mês.* |
| **Chamados   relacionados:** | *TURESX, TUUBTF* |
| **Versões/Release:** | *11.82.44, 12.1.11* |
