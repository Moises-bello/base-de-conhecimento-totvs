---
content_hash: 756e8e2efc13c884c6d3a1299af110b797ffe30e40eff9d088833e314e8b6d6d
fetched_at: '2026-06-29T00:09:11.726642+00:00'
page_id: '415705671'
product: rm
source: tdn-rm
title: MATFATCMPCRM01-5518 DT Movimento de Remessa Simbólica de Exportação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=415705671
version: 4
---

# Movimento de Remessa Simbólica de Exportação

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Construção e Projetos |
| **Módulo:** | Totvs Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | MOV.035 | ITEM DE MOVIMENTO | |
| **Cadastros Iniciais:** | - |
| **Parâmetro(s):** | - |
| **Ponto de Entrada:** | - |
| **Tickets relacionados** | MATFATCMPCRM01-5518 / MATFATCMPCRM01-5498 |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | MATFATCMPCRM01-5518 / MATFATCMPCRM01-5498 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQL Server / Oracle |
| **Tabelas Utilizadas:** | TTMVEXT, TITMVINCEXPORTACAO |
| **Sistema(s) Operacional(is):** | . |
| **Pacote:** | . |

## Descrição

Implementação para permitir inclusão de Movimento de Remessa Simbólica de Exportação.

O emissor da Nota de Exportação precisa informar as notas de Remessa que estão vinculadas a essa exportação. Porém, no caso onde as notas de Exportação foram emitidas por um terceiro, o emissor da Nota precisa, mesmo assim, vincular as notas emitidas por esse terceiro na exportação.

A implementação descrita abaixo, ensina como criar um Movimento "Simbólico" para uma nota emitida por um terceiro, de forma a permitir que essa nota seja vinculada no Movimento de Exportação.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de um dos seguintes pacotes de atualizações:

* 12.1.20.395 ou
* 12.1.21.140 ou
* 12.1.22.108 ou
* 12.1.23 e superiores

## Procedimento para Utilização

Para parametrizar o Movimento de Remessa simbólica de exportação, siga os seguintes passos:

* Acessar o **Gestão de Estoque, Compras e Faturamento → Ambiente → Parâmetros → Gestão de Estoque, Compras e Faturamento**, selecionar o Tipo de Movimento, ir na etapa **Fis - Dados** e marcar a opção **Remessa de Terceiros para Formação de Lote Simbólico.**
* Esse movimento também deve ser parametrizado para utilizar Natureza de operação.
* É importante lembrar que esse Movimento tem a intenção de ser simbólico, e portanto não deveria possuir as seguintes opções:
  + Integração com o Financeiro
  + Integração com a Contabilidade
  + Tributos
  + Preços
  + Faturamento
  + Escrituração
* Ao marcar esse campo será habilitado, nesse movimento, o campo para que seja informado o Tipo de Documento a que se refere esse Movimento simbólico. Deve-se informar também, a Natureza de Operação.
* E também será habilitado o campo Chave de Acesso para se informar a chave de acesso do documento fiscal - normalmente uma Nota Fiscal Eletrônica.
* Por fim, deve-se informar os itens da Nota de Remessa com as quantidades correspondentes.
* **IMPORTANTE: Deve-se gerar um movimento de remessa simbólica para CADA nota fiscal de Remessa emitida por terceiros.**
* Assim, um movimento gerado a partir dessa parametrização, aparecerá na tela de **Relac. Mov. Exportação** do Movimento para Gerar a Nota Fiscal de Exportação. como disponível para ser vinculado.
