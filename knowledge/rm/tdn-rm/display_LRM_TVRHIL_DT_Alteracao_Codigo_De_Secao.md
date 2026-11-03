---
content_hash: 9c7deeff38b4107cb42f9f0bc179fa57bc9df2dc8d602ad347413f6b2340057e
fetched_at: '2026-06-29T00:08:16.907171+00:00'
page_id: '248582446'
product: rm
source: tdn-rm
title: TVRHIL_DT_Alteracao_Codigo_De_Secao
type: documentation
url: https://tdn.totvs.com/display/LRM/TVRHIL_DT_Alteracao_Codigo_De_Secao
version: 113
---

# ALTERAÇÃO CODIGO DE SECAO

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construções e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Alterar Código de Seção.* |
| **Situação/Requisito:** | *Ao alterar o código de uma seção o seguinte erro é apresentado:*  *ORA-02292: restrição de integridade (RM.FKPSECAOPROPOSTADEPARA\_PSECAO) violada - registro filho localizado* |
| **Solução/Implementação:** | O erro acontecia pois existiam informações na tabela PSECAOPROPOSTADEPARA que não haviam sido substituídas pela nova seção, deixando vínculo com a seção antiga, causando assim o erro, foi ajustado o código para que o sistema troque o código da seção na tabela e não exista mais vínculo com a tabela do erro, podendo assim realizar a alteração do código. |
| **Chamados relacionados:** | TVRHIL |

divs
