---
content_hash: 2c7ae997a4a7688c7d28c9301ef866f2de772ef2f42a21dc16be6eccae7fdb99
fetched_at: '2026-06-29T00:08:04.084967+00:00'
page_id: '235335497'
product: rm
source: tdn-rm
title: TUNC52_DT_GERACAO_RAIS_MANAD
type: documentation
url: https://tdn.totvs.com/display/LRM/TUNC52_DT_GERACAO_RAIS_MANAD
version: 114
---

# MANAD

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *MANAD* |
| **Situação/Requisito:** | *MANAD gera arquivo em formato errado quando utilizado parâmetro de distribuição por tomador.* |
| **Solução/Implementação:** | Ajuste na rotina de geração do MANAD para considerar distribuição por tomadores quando o funcionário não possui histórico cujo CEI/CGC da Seção é diferente da Seção centralizadora mínima. Ex: seção histórico funcionário 03.01, seção centralizadora mínima: 01 (possuem CEI/CGC diferentes) |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TUNC52 TUQIBW |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.43* |
| **Versão Corrigida:** |  |
| **Versão Expedida:** |  |

divs
