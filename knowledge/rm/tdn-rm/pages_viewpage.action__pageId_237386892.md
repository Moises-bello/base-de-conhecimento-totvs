---
content_hash: 20d119f6619f7022f20ad0ea4dd68e33f9b08c494575a044a6bfde50dc6b4948
fetched_at: '2026-06-29T00:08:07.743968+00:00'
page_id: '237386892'
product: rm
source: tdn-rm
title: TUUZGH_DT_Aproveitamento_Conta_Corrente_Baixa_Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=237386892
version: 116
---

# APROVEITAMENTO CONTA CORRENTE

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *TOTVS Gestão Educacional* |
| **Função:** | *Aproveitamento Conta Corrente* |
| **Situação/Requisito:** | *No processo de "Aproveitar valores em conta corrente", quando natureza da conta corrente é um Crédito, o sistema está obrigando a preencher o campo "Evento p/inclusão do lançamento" incorretamente visto que o default do parâmetro Fluxus "Contas a Pagar | Contab. Inclusão | Default Contábil no lançamento" está com "Baixa contábil".* |
| **Solução/Implementação:** | No processo de "Aproveitar valores em conta corrente", quando natureza da conta corrente é um Crédito e estiver configurado para buscar o Tipo Contábil do Serviço, o sistema observa o parâmetro do Fluxus "Contas a Pagar | Contab. Inclusão | Default Contábil no lançamento". Somente se este default for do tipo "Contabil" ou "A contabilizar", será obrigatório o preenchimento do campo "Evento p/inclusão do lançamento". |
| **Conversores e Parâmetros:** | *N/A* |
| **Chamados relacionados:** | N/A |
| **Requisito (ISSUE):** | *N/A* |

divs
