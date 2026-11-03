---
content_hash: f35ca600c806b196d05e2afad99376a7af8e4926a8f46f3b3bd2a9c40049b8c0
fetched_at: '2026-06-29T00:08:14.053169+00:00'
page_id: '244439616'
product: rm
source: tdn-rm
title: TVBYCY_DT_Digitacao_Historico_Ensino_Basico
type: documentation
url: https://tdn.totvs.com/display/LRM/TVBYCY_DT_Digitacao_Historico_Ensino_Basico
version: 116
---

# NOME DO REQUISITO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Classis.Net* |
| **Função:** | *Digitação de Histórico* |
| **Situação/Requisito:** | *Ao realizar a digitação de histórico, ocorrem situações onde a posição de uma disciplina que está sendo cadastrada some ao clicar no botão Novo.* |
| **Solução/Implementação:** | *Foi realizado algumas melhorias na usabilidade do cadastro, que evita que algumas validações existentes na tela sejam executadas em diferentes situações e que dependendo da ordem de preenchimento causa uma confusão por parte do usuário.*  1) Melhorado a seleção/edição das colunas que possuem lista. Não é necessário realizar 3 ou mais cliques para abrir a listagem.  2) Ao realizar um novo cadastro, a primeira coluna é selecionada para evitar que a validação de obrigatoriedade da coluna seja emitido antes de concluir o cadastro das demais informações.  3) Ao selecionar uma disciplina na lista da coluna de Disciplina que já esteja cadastrada, ambas as linhas ficarão marcadas em vermelho, apenas para orientar o usuário que existe esta duplicidade.  4) Alterado a ordem das colunas Disciplinas e Posição. Para exibir a lista de posições é importante já ter preenchido primeiro a coluna da disciplina. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
