---
content_hash: 0e505f1765dec11451acc009a3e91972ccf7cd92858619bcdff890a85e72c4a2
fetched_at: '2026-06-29T00:08:05.922007+00:00'
page_id: '236422488'
product: rm
source: tdn-rm
title: TTHMKK_DT_Alteracao_Campos_Do_Cadastro
type: documentation
url: https://tdn.totvs.com/display/LRM/TTHMKK_DT_Alteracao_Campos_Do_Cadastro
version: 115
---

# ALTERAÇÃO CAMPOS DO CADASTRO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Alteração Campos de Cadastro* |
| **Situação/Requisito:** | No processo de alteração de campos cadastrais, o sistema somente habilita o campo Histórico ‘Data da Mudança’, quando clico nos campos para informar as formulas. Quando o processo já está com o campo informado, salvo no perfil de parâmetros, o sistema permanece com o campo histórico desabilitado permitindo que o usuário realize o processo sem informar a data da mudança.  O log da execução do processo não condiz com a situação da alteração. No log é apresentado o total de registros alterados e ou com avisos igual a zero, porem os dados do funcionário foram alterados corretamente. |
| **Solução/Implementação:** | Quando tiver perfil de usuário salvo, o campo 'Data da Mudança' deve ter o mesmo valor de quando clica no campo lookup para informar as formulas. Foi incluído no log a informação com as chapas que tiveram alteração e os campos que foram alterados. |
| **Chamados relacionados:** | TTHMKK |

divs
