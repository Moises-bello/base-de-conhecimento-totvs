---
content_hash: 58106315a5773f2d4115be8d05d313ec06762548dbcebb10ff857cd8928ca156
fetched_at: '2026-06-29T00:06:30.109979+00:00'
page_id: '235312796'
product: rm
source: tdn-rm
title: TUKNY4_DT_Log_Status_Opcoes_Nao_Salva_Status_Alterado_Cliente
type: documentation
url: https://tdn.totvs.com/display/LRM/TUKNY4_DT_Log_Status_Opcoes_Nao_Salva_Status_Alterado_Cliente
version: 118
---

# LOG ALTERAÇÃO DE STATUS DE OPÇÕES

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Processo Seletivo* |
| **Função:** | *Log de alteração de status de opções* |
| **Situação/Requisito:** | *Quando era executado algum processo que altera o status da opção do candidato em um processo seletivo que utiliza log de alteração de status, o sistema está salvando no log o "status na opção" sempre igual ao "status na opção (descrição original)" mesmo que estes sejam diferentes.* |
| **Solução/Implementação:** | *Foi identificado que no momento de salvar estas informações o sistema não estava buscando corretamente a descrição que o usuário definiu, está buscando sempre a mesma descrição original, foi feito o ajustes e assim o sistema passou a salvas estes dados corretamente.* |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
