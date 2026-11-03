---
content_hash: 3c47598098a2810dca44d5455ff52bdfcae73d1eacd8fb85c7e6c6d17eb77d4d
fetched_at: '2026-06-29T00:08:30.921056+00:00'
page_id: '272705922'
product: rm
source: tdn-rm
title: 538632 MATESTCNTFTOF01-5 DT Materiais com saldo de estoque zerado não é listado
  na tela de empenho
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=272705922
version: 113
---

# Materiais com saldo de estoque zerado não é listado na tela de empenho

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Totvs Gestão Planejamento e Controle da Produção |
| **Função:** | Empenho de Materiais |
| **Situação/Requisito:** | Ao promover uma Ordem de Produção de criada para aguardando recursos, foi verificado que os Produtos com saldo de estoque zerado no momento, não foram relacionado na tela de visão de empenho. |
| **Solução/Implementação:** | Foi criado uma Flag para filtrar na visão de empenho os Produtos com Saldo de Estoque zerado. |
| **Conversores e Parâmetros:** | Não se Aplica |
| **Tickets relacionados:** | 538632 |
| **Requisito:** | MATESTCNTFTOF01-5 |

## Descrição

Ao promover uma Ordem de Produção de criada para aguardando recursos, foi verificado que os Produtos com saldo de estoque zerado no momento, não foram relacionado na tela de visão de empenho. Foi então criado uma Flag para filtrar na visão de empenho os Produtos com Saldo de Estoque zerado.

## Procedimento para Utilização

1. Entrar no Menu Produção - Ordem de Produção e escolher o filtro desejado.
2. Selecionar a Ordem de Produção.
3. Clicar em "Empenho de Matéria Prima da Ordem Selecionada.

Neste momento irá aparecer a Visão de Empenho. Pode-se notar, abaixo da grid, que foi criado um Check Box com a descrição "Exibir produtos sem Saldo Disponível. Este Check Box irá controlar a exibição ou não dos Produtos com Estoque zerado.

Observação: Dentro os locais possíveis parametrizados, ele irá mostrar o saldo disponível, mesmo que o produto não tenho saldo neste local nem movimentação.

divs
