---
content_hash: 8941583061d73d8fc87003ceed507aae60c24f90151676c1a6efef545b6a2ae5
fetched_at: '2026-06-29T00:09:50.771719+00:00'
page_id: '435112936'
product: rm
source: tdn-rm
title: MATFATCMPCRM01-5782 DT Filial e Local de estoque no Orçamento da cotação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435112936
version: 18
---

ilial e Local de estoque no Orçamento da cotação

# Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Backoffice |
| **Módulo:** | Gestão de Estoque, Compras e Faturamento |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | |  | Orçamento da Cotação | |
| **Cadastros Iniciais:** | . |
| **Parâmetro(s):** | . |
| **Ponto de Entrada:** | . |
| **Tickets relacionados** | MATFATCMPCRM01-5782 |
| **Requisito/S****tory/Issue (informe o requisito relacionado):** | MATFATCMPCRM01-5782 |
| **País(es):** | Bra |
| **Banco(s) de Dados:** | SQL Server e Oracle |
| **Tabelas Utilizadas:** | TCORCAMENTO |
| **Sistema(s) Operacional(is):** | . |
| **Pacote:** | . |

## Descrição

Implementação de Filial e Local de Estoque no Orçamento da Cotação

## Procedimento para Implantação

O sistema é atualizado logo após a aplicação do pacote de atualizações *12.1.23* deste chamado

## Procedimento para Utilização

## **1. Parametrização:**

Para se utilizar a **Filial e o Local de Estoque no Orçamento/Negociação da Cotação**, é necessário acessar os Parâmetros da Cotação em **Parâmetros → Gestão de Estoque, Compras e Faturamento → 04.06 - Gestão de Compras → 04.06.02 - Cotação → Definições Gerais 3/5** e informar o campo **Utiliza Filial/Local de Estoque no Orçamento/Negociação** com valor igual a **Utiliza do Orçamento** ou ****Utiliza do Orçamento Obrigatoriamente.****

O mesmo parâmetro estará contido também na parametrização da Cotação de cada Filial.

Ao parametrizar, serão exibidos novos campos para informar **Filial e Local de Estoque** na tela de **Registrar Orçamento/Negociação** por fornecedor.

**2. Regras Importantes:**

**2.1. Registro de Orçamento:**

**2.1.1.** Os campos **Filial e Local de Estoque** serão habilitados somente quando for parametrizado uma das opções:**“Utiliza do Orçamento” ou “Utiliza do Orçamento Obrigatoriamente”;**

**2.1.2**. Quando parametrizado uma das opções “**Utiliza do Orçamento**” ou **“Utiliza do Orçamento Obrigatoriamente**”, os default's de **Filial e Local de Estoque** serão preenchidos no **Orçamento** da cotação desde que a(s) solicitação(s) sejam de uma mesma Filial. Caso negativo os campos serão apresentados em branco;

**2.1.3.** Para cotação de solicitações de duas ou mais coligadas(**Central de Compras**)**,** os campos **Filial e o Local de Estoque,** não serão apresentados no **Orçamento/Negociação.**

## **2.2. Registro de Negociação:**

Os dados informados no **Orçamento**serão copiados para a **Negociação,**e caso, necessário podem sofrer alterações pelo usuário na tela de negociação;

**Importante: Coligadas parametrizadas para trabalhar como Central de Compras não serão apresentados os campos Filial e Local de Estoque na Negociação.**

**2.3. QCP(Quadro Comparativo):**

**2.3.1** Quando definido **Filial e Local de Estoque** no **Orçamento/Negociação,** os cálculos serão realizados de acordo com o estado da Filial informada;

**2.3.2** Caso o Quadro Comparativo já tenha sido gerado e a **Filial** do **Orçamento/Negociação** for preenchida posteriormente, o mesmo será recalculado.

**2.4. Geração Ordem de Compra:**

Se preenchido **Filial** e **Local de Estoque** no Orçamento/Negociação, a Ordem de compra será gerada para a Filial correspondente;

**Importante: O default de local de estoque não será aplicado quando o sistema estiver parametrizado para utilizar local de estoque por item.**

**2.5. Novos Campos:**

Foram criados os campos **CODCOLFILIALNEG**, **CODFILIALNEG** e **CODLOCNEG** na tabela **TCORCAMENTO,** para que sejam gravados os valores referente a **CODFILIAL** e **CODLOC** da tela de **Negociação**.
