---
content_hash: ef1cde50ed2e0de3093b0241580538d5e4e51611fcadb161f115a27d1e8a3af9
fetched_at: '2026-06-29T00:08:18.166320+00:00'
page_id: '263193433'
product: rm
source: tdn-rm
title: TVLEBS_DT_Baixa
type: documentation
url: https://tdn.totvs.com/display/LRM/TVLEBS_DT_Baixa
version: 112
---

# Baixa

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | Gestão Financeira. |
| **Função:** | Baixa. |
| **Situação/Requisito:** | Ao cancelar o item de baixa de um lançamento que foi baixado parcialmente, sendo que a primeira baixa foi contabilizada, e a segunda baixa realizada marcando a opção contabilizar posteriormente, o sistema cancela os itens de baixa gerados mas ao consultar a contabilidade é possível encontrar os registros da baixa contabilizada. |
| **Solução/Implementação:** | Ajustado o formulário de itens de baixa, para poder editar a contabilização de um item de baixa caso o laçamento estiver com status Contábil "BaixaAContabilizar" ou "ContabilBaixaAContabilizar". Alterado o serviço de baixa para executar o cancelamento contábil para os itens de baixa que tiverem operação contábil. |
| **Conversores e Parâmetros:** | N/A. |
| **Chamados relacionados:** | N/A. |
| **Requisito (ISSUE):** | FIN000040. |

divs
