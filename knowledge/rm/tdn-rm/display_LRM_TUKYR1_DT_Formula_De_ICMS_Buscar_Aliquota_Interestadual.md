---
content_hash: e45371ff1f146c74150a8f905f5a39bbad95e5ac839d19181c0e6993cef7984d
fetched_at: '2026-06-29T00:08:04.475366+00:00'
page_id: '235571843'
product: rm
source: tdn-rm
title: TUKYR1_DT_Formula_De_ICMS_Buscar_Aliquota_Interestadual
type: documentation
url: https://tdn.totvs.com/display/LRM/TUKYR1_DT_Formula_De_ICMS_Buscar_Aliquota_Interestadual
version: 2
---

# Fórmula De ICMS Buscar Alíquota Interestadual

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento |
| **Função:** | Inclusão de Movimento |
| **Situação/Requisito:** | Alteração no cálculo das das fórmulas SOMAVICMSUFDEST, SOMAVICMSUFREMET, VICMSUFDEST, VICMSUFREMET. |
| **Solução/Implementação:** | Ao utilizar as fórmulas SOMAVICMSUFDEST, SOMAVICMSUFREMET, VICMSUFDEST, VICMSUFREMET o sistema verifica se o parâmetro  "Utilize Alíquota do Estado na Operação com Diferencial de Alíquota" no tipo de movimento está marcado e então utiliza o valor da alíquota interestadual  para calcular as fórmulas. Caso contrário, utiliza a alíquota da natureza fiscal. |
| **Conversores e Parâmetros:** | *NA.* |
| **Chamados relacionados:** | TUQXY0 |
| **Requisito (ISSUE):** | *NA.* |
