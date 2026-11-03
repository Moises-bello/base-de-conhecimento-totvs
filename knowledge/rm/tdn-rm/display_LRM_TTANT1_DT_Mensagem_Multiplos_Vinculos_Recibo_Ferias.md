---
content_hash: e80d89e72ffcf0f14ed59d309ca7a51bb979a1812c55eab8358e55bbe6d1b8ec
fetched_at: '2026-06-29T00:06:05.782666+00:00'
page_id: '201727297'
product: rm
source: tdn-rm
title: TTANT1_DT_Mensagem_Multiplos_Vinculos_Recibo_Ferias
type: documentation
url: https://tdn.totvs.com/display/LRM/TTANT1_DT_Mensagem_Multiplos_Vinculos_Recibo_Ferias
version: 3
---

# RECIBO DE FÉRIAS DE MÚLTIPLOS VÍNCULOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Múltiplos Vínculos* |
| **Situação/Requisito:** | *Quando existem funcionários com Múltiplos Vínculos utilizando Chapa Centralizadora, caso sejam cadastradas férias somente para um vínculo, no cálculo do Recibo de Férias é exibida a mensagem abaixo:*  *"A Chapa 00001, que é Centralizadora de IRRF do Funcionário 00002 não foi selecionada para o processo. O Funcionário 00001 deverá ser recalculado para que o IRRF fique correto."*  *Foi solicitado para complementar a mensagem, informando que o Lançamento das Férias só será permitido se a Chapa Centralizadora for selecionada, junto com os demais vínculos.* |
| **Solução/Implementação:** | *Melhoria na mensagem de Múltiplos Vínculos no cálculo do Recibo de Férias para informar que se a Chapa Centralizadora não for selecionada para o cálculo, não será possível efetuar o lançamento para o envelope.*  *Segue a nova mensagem que será exibida:*  *"A Chapa 00001, que é Centralizadora de IRRF do Funcionário 00002 não foi selecionada para o processo. O Funcionário 00001 deverá ser recalculado para que o IRRF fique correto. O Lançamento das Férias para a movimentação só poderá ser processado selecionando a Chapa Centralizadora, junto com os demais vínculos."* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTANT1* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.41* |
