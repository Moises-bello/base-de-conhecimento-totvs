---
content_hash: b2e18938f4e5ba9185002cf9d1e3aeee6c93f073c4dc8e1c96cc6a42a73bfac2
fetched_at: '2026-06-29T00:10:25.335356+00:00'
page_id: '502827143'
product: rm
source: tdn-rm
title: 5328084 FISCAL01-8600 DT EFD Contribuições - F100 Campo 16 - Indicador da Origem
  do Crédito
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=502827143
version: 1
---

****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | EFD Contribuições |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-8600 |

**02. SITUAÇÃO/REQUISITO**

Na geração do EFD Contribuições no registro F100 solicita que o campo 16 - Indicador da Origem do Crédito seja gerado como

"0 – Operação no Mercado Interno" quando se tratar de operação com o exterior mas de origem interna.

**03. SOLUÇÃO**

Alterada a geração do "Campo 16 - Indicador da Origem do Crédito",

para gerar valor  “0 – Operação no Mercado Interno” quando o UF do Cli/For associado ao lançamento financeiro for do Exterior e o CSTPIS for igual a

CST 62 – Crédito Presumido – Operação de Aquisição Vinculada Exclusivamente a Receita de Exportação.
