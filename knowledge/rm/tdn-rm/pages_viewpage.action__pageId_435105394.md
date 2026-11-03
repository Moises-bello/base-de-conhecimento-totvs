---
content_hash: 47f5f3a015b592870e7a8495316739fd05ffa6b518da2ddb2ad636e7a465ce4e
fetched_at: '2026-06-29T00:09:50.097084+00:00'
page_id: '435105394'
product: rm
source: tdn-rm
title: Distrato - Processo - Desfazer efetivação Distrato
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105394
version: 4
---

Esse processo tem como função alterar a Situação do Distrato de Efetivado para Em preparação.

Dessa forma a venda voltará ao Status de Efetivada e seus lançamentos serão desbloqueados, enquanto os lançamentos do Distrato serão bloqueados.

Cabe ressaltar que as ações executadas na venda, devem seguir uma **ordem cronológica**, para que não hajam erros. Ou seja, o TCGI não permitirá que se desfaça a efetivação de um Distrato caso haja um Aditivo de Distrato efetivado e vice-versa, o sistema não permitirá que um Aditivo efetivado antes de um Distrato (ou seja, quanto a Situação desta venda estava Efetivada) tenha a sua Situação alterada sem antes se Desfazer a Efetivação deste (Situação da Venda Distratada).

É preciso seguir a ordem cronológica das ações.

Para que este processo seja executado corretamente, o parâmetro do TIN "Cancelar Parcelas da venda ao Efetivar Aditivo" deve estar *Desmarcado*. Este parâmetro encontra-se nos Parâmetros do TIN -> Contrato -> Etapa 5 - Plano de financiamento -> Agrupamento do distrato.
