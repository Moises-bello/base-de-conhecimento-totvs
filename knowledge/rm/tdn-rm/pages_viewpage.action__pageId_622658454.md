---
content_hash: d252483815758ca44da57b1d6e97c0e505789ee2a5b55e7077b040597a54919b
fetched_at: '2026-06-29T00:11:03.457026+00:00'
page_id: '622658454'
product: rm
source: tdn-rm
title: FISCAL01-14901 - DT EFD ICMS\IPI - E110 - Lanc. Ajuste
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=622658454
version: 6
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | Gestão Fiscal |
| Função: | Geração do Arquivo EFD ICMS\IPI |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-14901 |

## **02. SITUAÇÃO/REQUISITO**

Alterar o SPED Fiscal para considerar o código de ajuste do lançamento na geração do E110.

## **03. SOLUÇÃO**

Considerar os ajustes C197 e D197 dos lançamentos fiscais no registro E110 da EFD ICMS\IPI.

Deve ser considerado como Ajuste de Débito (Considerar como débito) os Códigos de Ajuste cujo o Terceiro caractere for igual a ‘3’, ‘4’ ou ‘5’ e o Quarto caractere for igual a “0”, “3”, “4”, “5”, “6”, “7” ou “8”.

Exemplo de código: UF30xxxxxx, UF04xxxxxx

Deve ser considerado como Ajuste de Crédito (Considerar como crédito) os Códigos de Ajuste cujo o Terceiro caractere for igual a ‘0’, ‘1’ ou ‘2’ e o Quarto caractere for igual a ‘0’, “3”, “4”, “5”, “6”, “7” ou “8”.

Exemplo de código: UF00xxxxxx, UF03xxxxxx.
