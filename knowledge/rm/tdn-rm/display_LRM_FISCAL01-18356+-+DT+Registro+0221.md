---
content_hash: e9f668bd1ec29f23583b3bab28e1e54c678190195a0c5cd8ad344e2452c64f1c
fetched_at: '2026-06-29T00:11:25.456767+00:00'
page_id: '708888628'
product: rm
source: tdn-rm
title: FISCAL01-18356 - DT Registro 0221
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-18356+-+DT+Registro+0221
version: 5
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
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-18356 |

## **02. SITUAÇÃO/REQUISITO**

O registro 0221 foi adicionado na versão 3.1.1 da EFD-ICMS/IPI.

A rotina de geração do SPED não gera o registro.

## **03. SOLUÇÃO**

Atualização feita na rotina do SPED para gerar o novo registro, de acordo com as regras do [manual da EFD-ICMS/IPI](http://sped.rfb.gov.br/estatico/9B/D8DA69D5B801128DB2688E3FAC9410E279A61A/Guia%20Pr%c3%a1tico%20EFD%20-%20Vers%c3%a3o%203.1.1.pdf).

Incluído nova opção na tela de parâmetros da rotina para tornar opcional a geração do registro.

Como o registro é gerado apenas a partir de 2023, a opção é apenas visível caso o ano da data final seja igual ou superior a 2023.

Disponível a partir da biblioteca 12.1.2205
