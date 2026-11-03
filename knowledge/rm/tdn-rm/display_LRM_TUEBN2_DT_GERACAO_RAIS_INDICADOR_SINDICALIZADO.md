---
content_hash: d13ab80118d591d8f4c88ca3379d2f9cc9cacd8cc3b780bd056d19dd11cc9cc0
fetched_at: '2026-06-29T00:06:28.120736+00:00'
page_id: '233748133'
product: rm
source: tdn-rm
title: TUEBN2_DT_GERACAO_RAIS_INDICADOR_SINDICALIZADO
type: documentation
url: https://tdn.totvs.com/display/LRM/TUEBN2_DT_GERACAO_RAIS_INDICADOR_SINDICALIZADO
version: 117
---

# GERAÇÃO RAIS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Geração Rais* |
| **Situação/Requisito:** | Indicador de Sindicalizado deixou de ser levado dos Campos Complementares do funcionário para o arquivo RAIS |
| **Solução/Implementação:** | Ajuste na rotina da Rais para validar preenchimento de campo complementar para Indicador de Sindicalizado. Agora a rotina prioriza o preenchimento dos campos complementares para o valor de sindicalizado e caso não esteja preenchido, é levado o valor informado no cadastro do funcionário da aba RAIS |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TUEBN2 TUKRX2 |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.43 12.1.11* |
| **Versão Corrigida:** |  |
| **Versão Expedida:** |  |

divs
