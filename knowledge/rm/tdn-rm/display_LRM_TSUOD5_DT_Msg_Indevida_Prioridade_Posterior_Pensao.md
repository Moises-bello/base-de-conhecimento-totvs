---
content_hash: c4af7f7cdaf850d191d67dfd697927fcc9233511371b432678aab5ea3b9b33e6
fetched_at: '2026-06-29T00:06:10.296201+00:00'
page_id: '203760710'
product: rm
source: tdn-rm
title: TSUOD5_DT_Msg_Indevida_Prioridade_Posterior_Pensao
type: documentation
url: https://tdn.totvs.com/display/LRM/TSUOD5_DT_Msg_Indevida_Prioridade_Posterior_Pensao
version: 4
---

# MSG INDEVIDA DE EVENTO COM PRIORIDADE POSTERIOR À PENSÃO ALIMENTÍCIA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Pensão Alimentícia* |
| **Situação/Requisito:** | *Está sendo exibida indevidamente mensagem de consistência de prioridade de eventos que incidem em pensão, quando existe restituição de INSS no envelope, e o evento de CC 92 incide em pensão.*  *Mensagem:  "O(s) evento(s) 0111 lançado(s) para o funcionário 000101, incidem em Pensão de Folha e estão com prioridade posterior ao evento de cc13.  É necessário acertar a prioridade para que o valor da Pensão Alimentícia possa ficar correto."* |
| **Solução/Implementação:** | *Ajuste na consistência de prioridade de eventos que incidem pensão, para não exibir a mensagem indevidamente quando existir restituição de INSS no envelope do funcionário* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TSUOD5* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *11.82.41* |
