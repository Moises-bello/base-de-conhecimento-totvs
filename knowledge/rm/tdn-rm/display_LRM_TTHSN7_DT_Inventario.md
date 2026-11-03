---
content_hash: 7b6a4cbc3680f61b7ac46874fd40b10c48537f875d31885c4a95038752f76107
fetched_at: '2026-06-29T00:06:12.934578+00:00'
page_id: '205922031'
product: rm
source: tdn-rm
title: TTHSN7_DT_Inventario
type: documentation
url: https://tdn.totvs.com/display/LRM/TTHSN7_DT_Inventario
version: 1
---

# Inventário

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Gestão de Estoque, Compras e Faturamento* |
| **Função:** | *Inventário* |
| **Situação/Requisito:** | Quando 2 usuários estão realizando o processo de inventário para o mesmo produto, ex: Usuário 1 altera Contagem 1 e Usuário 2 altera Contagem 2, o sistema considera apenas a  alteração do usuário que salvar o registro por último, fazendo com que as demais informações sejam perdidas. |
| **Solução/Implementação:** | Foi criado um tratamento para evitar problemas de concorrência durante o processo de inventário. |
| **Conversores e Parâmetros:** | *Não se Aplica* |
| **Chamados relacionados:** | *Não se Aplica* |
| **Requisito (ISSUE):** | *Não se Aplica* |
| **Versões/Release:** | *12.1.8* |
| **Versão Corrigida:** | *12.1.7* |
| **Versão Expedida:** | *12.1.7* |

divs
