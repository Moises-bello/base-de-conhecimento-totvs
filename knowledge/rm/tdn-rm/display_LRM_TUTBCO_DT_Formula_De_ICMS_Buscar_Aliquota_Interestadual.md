---
content_hash: 866328f4e38d653df7d5a320a10d2958b6fd6a7eb71ff651bf9ef80cde7ab6ce
fetched_at: '2026-06-29T00:08:05.881542+00:00'
page_id: '235601906'
product: rm
source: tdn-rm
title: TUTBCO_DT_Formula_De_ICMS_Buscar_Aliquota_Interestadual
type: documentation
url: https://tdn.totvs.com/display/LRM/TUTBCO_DT_Formula_De_ICMS_Buscar_Aliquota_Interestadual
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
| **Solução/Implementação:** | Ao utilizar as fórmulas SOMAVICMSUFDEST, SOMAVICMSUFREMET, VICMSUFDEST, VICMSUFREMET o sistema verifica se o parâmetro  "Utilize Alíquota do Estado na Operação com Diferencial de Alíquota" no tipo de movimento está marcado e então utiliza o valor da alíquota interestadual  para calcular as fórmulas. Caso contrário, utiliza a alíquota da natureza fiscal. Para utilizar essa alíquota o sistema busca o valor no estado do cliente/fornecedor.  Anteriormente utilizava-se o estado da filial. |
| **Conversores e Parâmetros:** | *NA.* |
| **Chamados relacionados:** | TUTSO4 |
| **Requisito (ISSUE):** | *NA.* |
