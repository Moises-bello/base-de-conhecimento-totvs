---
content_hash: a3d1f3e82e01c5160cfc134bc758a010e48f976db0b4e366d8793cc03fe03e78
fetched_at: '2026-06-29T00:08:03.432428+00:00'
page_id: '235321191'
product: rm
source: tdn-rm
title: TUNDBU_DT_Funcao_RANT_Salario_Composto_Meses_Anteriores
type: documentation
url: https://tdn.totvs.com/display/LRM/TUNDBU_DT_Funcao_RANT_Salario_Composto_Meses_Anteriores
version: 2
---

# FUNÇÃO RANT RETORNA VALOR INCORRETO DE SALÁRIO COMPOSTO DE MESES ANTERIORES

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Fórmula* |
| **Situação/Requisito:** | *Para funcionários que utilizam salário composto, a função de fórmula RANT não está considerando o valor de todos os eventos de salário, quando é utilizada data anterior à competência atual.*  *Se o evento da época não está sendo usado atualmente como salário composto, o seu valor não é acumulado para o retorno na função RANT.* |
| **Solução/Implementação:** | *Ajuste na função RANT para considerar todos os registros de salário composto da época solicitada, independente do evento de salário estar sendo utilizado atualmente ou não.* |
| **Chamados   relacionados:** | *TUNDBU, TUOSME* |
| **Versões/Release:** | *11.82.43, 12.1.11* |
