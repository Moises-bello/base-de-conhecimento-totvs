---
content_hash: 77ab0e95707f9a85eb0d5b9edd4a56a479ce8cb768ac5d47378ee29b65f38b18
fetched_at: '2026-06-29T00:09:58.169764+00:00'
page_id: '451267437'
product: rm
source: tdn-rm
title: MATFATCMPCRM01-6453 DT Remessa Parcelada de Exportação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=451267437
version: 4
---

# REMESSA PARCELADA DE EXPORTAÇÃO

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Backoffice. |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | VEN.003 | MOVIMENTO DE EXPORTAÇÃO | |
| **Cadastros Iniciais:** |  |
| **Parâmetro(s):** |  |
| **Ponto de Entrada:** |  |
| **Tickets relacionados** | [3875653](https://totvssuporte.zendesk.com/agent/tickets/3875653 "Open ticket in Zendesk Support") |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | MATFATCMPCRM01-6453 |
| **País(es):** | Bta |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Tabelas Utilizadas:** | TITMVINCEXPORTACAO |
| **Sistema(s) Operacional(is):** | - |
| **Pacote:** |  |

## Descrição

Implementação da possibilidade de vinculo de Movimentos de Exportação, em outros movimentos de Exportação para geração de Remessa Parcelada de Exportação.

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação de um dos pacote de atualizações abaixo:

* 12.1.24 ou superiores.

## Procedimento para Utilização

Caso seja necessário a geração de Notas de Remessa Parcelada de Exportação, o vinculo dessa nota com a Nota de Exportação deve ser realizado também pela pela tela de **Relac. Mov. Exportação.**

**1) PARAMETRIZAÇÃO**

* Para parametrizar um tipo de movimento como Movimento de Remessa Parcelada de Exportação vá até os parâmetros do Tipo de Movimento, na etapa **Fis - Dados** e marque a opção **Movimento de Remessa Parcelada de Exportação.**

**2) MOVIMENTO**

Após a  parametrização, o Movimento de Remessa Parcelada pode ser gerado. Nesse movimento, deve-se vincular os Itens do Movimento de Exportação original que compõe aquela Remessa Parcelada. Assim, na tela de **Relac. Mov. Exportação** deve-se seguir os seguintes passos,:

* O Movimento de Remessa Parcelada deve possuir o mesmo Cliente do Movimento de Exportação
* Assim, o sistema irá exibir somente Movimentos de Exportação (CFOP = 7), movimentos do Tipo 2.2. e Mesmo cliente/Fornecedor do movimento para serem vinculados.
