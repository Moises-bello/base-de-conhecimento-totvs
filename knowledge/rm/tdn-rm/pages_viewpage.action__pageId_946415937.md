---
content_hash: b134d70537f9cfef01f38fd2b04ba98637bd9f52034476e10b782b8784b4f2e8
fetched_at: '2026-06-29T00:12:09.452606+00:00'
page_id: '946415937'
product: rm
source: tdn-rm
title: FISCAL01-25775 - GIA ST - Nova MDI - Relatório de guias da rotina com valores
  incompatíveis com a filial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=946415937
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | GIA-ST |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-25775 |

## **02. SITUAÇÃO/REQUISITO**

Ao gerar o arquivo txt da rotina GIA ST para a UF Rio Grande do Sul é apresentado no campo 3.1 Valor do ICMS-ST Referente ao 1º Vencimento o valor da guia gerada de outro estado no registro A0.

O layout não diferencia as uf das guias conforme o estado informado na tela de geração.

## **03. SOLUÇÃO**

Ajustado Layout para buscar apenas as guias do Estado conforme Parâmetro de geração.

O novo layout FISLAY0024 - GIA-ST está disponível à partir do TOTVS Compartilhamento.

Deve-se Atualizar o Patch e o Layout.

Disponível a partir da biblioteca 12.1.2406
