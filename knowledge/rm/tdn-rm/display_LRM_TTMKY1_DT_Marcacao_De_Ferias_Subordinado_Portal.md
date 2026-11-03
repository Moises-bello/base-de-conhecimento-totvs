---
content_hash: 6dbd35dd1a38f0428a61a8730471f01333129f012a0d9cbcca41cb5a8fdfe4c5
fetched_at: '2026-06-29T00:06:16.103585+00:00'
page_id: '211062792'
product: rm
source: tdn-rm
title: TTMKY1_DT_Marcacao_De_Ferias_Subordinado_Portal
type: documentation
url: https://tdn.totvs.com/display/LRM/TTMKY1_DT_Marcacao_De_Ferias_Subordinado_Portal
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
| **Chamados relacionados:** | TTMKY1 |
| **Versões/Release:** | *11.82.42* |

divs
