---
content_hash: 3d4781f194650c374da17c41b66ae77433febb268174b551e5bf7ec302bea053
fetched_at: '2026-06-29T00:11:25.617366+00:00'
page_id: '714215193'
product: rm
source: tdn-rm
title: FISCAL01-18543 - DT DCTF - Código de Variação DARF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=714215193
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | DCTF |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-18543 |

## **02. SITUAÇÃO/REQUISITO**

No cadastro dos tributos, o campo variação permite apenas um dígito, porém é necessário o cadastro de dois dígitos  
conforme tabela de códigos da receita federal, onde alguns tributos possuem a variação com mais de um dígito, exemplo IRPJ: 0220/12.

## **03. SOLUÇÃO**

Alterado o tamanho do campo “Variação” do cadastro de tributo para permitir o preenchimento de dois dígitos ao invés de um,  
para correta geração da DCTF.

Disponível a partir da biblioteca 12.1.34
