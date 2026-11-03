---
content_hash: 8b352053fd2acf80ffa85820ad0a4336a0bfe9bd4069bb2272f8ae5d0af43bc1
fetched_at: '2026-06-29T00:08:52.327705+00:00'
page_id: '338380675'
product: rm
source: tdn-rm
title: 1519972 MATESTCNTFTOF01-1375 DT Apresentar os campos XPED/ NITEMPED no Movimento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=338380675
version: 17
---

# APRESENTAR OS CAMPOS XPED/ NITEMPED NO MOVIMENTO

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Linha de Produto:** | RM. | | |
| ****Segmento Executor:**** | Construção e Projetos. | | |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento. | | |
| **Rotina:** | |  |  | | --- | --- | | **Rotina(s) envolvida(s)** | **Nome Técnico** | | Movimento | MovMovimentoAction | | Parâmetros do Movimento | RMSParamsWizardAction | | | |
| **Ticket:** | 1519972. | | |
| **Requisito (ISSUE):** | MATESTCNTFTOF01-1375 e MATESTCNTFTOF01-2217. | | |
| **País:** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros:** | [Fiscal - Dados Fiscais.](http://wikihelp.totvs.com.br/WikiHelp/EST/EST.Fiscal.aspx) | | |

## Objetivo

Criação de parâmetro no TOTVS Gestão de Estoque, Compras e Faturamento que permite configurar o comportamento dos campos XPED e NITEMPED em um movimento de pedido e de nota fiscal.

## Definição da Regra de Negócio

Atualmente os campos **Número do Pedido (TITMMOVFISCAL.NUMPEDIDO) e Item do Pedido (TITMMOVFISCAL.NUMITEMPEDIDO)** são apresentados em movimentos que possuem o modelo de documento igual a 55 e que estejam parametrizados para gerar escrituração.

Foi criado a possibilidade de que esses campos **sejam apresentados em movimento de pedido (não escritura)**, uma vez que o pedido é a origem da NF-e. Foi habilitado também a possibilidade de parametrizar o comportamento desses campos em um movimento de NF-e.

É necessário parametrizar o movimento para que os campos de pedido sejam exibidos. **Apenas movimentos do tipo 1.1, 2.1, 1.2 e 2.2 têm essa possibilidade**.

Para manter o comportamento da parametrização dos movimentos de NF-e foi acrescentada uma consistência que não permite parametrizar o tipo de movimento como **Não Edita** no parâmetro criado, caso ele tenha **tipos de documentos que possuem o modelo de documento igual a 55 - NF-e**. Se este cenário ocorrer, a mensagem abaixo será apresentada em movimentos do grupo [1.1, 2.1, 1.2, 2.2].

**Tabelas Utilizadas**

* TTMVEXT- Tipos de Movimentos.
* TITMMOVFISCAL - Dados Fiscais do Item de Movimento

### Procedimento para Utilização

Não se aplica.

## Procedimento para Configuração

**CONFIGURAÇÃO DE PARÂMETROS**

1. É necessário parametrizar o movimento para que os campos de pedido sejam exibidos.

   O parâmetro pode ser acessado em “Etapa Fis – Dados”, campo “Editar Número do Pedido” que deve ter a opção de ser definido como [Não Edita, Mostra, Edita].
