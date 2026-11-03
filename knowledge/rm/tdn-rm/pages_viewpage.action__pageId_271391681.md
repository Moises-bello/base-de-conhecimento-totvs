---
content_hash: 5dfc0c7f7a7916c528482b76b93299ab382574a25c3d17888e2c0b107feec908
fetched_at: '2026-06-29T00:08:27.152876+00:00'
page_id: '271391681'
product: rm
source: tdn-rm
title: 192718 MRH-3132 DT Histórico da Tabela Salarial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=271391681
version: 108
---

# HISTORICO DA TABELA SALARIAL

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão de Pessoas |
| **Função:** | Histórico da Tabela Salarial |
| **Situação/Requisito:** | Ao aplicar filtro com a condição: 'Código e Operador: IS Not Null', no histórico de Tabelas salariais é apresentado o seguinte erro: ''Ocorreu um erro ao efetuar leitura da visão: The multi-part identifier 'HISTORICO.CODHISTORICO' could not be bound'' |
| **Solução/Implementação:** | A consulta sql estava buscando a tabela errada, assim foi inserido a propriedade ColProps.Origin = 'VHISTORICOTABELASALARIAL.CODHISTORICO' no CODHISTORICO. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | MRH-3132 |
| **Requisito (ISSUE):** |  |

divs
