---
content_hash: f76fbc512c4bd04a05c4411de6281077470354ca177d3d37bf8143885ee1f07a
fetched_at: '2026-06-29T00:11:10.554142+00:00'
page_id: '644002643'
product: rm
source: tdn-rm
title: TU - FISCAL01-16723 - Erro Registro E240
type: documentation
url: https://tdn.totvs.com/display/LRM/TU+-+FISCAL01-16723+-+Erro+Registro+E240
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | SPED Fiscal |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-16723 |

## **02. SITUAÇÃO/REQUISITO**

Ao gerar o registro E240 do Sped fiscal, o campo 5 (subsérie) é preenchido com valor 0 e ao validar o SPED é apresentada a mensagem:  
Se código do modelo do registro for igual a 63 ou 65, o campo COD\_PART(Código do Participante) não deve ser informado. Caso seja 63, o campo COD\_ITEM também não deve ser informado. Caso seja 55, 57, 63, 65 ou 67, o campo SUB (Subsérie) também não deve ser informado. Os demais campos devem manter sua obrigatoriedade original.

TESTES REALIZADOS

Foi inserido um Lançamento de Entrada, modelo de documento 57, e utilizado um CFOP com Regra de ICMSST e com a flag "Ressarcimento" marcado e assim, inserido um código de ajuste, na aba AJUSTE SPED do Lançamento Fiscal.

Em lançamento de Outros Débitos/Créditos, foi inserido um Debito de ICMSST e subtipo Ressarcimento ST e também informado valor e código de ajuste.

Na aba de Referencia, foi referenciado o lançamento de entrada citado anteriormente.

Ao gerar a rotina, no Registro E240 o campo 5 é preenchido com o valor “0” e ao validar o arquivo a inconsistência foi apresentada.

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| E240 | GC00013 | 57 | 1 | 0 | 000006555 | 24092021 | 01.01 | 200,00 |

## **03. SOLUÇÃO.**

O problema foi resolvido alterando o campo SUB da classe RegistroE240 para permitir null
