---
content_hash: 1211ba46f79a7b221bc0a87c5a6cab870c5c7b1d7eaf0632d12475717b1aee2f
fetched_at: '2026-06-29T00:11:26.155836+00:00'
page_id: '715826740'
product: rm
source: tdn-rm
title: 'FISCAL01-18702 - Ticket #14925869 - DT - Simples Nacional - Anexo 4 - Desconsiderar
  ISS'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=715826740
version: 3
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Simples Nacional |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-18795 |

## **02. SITUAÇÃO/REQUISITO**

Cliente do simples nacional, anexo IV, contém dois cenários de apuração, um normal e um com retenção do ISS.

Para notas de serviços prestados que contém a linha do ISS o mesmo não deve compor o cálculo da alíquota do tipo de tributo Simples Nacional ( a alíquota de repartição).

## **03. SOLUÇÃO**

Os campos de ST do cadastro de Combinações de Situações Tributárias não estavam sendo utilizados após o ano de 2018, para atender a necessidade do cliente e deixar o sistema apto a atender a futuras necessidades do mesmo tipo, passaremos a utilizar novamente os campos, o tributo que estiver selecionado vai ter sua alíquota desconsiderada no Cálculo do Percentual de Repartição.

A alteração é válida para Cenários criados a partir do mês 10/2022, os cadastros realizados antes do mês 10/2022 não serão afetados mesmo que os campos estejam marcados.

IMAGEM

Disponível a partir da biblioteca 12.1.34
