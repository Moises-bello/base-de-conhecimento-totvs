---
content_hash: 59c3f335b65a1e95065f224ee53a719cb5d5a9e6661e71401d66695bae9d5189
fetched_at: '2026-06-29T00:06:06.112523+00:00'
page_id: '201728514'
product: rm
source: tdn-rm
title: TTCZOB_DT_Msg_Multiplos_Vinculos_Recibo_Ferias
type: documentation
url: https://tdn.totvs.com/display/LRM/TTCZOB_DT_Msg_Multiplos_Vinculos_Recibo_Ferias
version: 1
---

# RECIBO DE FÉRIAS DE MÚLTIPLOS VÍNCULOS

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Função de Fórmula* |
| **Situação/Requisito:** | *Quando existem funcionários com Múltiplos Vínculos utilizando Chapa Centralizadora, caso sejam cadastradas férias somente para um vínculo, no cálculo do Recibo de Férias é exibida a mensagem abaixo:*  *"A Chapa 00001, que é Centralizadora de IRRF do Funcionário 00002 não foi selecionada para o processo. O Funcionário 00001 deverá ser recalculado para que o IRRF fique correto."*  *Foi solicitado para complementar a mensagem, informando que o Lançamento das Férias só será permitido se a Chapa Centralizadora for selecionada, junto com os demais vínculos.* |
| **Solução/Implementação:** | *Melhorar a mensagem de Múltiplos Vínculos no cálculo do Recibo de Férias para informar que se a Chapa Centralizadora não for selecionada para o cálculo, não será possível efetuar o lançamento para o envelope.*  *Segue a nova mensagem que será exibida:*  *"A Chapa 00001, que é Centralizadora de IRRF do Funcionário 00002 não foi selecionada para o processo. O Funcionário 00001 deverá ser recalculado para que o IRRF fique correto. O Lançamento das Férias para a movimentação só poderá ser processado selecionando a Chapa Centralizadora, junto com os demais vínculos."* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTCZOB* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.8* |
