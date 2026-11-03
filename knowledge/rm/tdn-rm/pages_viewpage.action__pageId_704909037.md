---
content_hash: b9e9a5c5e16c6c282cffe40fc0f6af6841a3c4a29827f830ba7172b348a4ac36
fetched_at: '2026-06-29T00:11:22.430400+00:00'
page_id: '704909037'
product: rm
source: tdn-rm
title: Aprovação cotação via TAA (TOTVS Aprovações e Atendimentos)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=704909037
version: 16
---

Atenção

Recurso disponível na release 12.1.2209 ou superior.

## **01. OBJETIVO**

Para as empresas que usam **fluxo de aprovação**, é necessário que o **gestor** tenha uma visão geral da **negociação** de preço de cada **compra**, desta forma ele terá condições de tomar a decisão de aprovar ou não a compra, antes mesmo da geração da ordem de compra.

O nosso objetivo com este recurso é disponibilizar um controle na cotação, permitindo que a **ordem de compra** seja gerada apenas para **cotações aprovadas**.

## **02. PARAMETRIZAÇÃO**

A utilização da **aprovação** no processo de cotação é **opcional**, mas a partir do momento que a coligada for parametrizada para utilizar o recurso, **todas** as cotações deverão passar pelo processo de aprovação através do **TOTVS Aprovações e Atendimentos**.

Gestão de Compras > Cotação > Definições Gerais 6/6

Parâmetro

- **Coligada do Atendimento**: É possível selecionar uma Coligada diferente da qual o movimento será gerado para ser aprovado no TOTVS Gestão de Relacionamento com o cliente. Neste caso o movimento poderá ser gerado na coligada 1, e o atendimento aprovado na coligada 2, por exemplo.

- Os demais campos definem qual Tipo de Atendimento será utilizado para a aprovação do movimento.

## **02. PROCESSO APROVAÇÃO**

O processo de aprovação é utilizado, quando o comprador concluiu o processo de 

* Todas as cotações nascem sem status de aprovação.
* Só será possível enviar uma nova aprovação para as cotações sem status de aprovação ou com a última aprovação reprovada.

Para realizar o processo selecione a cotação e acesse Processos\Aprovação de Cotação, conforme tela abaixo:

## **03. FLUXO DE APROVAÇÃO**

O fluxo de aprovação no **TOTVS Aprovações e Atendimentos**, pode ser criado com quantas etapas forem necessárias para atender as necessidades de cada empresa, mas é importante se atentar para **ação** definida na última **etapa**.

Para o fluxo de aprovação **aprovada**, a última etapa deve ter a ação **Concluído Confirmado**.

Para o fluxo de aprovação **reprovada**, a última etapa deve ter a ação **Cancelado**.

Para mais informações acesse

## **04. PROCESSOS AFETADOS**

**Alterar cotação**

* Apenas cotações que não iniciaram o processo de aprovação ou aprovação reprovada podem ser alteradas.
* Caso o comprador precise realizar alguma alteração na cotação que iniciou o processo de aprovação, será necessário cancelar aprovação. Desta forma o atendimento gerado será cancelado permitindo realizar alterações, e depois de finalizada as alterações, deve-se gerar uma nova aprovação.

**Cancelar cotação**

* Caso o comprador deseje cancelar uma cotação que iniciou o processo de aprovação, todos as aprovações (atendimentos) também serão cancelados.

**Excluir cotação**

* Cotação que foram previamente canceladas podem ser canceladas

## **04. TABELAS UTILIZADAS**

* TCCOTACAOATEND - Tabela responsável pelas informações dos atendimentos relacionados a cotação

Informações

Esta disponível o relatório "**CRMREL0017 - Work Flow Minhas Aprovações - Cotação**" a partir da versão 12.1.2310, para ser utilizado no processo de aprovação.

Para mais informações clique [aqui](https://tdn.totvs.com/pages/releaseview.action?pageId=607612620#tudo-sobre-funcionalidades-interfaces)
