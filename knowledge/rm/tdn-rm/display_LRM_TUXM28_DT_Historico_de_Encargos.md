---
content_hash: e8558c1b499a25a266a583b9c5eacb8547fee8f810abd7fd62ce8d8ae49c8e36
fetched_at: '2026-06-29T00:08:09.884307+00:00'
page_id: '240294313'
product: rm
source: tdn-rm
title: TUXM28_DT_Historico_de_Encargos
type: documentation
url: https://tdn.totvs.com/display/LRM/TUXM28_DT_Historico_de_Encargos
version: 112
---

# HISTÓRICO DE ENCARGOS

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Folha de Pagamento |
| **Função:** | Exclusão de Histórico de Encargos |
| **Situação/Requisito:** | Ao tentar excluir o registro de histórico de encargos, através da tela de edição, o sistema apresenta mensagem "A cadeia de caracteres não está em um formato válido" |
| **Solução/Implementação:** | Verificado que o erro ocorria devido à validação de data de competência. Alteração na validação para que a mesma só seja realizada em casos de inclusão e edição de registro e não em exclusão. |
| **Chamados relacionados:** | TUXM28 |

divs
