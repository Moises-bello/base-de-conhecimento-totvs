---
content_hash: cecae70ce1e0f6038b1604398c990281dbddb57c2a05f71e10f2a31e857b0df8
fetched_at: '2026-06-29T00:06:16.106728+00:00'
page_id: '211062802'
product: rm
source: tdn-rm
title: TTORA0_DT_Marcacao_De_Ferias_Subordinado_Portal
type: documentation
url: https://tdn.totvs.com/display/LRM/TTORA0_DT_Marcacao_De_Ferias_Subordinado_Portal
version: 1
---

# MARCAÇÃO DE FÉRIAS SUBORDINADO (PORTAL)

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Marcação de Férias de Subordinado via Portal* |
| **Situação/Requisito:** | Quando o chefe aprovava férias de um subordinado, era verificado o grupo de acesso do chefe, não do subordinado, pra validar as informações. Ao MARCAR férias para o subordinado, também estava tentando pegar o grupo de acesso do subordinado e era lançada exceção quando não havia grupo associado. |
| **Solução/Implementação:** | Caso o subordinado não possua grupo de acesso e o funcionário logado seja diferente do funcionário das férias (em caso de chefe marcando para subordinado), é pego o grupo de acesso do chefe. |
| **Chamados relacionados:** | TTORA0 |
| **Versões/Release:** | *12.1.9* |

divs
