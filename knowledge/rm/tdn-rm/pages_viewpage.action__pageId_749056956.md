---
content_hash: 7411ba64a509dc5bd1bf89e3634e450c6ad6e1dde0b35b41a66343d6839bcd2b
fetched_at: '2026-06-29T00:11:32.783600+00:00'
page_id: '749056956'
product: rm
source: tdn-rm
title: FISCAL01-19599 - DT -  Geração do registro Mestre do Convênio 115
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=749056956
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Rotinas Estaduais |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-19388 |

## **02. SITUAÇÃO/REQUISITO**

Será necessário alterar o processo de geração da CAT 79/Convênio ICMS 115, para que o registro Mestre seja gerado considerando os campos **Data Leitura** e **Data Leitura Anterior**, para os Modelos de Documento 6, 21 e 22.

## **03. SOLUÇÃO**

O registro Mestre será gerado preenchendo os campos  **Data Leitura** e **Data Leitura Anterior**, para os Modelos de Documento 6, 21 e 22, com base na pasta **Energia/Comunicação**, campos **Data Leitura** e **Data Leitura Anterior** de cada Lançamento Fiscal. Além disso, o fato do campo estar em branco não deverá causar erros na execução da Rotina, apenas manter o comportamento atual preenchendo com zeros.

Imagem

Disponível a partir da biblioteca 12.1.2205
