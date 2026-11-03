---
content_hash: 79ea4fc759a32ddfc50a742b3e9890a8e567b5ef28a14506e79b1446f152e804
fetched_at: '2026-06-29T00:12:07.436143+00:00'
page_id: '925358774'
product: rm
source: tdn-rm
title: DT - S-1210 - Gerar XML para Residente Exterior verificando a validade
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+S-1210+-+Gerar+XML+para+Residente+Exterior+verificando+a+validade
version: 10
---

## **01. DADOS GERAIS**

| Produto: | TOTVS |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: |  |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | S-1210 - Gerar XML para Residente Exterior verificando a validade |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-13189](https://jiraproducao.totvs.com.br/browse/DRHROTRM-13189) |

## **02. LIBERAÇÃO**

**Lembrando que, será a partir dos patches:**

* 12.1.2406.250
* 12.1.2410.194
* 12.1.2502.114 e superiores

## **03. SITUAÇÃO/REQUISITO**

O produto deverá gerar o evento S-1210 verificando a validade dos dados do Residente no Exterior.

## **04. SOLUÇÃO**

Adequação do produto para que, na geração do XML do evento S-1210, o sistema valide se a data de pagamento dos eventos no envelope está dentro do período de validade do cadastro do residente no exterior. Caso esteja, serão impressas as respectivas tags. Confira o exemplo abaixo:

Em Administração de Pessoal l Funcionário l Anexos l Folha de Pagamento l Dados do Residente ou Domiciliado no Exterior e informado o período:

**Exemplo 1:**

 Em Administração de Pessoal l Funcionário l Anexos l Movimento | Envelope de Pagamento foi calculado o Envelope do funcionário com data de pagamento 12/2024:

 Ao gerar o XML do evento S-1200 o sistema irá preencher os dados do Residente no Exterior:

**Exemplo 2:**

Emdados do Residente ou Domiciliados no exterior o funcionário tem 2 cadastros com vigencias diferentes.

Periodo 1: Eventos com data de pagamento  30/12/2024 - Fora da competencia Atual

 Periodo 2:  Evento com data de pagamento na competencia Atual

Gerando o S-1210 para competência Atual 

A tag `<endExt>` não será impressa nos seguintes casos:

* O anexo "Dados do Residente ou Domiciliado no Exterior" do funcionário não estiver preenchido.
* A data de pagamento dos eventos no envelope do funcionário estiver fora do período cadastrado nos "Dados do Residente ou Domiciliado no Exterior" (Data Início e Data Fim).
