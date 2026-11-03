---
content_hash: cfec11df8fb739494307d92afd5edc632de87a6a7641685ef80d4cc37bf2975f
fetched_at: '2026-06-29T00:08:09.734698+00:00'
page_id: '239040047'
product: rm
source: tdn-rm
title: TVACJD_DT_Historico_Situacao_Incorreto
type: documentation
url: https://tdn.totvs.com/display/LRM/TVACJD_DT_Historico_Situacao_Incorreto
version: 117
---

# HISTÓRICO DE SITUAÇÃO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Histórico de Situação* |
| **Situação/Requisito:** | Ao gerar a contabilização retroativa para funcionário demitido, o sistema conclui o processo com sucesso porém apresenta as seguintes mensagens:     Lote: XXXXXX     Excluindo o lote XXXXXXX     [Erro] Nao existem lançamentos para estes parâmetros.     Os valores de provisão e encargos do funcionário foram gerados, mas a contabilização não leva os valores para o lote criado. |
| **Solução/Implementação:** | *Foi identificado um histórico de situação com o valor nulo no campo NOVASITUACAO. Alterado para exibir esses registros no histórico de situação.* |
| **Chamados relacionados:** | *TVACJD* |

divs
