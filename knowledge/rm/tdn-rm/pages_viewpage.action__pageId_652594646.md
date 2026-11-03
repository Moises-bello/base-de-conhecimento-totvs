---
content_hash: 86accbac57e90513db3fc2df147c729dd51e13d504361f35a313bb89169cd161
fetched_at: '2026-06-29T00:11:12.426412+00:00'
page_id: '652594646'
product: rm
source: tdn-rm
title: FISCAL01-17018 - Codificação - Código de barras no registro 0220
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=652594646
version: 2
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | SPEED |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-17018 |

**02. SITUAÇÃO/REQUISITO**

     Inclusão do código de barras no Registro 0220Deverá ser incluído o código de barras na geração do registro 0220

## **03. SOLUÇÃO**

O Problema foi resolvido acrescentando o campo CodigoBarrasLancamento na classe FisProdutoCxt, populando ele na linha 5376 da classeSped.Context, e utilizando o mesmo para gerar o 0220 no método InsereFatorConversao da classeSped.Module.Bloco0.Alémdisso,foi acrescentado uma lógica para que datas posteriores a 31/12/2021 seja gerado o campo no arquivo e para que datas anteriores a 01/01/2022 não seja gerado
