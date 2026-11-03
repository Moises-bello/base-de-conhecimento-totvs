---
content_hash: 23b32b952ded0441bf8b0123562db46607498055623d7bcdbdf9d6e0e4b0291d
fetched_at: '2026-06-29T00:08:07.753804+00:00'
page_id: '237387968'
product: rm
source: tdn-rm
title: TUXJN6_DT_Sugestao_Compra_Erro_Alterar_Situacao
type: documentation
url: https://tdn.totvs.com/display/LRM/TUXJN6_DT_Sugestao_Compra_Erro_Alterar_Situacao
version: 118
---

# SUGESTÃO DE COMPRAS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Gestão Bibliotecária* |
| **Função:** | *Sugestão de compras* |
| **Situação/Requisito:** | *Ao tentar alterar a situação de uma sugestão de compras, o sistema retorna um erro não tratado na primeira tentativa de salvar, na segunda tentativa a alteração é salva com sucesso.* |
| **Solução/Implementação:** | *Foi identificado que no evento que é executado antes de salvar, o sistema tentava verificar campos que estavam vazios, foram inseridos validações para que verifique os campos vazios para evitar este tipo de erro. Após as validações, as alterações na sugestão de compras passaram a ser salvas na primeira vez sem erros.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
