---
content_hash: 3e3d70e63d399501bbcc519856245bdd86e6c0fac4539ad7bbbf5bff991d4fcb
fetched_at: '2026-06-29T00:08:17.568517+00:00'
page_id: '256311503'
product: rm
source: tdn-rm
title: TVQSIP_DT_Exclusão_Bolsa_Retroativa_Com_Bolsa_Tem_Repasse
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=256311503
version: 120
---

# Bolsa Retroativa

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Bolsa Retroativa |
| **Situação/Requisito:** | Ao executar a exclusão de uma bolsa retroativa para um aluno que tinha algum repasse de bolsa cadastrado, era apresentado uma não conformidade referente a violação de chave. |
| **Solução/Implementação:** | Realizamos uma evolução no serviço de exclusão para que valide se existe algum repasse para a bolsa e avise ao usuário através do log através de uma mensagem mais intuitiva. |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | TVQSIP |
| **Requisito (ISSUE):** | *N/A* |

divs
