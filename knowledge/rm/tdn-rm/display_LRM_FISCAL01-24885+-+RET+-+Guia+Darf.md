---
content_hash: 65213558a7a4d5ff0a478118bc635b79b108eed929c9b64c3c85ac31062c448e
fetched_at: '2026-06-29T00:12:07.366976+00:00'
page_id: '925337039'
product: rm
source: tdn-rm
title: FISCAL01-24885 - RET - Guia Darf
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-24885+-+RET+-+Guia+Darf
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | EFD Contribuições |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-24885 |

## **02. SITUAÇÃO/REQUISITO**

Ao gerar o registro 1800 da rotina EFD Contribuições o campo 07 (Valor Recolhimento Unificado) não está sendo gerado. Criamos o período de apuração para o tributo RET conforme documentação, após criamos o evento tributário para o tributo RET e encerramos o período de apuração, criamos uma guia manualmente para simularmos a geração do campo 7 e o mesmo não realiza a soma do valor principal das guias, sistema informa apenas o valor principal da primeira guia.

## **03. SOLUÇÃO**

Ajuste no registro 1800 da EFD Contribuições referente ao valor do campo 7.  
O Campo sete passa a ser gerado com o somatório do valor principal das guias do tributo RET, sendo agrupado por código de receita e data de recolhimento.

Disponível a partir da biblioteca 12.1.2406
