---
content_hash: d4e467d66d978cd6d876239101842f3678a154cc1e1c0d498c486115a9ac4c1c
fetched_at: '2026-06-29T00:08:09.308728+00:00'
page_id: '239033460'
product: rm
source: tdn-rm
title: TV3959_DT_Movimentacao_Exemplar_Igual_Unidade_Diferente_Impedindo_Emprestimo
type: documentation
url: https://tdn.totvs.com/display/LRM/TV3959_DT_Movimentacao_Exemplar_Igual_Unidade_Diferente_Impedindo_Emprestimo
version: 116
---

# MOVIMENTAÇÕES

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Bibliotecária* |
| **Função:** | *Movimentações* |
| **Situação/Requisito:** | *Se uma publicação possui exemplares em unidades diferentes, porém possuem o mesmo código de exemplar e tombos diferentes, o sistema no momento de fazer o empréstimo do exemplar que não está emprestado na sua unidade correta, o sistema informa que não é permitido pois identifica que o exemplar já está emprestado, porém o empréstimo que o sistema informa é de outra unidade, da mesma publicação com mesmo código de exemplar porém com tombos diferentes.* |
| **Solução/Implementação:** | *Foi identificado que no momento que o sistema verifica se o exemplar está emprestado, o sistema não está considerando a unidade, fazendo com que o sistema identifique que sim, pois os exemplares tem o mesmo código. Após inserir o filtro de unidade, o conflito não ocorreu mais, permitindo assim os empréstimos e devoluções corretos.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *TVBDSZ* |
| **Requisito (ISSUE):** | *N/A* |

divs
