---
content_hash: 3f622bd36d271595eddfae35fa84357f5ae188c5bed0a7e3204a94dbf8d1beee
fetched_at: '2026-06-29T00:08:13.449729+00:00'
page_id: '244422821'
product: rm
source: tdn-rm
title: TUNOGK_DT_SEFIP
type: documentation
url: https://tdn.totvs.com/display/LRM/TUNOGK_DT_SEFIP
version: 114
---

# SEFIP

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e projetos* |
| **Módulo:** | *Folha de pagamento* |
| **Função:** | *SEFIP* |
| **Situação/Requisito:** | Ao parametrizar as telas da geração do processo da SEFIP, na tela de parametrização especifica da coligada na aba de lançamentos financeiros, é selecionado a opção de gerar os lançamentos financeiros com o tipo SEFIP - FGTS a recolher. São preenchidas as informações referente a data de emissão, data de vencimento e dados das tabelas opcionais. Os campos "Gerar lançamentos rateados por departamento" e "Gera lançamentos rateados por centro de custo" não são marcados. Porém ao confirmar as informações (clicando em OK) e sair da tela, ao retornar a tela as flags são selecionados automaticamente e com isso são geradas informações de rateios que não devem ser geradas para o financeiro. |
| **Solução/Implementação:** | Ajuste realizado para que os parâmetros "Gerar lançamentos rateados por departamento" e "Gera lançamentos rateados por centro de custo" fiquem consistentes com a marcação que o usuário deseja.  Implementada regra para que o parâmetro "Gera lançamentos rateados por centro de custo" não apareça na tela caso o cliente não utiliza centro de custo e/ou a opção por ratear por centro de custo esteja marcada como obrigatória no Fluxus |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | TUNOGK TVDJ43 |
| **Requisito (ISSUE):** |  |

divs
