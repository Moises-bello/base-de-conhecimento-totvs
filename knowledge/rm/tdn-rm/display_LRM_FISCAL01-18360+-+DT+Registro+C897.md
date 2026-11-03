---
content_hash: 560ba76cd331088d721eb127c4dfe4ecc881cd6fc2df7ea318f2912a174934e6
fetched_at: '2026-06-29T00:11:25.676403+00:00'
page_id: '715130616'
product: rm
source: tdn-rm
title: FISCAL01-18360 - DT Registro C897
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-18360+-+DT+Registro+C897
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
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-18360 |

## **02. SITUAÇÃO/REQUISITO**

O registro C897 foi adicionado na versão 3.1.1 da EFD-ICMS/IPI.

A rotina de geração do SPED não gera o registro.

## **03. SOLUÇÃO**

Atualização feita na rotina do SPED para gerar o novo registro, de acordo com as regras do [manual da EFD-ICMS/IPI](http://sped.rfb.gov.br/estatico/9B/D8DA69D5B801128DB2688E3FAC9410E279A61A/Guia%20Pr%c3%a1tico%20EFD%20-%20Vers%c3%a3o%203.1.1.pdf).

O registro é gerado apenas a partir de 2023.

Disponível a partir da biblioteca 12.1.2205
