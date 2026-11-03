---
content_hash: 11f1c915bf03768ca0631d5d3597be26c78e0d2936ceab416bc0bd0d873da0c0
fetched_at: '2026-06-29T00:08:09.086660+00:00'
page_id: '239022887'
product: rm
source: tdn-rm
title: TUYRUD_DT_Cadastro_Funcionario_Transferido
type: documentation
url: https://tdn.totvs.com/display/LRM/TUYRUD_DT_Cadastro_Funcionario_Transferido
version: 116
---

# Cadastro Funcionário Transferido

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e projetos* |
| **Módulo:** | *Folha de pagamento* |
| **Função:** | Cadastro Funcionário |
| **Situação/Requisito:** | Funcionário transferido não abre o cadastro, ocorre o erro: Valor era muito grande ou muito pequeno para Int16. |
| **Solução/Implementação:** | Ajuste de conversão de código de pessoa quando funcionário transferido. Código de pessoa ultrapassava o valor máximo para variável Int16. |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TUYRUD |
| **Requisito (ISSUE):** |  |

divs
