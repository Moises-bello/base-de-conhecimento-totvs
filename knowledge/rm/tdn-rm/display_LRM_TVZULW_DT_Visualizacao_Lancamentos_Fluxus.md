---
content_hash: 7988e235ddee7230e13ca2d3b5ab1049033d0b5e417ffcc402aafd6340c77b3a
fetched_at: '2026-06-29T00:08:20.234994+00:00'
page_id: '268572727'
product: rm
source: tdn-rm
title: TVZULW_DT_Visualizacao_Lancamentos_Fluxus
type: documentation
url: https://tdn.totvs.com/display/LRM/TVZULW_DT_Visualizacao_Lancamentos_Fluxus
version: 113
---

# LANÇAMENTOS FINANCEIROS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construções e Projetos* |
| **Módulo:** | *Folha de Pagamento.* |
| **Função:** | *Lançamentos Financeiros* |
| **Situação/Requisito:** | *Quando o usuário possui em seu perfil no sistema Gestão Financeira, nos seguintes menus:*     [02.01.01.05] Visualizar Lançamentos a Receber [02.01.01.06] Visualizar Lançamentos a Pagar [02.01.01.07] Visualizar Lançamentos Contábeis [02.01.01.08] Visualizar Lançamentos Não Contábeis  Ao realizar a visualização de lançamentos através do financeiro, o sistema aplicava o filtro barrando a visualização dos itens conforme suas restrições, porém quando o processo era feito no RMLabore, o sistema não respeitava os filtros que foram definidos pelo sistema de Gestão financeira e mostrava ao usuário todos os lançamentos mesmo quando o mesmo não possuía permissão para visualizar os mesmos no RMFluxus. |
| **Solução/Implementação:** | *Foi ajustado o sistema para respeitar o filtro que foi imposto pelo sistema Financeiro , desta forma o filtro que for definido por padrão no financeiro será respeitado e o usuário não irá visualizar lançamentos que não pode.* |
| **Chamados relacionados:** | TVZULW |

divs
