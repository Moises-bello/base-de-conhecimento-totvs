---
content_hash: c17002b7ad2cf9290fcf2a061b2dd5875c7a99175f350a1f894ad5a129ccdb62
fetched_at: '2026-06-29T00:08:17.873843+00:00'
page_id: '259558093'
product: rm
source: tdn-rm
title: TVJUB7_DT_Emissão_Recebimento_Cheque
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=259558093
version: 111
---

# Cheques - Emissão / Recebimentos de cheque

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | Gestão Financeira |
| **Função:** | Cheques - Emissão/Recebimentos cheque |
| **Situação/Requisito:** | O sistema apresenta erro de Débito/Crédito na baixa de lançamento com cheque incluso. Problema acontece porque o item de baixa está sem as tabelas opcionais, e o evento para contabilização do item de baixa está buscando defaults nas tabelas opcionais do item de baixa. |
| **Solução/Implementação:** | Ajustado  serviço de baixa para sobrescrever as tabelas opcionais do lançamento pelas tabelas opcionais relacionadas ao extrato, somente quando estas informações existirem e o parâmetro " => Cheque=> Copiar os campos opcionais do lançamento" estiver desmarcado. |
| **Conversores e Parâmetros:** | N/A. |
| **Chamados relacionados:** | N/A. |
| **Requisito (ISSUE):** | FIN000156 |

divs
