---
content_hash: e0d2f882b40b9131be90fb3adb646d5124bbc2f274e01b276b044e9fb4cdbad7
fetched_at: '2026-06-29T00:08:27.524739+00:00'
page_id: '271415274'
product: rm
source: tdn-rm
title: 96211 MRH-102 DT Diferenca 1 Centavo TRCT
type: documentation
url: https://tdn.totvs.com/display/LRM/96211+MRH-102+DT+Diferenca+1+Centavo+TRCT
version: 111
---

# DIFERENÇA DE 1 CENTAVO NO RELATÓRIO DO TRCT

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *TRCT* |
| **Situação/Requisito:** | Na geração do relatório do TRCT está exibindo o conteúdo do campo "Valor Líquido" com uma diferença de 1 centavo com o valor lançado no envelope no evento de CC 150 - LÍQUIDO DE RESCISÃO. |
| **Solução/Implementação:** | Alterar o tratamento de arredondamento do valores gravados na tabela PFFERRESCTRCT, para evitar diferenças entre o relatório e os valores lançados no envelope de rescisão. |
| **Tickets relacionados:** | 96211 |

divs
