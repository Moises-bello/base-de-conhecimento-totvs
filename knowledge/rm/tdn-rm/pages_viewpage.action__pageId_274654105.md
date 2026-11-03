---
content_hash: 98668b7c2226b22caedf1b44b077369e227cea4c00cbd04310a461d57d76644a
fetched_at: '2026-06-29T00:08:34.235444+00:00'
page_id: '274654105'
product: rm
source: tdn-rm
title: 140439 FINANCEIRO01-111 Baixa de Lançamentos - Controle de Concorrência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=274654105
version: 95
---

# Baixa de Lançamentos - Controle de Concorrência

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | TOTVS Gestão Financeira |
| **Função:** | Baixa de Lançamentos - Controle de Concorrência |
| **Situação/Requisito:** | Quando dois usuários tentam fazer a baixa de lançamentos ao mesmo tempo, seja pelo processos de baixa manual, baixa por retorno bancário, baixa por importação, emissão de cheque, acordo, Borderô, desconto duplicata ou integrações, estava ocorrendo baixas duplicadas |
| **Solução/Implementação:** | Foi implementado o controle de concorrência no qual o usuário que tentar efetuar a baixa primeiro, irá bloquear o lançamento até que o processo seja concluído.  Caso por algum motivo inesperado na execução do serviço (Queda de energia, queda de Host, Etc), o lançamento fique bloqueado, foi criado o processo “Utilitários |Ajuste na Base| Corrigir Lançamentos Bloqueado por concorrência” para que o mesmo seja desbloqueado e seja possível efetuar a baixa novamente |
| **Conversores e Parâmetros:** | Criado o Parâmetro "Controle de concorrência na baixa de lançamentos" disponível em "Ambiente | Parâmetros | TOTVS Gestão Financeira | 02.01 - Contas a Prgar | 02.01.02 - Baixa | 02.01.02.01 - Manutenção de baixa | Baixa 2/5" |
| **Tickets relacionados:** | FINANCEIRO01-111  FINANCEIRO01-121  FINANCEIRO01-552  FINANCEIRO01-74 |
| **Requisito:** | N/A |

divs
