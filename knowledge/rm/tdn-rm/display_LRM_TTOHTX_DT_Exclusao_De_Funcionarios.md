---
content_hash: 0da6a571c5bc9caeee237466d7c9f9c8db87331bf6685150b89d986005abade4
fetched_at: '2026-06-29T00:06:16.968295+00:00'
page_id: '212902985'
product: rm
source: tdn-rm
title: TTOHTX_DT_Exclusao_De_Funcionarios
type: documentation
url: https://tdn.totvs.com/display/LRM/TTOHTX_DT_Exclusao_De_Funcionarios
version: 2
---

# EXCLUSÃO DE FUNCIONÁRIOS ADMITIDO VIA REQUISIÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projeto* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Exclusão de funcionário* |
| **Situação/Requisito:** | Ao tentar excluir um funcionário que foi admitido via requisição e não tem ficha financeira, é apresentado mensagem de erro. |
| **Solução/Implementação:** | Criado uma consulta na tabela de requisisão do vitae, se existir alguma requisisão para a chapa e coligada é apresentado mensagem informando. A mesma foi alterada para "Não é possível realizar a exclusão do funcionário {0} pois ele foi admitido via requisição." |
| **Chamados relacionados:** | TTOHTX |
| **Versões/Release:** | *12.1.9* |

divs
