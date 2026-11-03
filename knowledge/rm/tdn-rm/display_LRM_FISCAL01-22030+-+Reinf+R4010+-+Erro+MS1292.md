---
content_hash: 6377d7f06bec5df1671f0b69044f1bac9b03e55b939b879ce46a2b7d1a4242e1
fetched_at: '2026-06-29T00:11:48.659601+00:00'
page_id: '824918477'
product: rm
source: tdn-rm
title: FISCAL01-22030 - Reinf R4010 - Erro MS1292
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-22030+-+Reinf+R4010+-+Erro+MS1292
version: 2
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | REINF |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-22030 |

## **02. SITUAÇÃO/REQUISITO**

O sistema não gera o campo descRendimento relacionado ao registro rendisento, do evento R4010. Dessa forma ao enviar o registro à Receita e consultar o evento é retornado o erro:   
   
Falha ao processar o evento de identificador 146 e tipo R-4010: O evento foi rejeitado, pelo(s) seguinte(s) motivo(s):   
Código MS1292: A descrição do rendimento isento/não tributavel {descRendimento}, é obrigatória e exclusiva se o tipo de isenção {tpIsencao} for igual a 99. Caso contrario não pode ser informada.

## **03. SOLUÇÃO**

Implementada a geração da tag "descRendimento" com o texto fixo "Rendimentos Isentos Outros" quando o "tpIsencao" for igual a 99.

Disponível a partir da biblioteca 12.1.2306
