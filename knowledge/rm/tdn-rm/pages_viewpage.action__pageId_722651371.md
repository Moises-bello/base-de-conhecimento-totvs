---
content_hash: 6f4986250342d52bca501a7518e0fa69c10269ed1db1a543af8aa835168fbbe6
fetched_at: '2026-06-29T00:11:27.361633+00:00'
page_id: '722651371'
product: rm
source: tdn-rm
title: FISCAL01-18931 - DT - EFD Contribuições - C170 campo 4 - Considerar a descrição
  do produto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=722651371
version: 4
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | EFD Contribuições |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado): | FISCAL01-18931 |

## **02. SITUAÇÃO/REQUISITO**

A geração do arquivo da EFD Contribuições deve considerar a descrição informada no campo "Descrição do produto do fornecedor" do Item do Lançamento Fiscal de Entrada para a geração do Registro C170 campo 4.

## **03. SOLUÇÃO**

Alteração feita na rotina de geração do registro C170 para considerar o valor do campo Descrição do Produto caso a observação do item não tenha sido preenchida.

Este novo campo só está disponível para Lançamentos de Entrada, portanto a regra não se aplica a Lançamentos de saída.

Disponível a partir da biblioteca 12.1.2205
