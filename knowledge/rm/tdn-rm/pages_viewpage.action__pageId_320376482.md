---
content_hash: f5489909358e66740bd35ac37f606d430d6103eb779126e0ea83068d8cac50bf
fetched_at: '2026-06-29T00:08:47.744014+00:00'
page_id: '320376482'
product: rm
source: tdn-rm
title: 1628952 EDUCACIONAL01-3186 DT Validação ao tentar excluir Turma/Disciplina
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=320376482
version: 2
---

# VALIDAÇÃO AO EXCLUIR TURMA/DISCIPLINA

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Educacional |
| **Módulo:** | TOTVS Gestão Educacional |
| **Função:** | Exclusão de turma/disciplina |
| **Situação/Requisito:** | Ao tentar excluir uma turma/disciplina o sistema apresentava a mensagem: Processo de Exportação executado com erro: A network-related or instance-specific error occurred while establishing a connection to SQL Server. The server was not found or was not accessible. Verify that the instance name is correct and that SQL Server is configured to allow remote connections. (provider: Named Pipes Provider, error: 40 - Could not open a connection to SQL Server). |
| **Solução/Implementação:** | A mensagem de validação foi ajustada, indicando ao usuário as possíveis causas de origem da mensagem:  "Ocorreu erro na exportação para o Scientia. Possíveis causas do problema:  - Configuração do servidor do Scientia (SPDA) está incorreta. - Servidor inacessível. - Rede indisponível." |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | 1628952 |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
