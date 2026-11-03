---
content_hash: b172d119035cfbb3a452f05c3d2ddf1d22fad70926bffea8b425e5b55a85a46f
fetched_at: '2026-06-29T00:12:09.059543+00:00'
page_id: '939232225'
product: rm
source: tdn-rm
title: FISCAL01-25686 - Erro ao calculo CIAP
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-25686+-+Erro+ao+calculo+CIAP
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão de Fiscal |
| Função: | CIAP |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-25686 |

## **02. SITUAÇÃO/REQUISITO**

Ao realizar o cálculo do CIAP para o período de apuração do ICMS, o seguinte erro é apresentado:  
   
Processo de Cálculo do CIAP não Efetuado:  
A cadeia de caracteres de entrada não estava em um formato correto.

Após a migração do CIAP para a nota MDI, a tabela DFILTRONAT é utilizada tanto com os parâmetros do CIAP do delphi (DSUBGRUPOPROCESSO) em versões de mercado (até a 12.1.2502) quando com os parâmetros da nova MDI (DNEWSUBGRUPOPROCESSO). Ambas as tabelas possuem a coluna IDSUBGRUPO, e pode coincidir que esse ID seja igual para as duas formas de geração do cálculo CIAP. Sendo assim, caso houver o IDSUBGRUPO 7 para o parâmetro do CIAP em ambas as tabelas, por exemplo, e tenha natureza preenchida para ambos esses subgrupos, a coluna CAMPO da tabela DFILTRONAT será retornada tanto com números inteiros (nova MDI) quanto com string (delphi), e sua conversão de tipo resultará em erro para o usuário.

## **03. SOLUÇÃO**

Consultas do CIAP passam a verificar se uma coluna de controle (RECCREATEDBY) está nula ou não na DFILTRONAT, pois o Delphi não preenche essas colunas.

Disponível a partir da biblioteca 12.1.2410
