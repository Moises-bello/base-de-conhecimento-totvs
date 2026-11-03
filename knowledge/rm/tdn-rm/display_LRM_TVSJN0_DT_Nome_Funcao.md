---
content_hash: f5daa8c050d8ffd19ddeaad89b8b92e4465e45d0191416208a3540852248292f
fetched_at: '2026-06-29T00:08:18.549892+00:00'
page_id: '264340659'
product: rm
source: tdn-rm
title: TVSJN0_DT_Nome_Funcao
type: documentation
url: https://tdn.totvs.com/display/LRM/TVSJN0_DT_Nome_Funcao
version: 113
---

# CADASTRO DE FUNÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construções e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Função* |
| **Situação/Requisito:** | Ao tentar incluir um agendamento automático de exames o erro abaixo é apresentado.  Não é possível definir a coluna 'NOME\_FUNCAO'. O valor viola o limite de MaxLength desta coluna. |
| **Solução/Implementação:** | *A propriedade da tabela PFUNCAO que se refere ao nome da função se encontrava com 40 caracteres , porém o correto seria 100 caracteres.* |
| **Chamados relacionados:** | TVSJN0 |

divs
