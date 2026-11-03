---
content_hash: 4486da00a490bca8afaf9d770f7c5fe12ab6ed4b2f1660088f0083b785983707
fetched_at: '2026-06-29T00:11:32.332807+00:00'
page_id: '746489986'
product: rm
source: tdn-rm
title: FISCAL01-19517 - DT -  Default da Natureza de Rendimentos
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-19517+-+DT+-++Default+da+Natureza+de+Rendimentos
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | EFD Reinf |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-19479 |

## **02. SITUAÇÃO/REQUISITO**

Verificar se a Natureza de Rendimento está preenchida no Produto ou Cli\For na inclusão do movimento.

## **03. SOLUÇÃO**

**Para os Tributos IRRF, IRRFPJ e IRRFIMPORT o preenchimento no movimento segue a seguinte regra:**

> Se preenchido no Cadastro do produto (Anexos | Dados Fiscais do Produto), considera este  
Senão, Se preenchido no Cliente Fornecedor (IR na pasta Outros | Tributos), considera este  
Senão, considera o preenchido no tipo de Movimento.

**Para as demais retenções que são PISRF, COFINSRF, COSIRF, CSLLRF e CSRF o preenchimento no movimento segue a seguinte regra:**

> Se preenchido no Cliente Fornecedor (Tributos, demais tributos na pasta Tributos Default do Fornecedor), considera este  
Senão, considera o preenchido no tipo de Movimento.

Disponível a partir da biblioteca 12.1.2209
