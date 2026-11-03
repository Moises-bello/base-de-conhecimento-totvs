---
content_hash: 6910a7dd338e70c762734651cd53caaaad4d2fd6a0815bbc03fca0b18e5bde51
fetched_at: '2026-06-29T00:10:36.452047+00:00'
page_id: '532049775'
product: rm
source: tdn-rm
title: 'FISCAL01-11890 DT EFD - Contribuições 2020 - Reg. 1011: 9- Escrituração'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=532049775
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Serviços |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | EFD Contribuições |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11890 |

## **02. SITUAÇÃO/REQUISITO**

### *"Registro 1011: Detalhamento das Contribuições com Exigibilidade Suspensa*

*Deverá ser escriturado pelo menos um registro 1011 para cada uma das ações judiciais escrituradas no registro 1010 que se refira à decisão judicial que autoriza a suspensão da exigibilidade de parte do valor das contribuições, ou de seu valor integral, porém sem o trânsito em julgado."*

**Funcionamento no RM**

No anexo de tributos discutido no cadastro de Processos Judiciais será criado um campo para informar a formula de cálculo da Base de Cálculo, Alíquota e CST do tributo discutido.

No Movimento será criado uma pasta para informar os processos por item, para que sejam informados os processos que discutem os tributos relacionados aquele item.

Durante o processo de escrituração em cada item do Lançamento fiscal será criado uma pasta com o resultado do cálculo do tributo discutido daquele item considerando a fórmula, alíquota e CST informados no cadastro do tributo discutido.

Ao gerar a EFD Contribuições o registro 1011 será gerado com base nos dados dos cálculos gravados nos Lançamentos Fiscais relacionados ao processo informado no registro 1010.

Na issue em questão será tratado o processo escrituração preencher os tributos discutidos e os processos do item.

## **03. SOLUÇÃO**

Ajustado o processo de escrituração para considerar o processo judicial e os tributos discutidos presentes no item de movimento.
