---
content_hash: d1f3ab6bc32f81bdab707e5b1abe0dff6f88f011f77a8bb72a5bb32159377543
fetched_at: '2026-06-29T00:08:08.309958+00:00'
page_id: '238029854'
product: rm
source: tdn-rm
title: TUVDP2_DT_Erro_Ao_Editar_Lote_Usando_Integracao_Com_Terceiros
type: documentation
url: https://tdn.totvs.com/display/LRM/TUVDP2_DT_Erro_Ao_Editar_Lote_Usando_Integracao_Com_Terceiros
version: 114
---

# LANÇAMENTOS CONTÁBEIS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Lançamentos Contábeis* |
| **Situação/Requisito:** | Ao editar um lote contábil e suas partidas ocorre erro informando que o lote contábil já foi integrado. O sistema está integrado com outros BackOffice, porém não foi executado o processo de envio de lotes para o sistema terceiro, apenas geração.  Mensagem incorreta:O Lote 2 já foi integrado com o backOffice de terceiro |
| **Solução/Implementação:** | *Ajustado validação que verifica se o lote já foi integrado. Essa validação fazia com que a mensagem fosse exibida indevidamente.* |
| **Chamados relacionados:** | *TUVDP2* |

divs
