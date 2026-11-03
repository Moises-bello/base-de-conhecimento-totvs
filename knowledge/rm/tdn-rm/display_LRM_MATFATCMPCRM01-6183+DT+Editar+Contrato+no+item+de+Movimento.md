---
content_hash: 68478f4c0cc4041c6c75d8644668dce418d07de91ad9d7308182218cf492b64c
fetched_at: '2026-06-29T00:09:53.830769+00:00'
page_id: '442044535'
product: rm
source: tdn-rm
title: MATFATCMPCRM01-6183 DT Editar Contrato no item de Movimento
type: documentation
url: https://tdn.totvs.com/display/LRM/MATFATCMPCRM01-6183+DT+Editar+Contrato+no+item+de+Movimento
version: 2
---

# Editar Contrato no Item de Movimento

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | BackOffice |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | Movimento | MovMovimentoBaseAction | |
| **Cadastros Iniciais:** | Movimento |
| **Parâmetro(s):** | Parâmetros → Gestão de Estoque, Compras e Faturamento → Tipo de Movimento → Projeto |
| **Ponto de Entrada:** | N/A |
| **Tickets relacionados** | N/A |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | MATFATCMPCRM01-6183 |
| **País(es):** | Brasil |
| **Banco(s) de Dados:** | SQLServer e Oracle |
| **Tabelas Utilizadas:** | TTMVEXT |
| **Sistema(s) Operacional(is):** | Windows |
| **Pacote:** | 12.1.23 |

## Descrição

Implementação do parâmetro responsável por definir a regra de visibilidade do campo "Contrato", localizado na tela de edição do item de movimento "Aba Integrações → Projetos".

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *12.1.23*.

## Procedimento para Utilização

* A parametrização pode ser realizada através dos **Parâmetros → Gestão de Estoque, Compras e Faturamento → Tipo de Movimento → Projeto** e informar o campo**Editar Contrato no Item******.****

Ao definir o parâmetro **Editar Contrato no Item**como **Edita** ou **Mostra**, o campo **Contrato** será habilitado na tela de edição do item de movimento.
