---
content_hash: 55b5e8fa0224e15b7beba887238da34713216deab7c72c186e11fb329b8e77cf
fetched_at: '2026-06-29T00:06:21.995686+00:00'
page_id: '223910488'
product: rm
source: tdn-rm
title: TTD137_DT_GERACAO_RAIS
type: documentation
url: https://tdn.totvs.com/display/LRM/TTD137_DT_GERACAO_RAIS
version: 122
---

# GERAÇÃO RAIS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Geração Rais* |
| **Situação/Requisito:** | *Ao gerar a RAIS em arquivo, dentro dos parâmetros da coligada, aba Seção é marcado o campo "Seção Sindicalizada", porém no arquivo - Registro tipo 1, posição 452, a informação está incorreta. O campo está preenchido com 2 (Não), quando o correto seria 1(Sim).* |
| **Solução/Implementação:** | - Ajuste na rotina da Rais para considerar valor correto para Seção Sindicalizada, respeitando o valor informado. - Ajuste na rotina de Rais para trazer registro de funcionário quando identificado por CEI. Arquivo trazia somente registros das seções. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTD137* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.43* |
| **Versão Corrigida:** |  |
| **Versão Expedida:** |  |

divs
