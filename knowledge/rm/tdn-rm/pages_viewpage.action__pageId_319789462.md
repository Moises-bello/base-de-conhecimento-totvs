---
content_hash: 9ecd3656d7d909fc41216072ca94f0de915894f36ea7f4aa00ff0158933e65c5
fetched_at: '2026-06-29T00:08:47.660750+00:00'
page_id: '319789462'
product: rm
source: tdn-rm
title: ER MATESTCNTFTOF01-1147 Tributação Cupom Fiscal por Filial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=319789462
version: 95
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Estoque, Compras e Faturamento | **Módulo** | RM |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | MATESTCNTFTOF01 | **IRM/EPIC1** |  |
| **Requisito/Story/Issue1** | MATESTCNTFTOF01-1147 | **Subtarefa1** | NA |
| **Chamado/Ticket2** | NA | | |
| **País** | Brasil | | |
| **Outros** | NA | | |

## 

## Objetivo

Devido algumas particularidades da legislação de ICMS, existe a possibilidade de um mesmo produto ser taxado de formas diferentes para uma mesma operação de venda em filiais distintas da mesma UF. Devido a isso, será necessário ajustar o sistema para que seja possível informar a tributação de cupom fiscal por filial, visto que atualmente é possível informar apenas um tipo de tributação por produto.

## 

## Definição da Regra de Negócio

1. Cadastro de Produto - Informações por Filial

Será necessário criar o campo "Tributação Cupom Fiscal" (TPRDFIL.TRIBUTACAOECF) na tela de Informações por Filial. Esse campo deverá ser um lookup que retornará os dados do cadastro fiscal **Tributação de Cupom Fiscal** (TTRIBUTACAOECF). Esse campo deverá ser salvo por filial e poderá vazio.

2. Envio de informações para o SIGALOJA

Ao fazer o envio das informações do produto para o SIGALOJA, deverá ser verificado para se existe Tributação ECF informada por filial (TPRDFIL.TRIBUTACAOECF). Se existir, essa informação é que deverá ser enviada para o SIGALOJA, caso contrário, deverá ser enviada a informação preenchida no cadastro do produto (TPRODUTODEF.TRIBUTACAOECF). Essa tratativa deve ser feita inclusão, edição e exclusão de produtos.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [ACAA040 – Parâmetros] | [Alteração] | [Atualizações -> Acadêmico-> Tesouraria] | - |
| [ACAA050 – Negociação Financeira] | [Envolvida] | [Atualizações -> Acadêmico-> Tesouraria] | - |
| [ACAA060 – Cadastro de Pedidos] | [Criação] | [Atualizações -> Acadêmico-> Cadastros] | - |

**Tabelas Utilizadas**

* TPRDFIL - Informações de Produto por Filial
* TPRODUTODEF - Dados dos Produtos Globais por Coligada

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
