---
content_hash: fdcb93b9c1ce611d68c8044a712d2bce67df11e676a9f58858bcb3ba35e0f5f7
fetched_at: '2026-06-29T00:11:27.402772+00:00'
page_id: '723317994'
product: rm
source: tdn-rm
title: FISCAL01-18932 - DT - EFD ICMS IPI - C170 campo 4 - Considerar a descrição
  do produto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=723317994
version: 3
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | EFD ICMS IPI |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado): | FISCAL01-18932 |

## **02. SITUAÇÃO/REQUISITO**

Na geração do arquivo da EFD ICMS IPI deve ser considerada a descrição do produto/serviço preenchida no campo "Descrição do produto do fornecedor" no item do Lançamento Fiscal, em lançamentos de entrada, para a geração do Registro C170 campo 4.

## **03. SOLUÇÃO**

Alteração feita na rotina de geração do registro C170, campo 04, do SPED Fiscal para considerar o valor do campo "Descrição do Produto do Fornecedor" caso esteja preenchido ou a observação do item caso o campo de descrição do produto não esteja preenchido.

Disponível a partir da biblioteca 12.1.2205
