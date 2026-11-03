---
content_hash: e1d3ca876acc2ad9f0e1a093c82c02d8249e3de6dcb8dee0c0ba29479e759512
fetched_at: '2026-06-29T00:08:12.210140+00:00'
page_id: '243639501'
product: rm
source: tdn-rm
title: TVDHLO_DT_Rastreabilidade
type: documentation
url: https://tdn.totvs.com/display/LRM/TVDHLO_DT_Rastreabilidade
version: 115
---

# Rastreabilidade lançamento financeiro

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e projetos* |
| **Módulo:** | *Folha de pagamento* |
| **Função:** | *Rastreabilidade lançamento financeiro* |
| **Situação/Requisito:** | Ao gerar a Guia de INSS com Lançamento Financeiro rateado por Centro de Custo, é feito uma Rastreabilidade por Funcionário incorreta na tabela PFITEMLAN.  Quando uma funcionária está de Licença Maternidade, o sistema deveria levar o valor de abatimento do Salário Maternidade para a tabela PFITEMLAN na própria chapa da funcionária porém o valor de abatimento é proporcionalizado entre todos os funcionários da Filial, causando uma inconsistência em todos os valores ao comparar a PFITEMLAN com PFFINANC. |
| **Solução/Implementação:** | Ajuste realizado para que o Folha de Pagamento volte a gravar na rastreabilidade do lançamento financeiro da guia de INSS para funcionários com valores negativos, para que seja possível ao cliente visualizar qual chapa teve valor negativo, mantendo consistência com valores ao se comparar a PFITEMLAN com PFFINANC |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TVDHLO |
| **Requisito (ISSUE):** |  |

divs
