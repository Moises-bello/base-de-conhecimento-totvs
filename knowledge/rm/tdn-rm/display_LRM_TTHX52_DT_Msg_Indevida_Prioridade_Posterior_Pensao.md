---
content_hash: a8027cba14866dc7d095a5c380aabd2f5cbd6a1e3c3d4a5ea76f6682f846b475
fetched_at: '2026-06-29T00:06:10.342208+00:00'
page_id: '203761221'
product: rm
source: tdn-rm
title: TTHX52_DT_Msg_Indevida_Prioridade_Posterior_Pensao
type: documentation
url: https://tdn.totvs.com/display/LRM/TTHX52_DT_Msg_Indevida_Prioridade_Posterior_Pensao
version: 1
---

# MSG INDEVIDA DE EVENTO COM PRIORIDADE POSTERIOR À PENSÃO ALIMENTÍCIA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *C&P* |
| **Módulo:** | *Folha de Pagamento* |
| **Função:** | *Pensão Alimentícia* |
| **Situação/Requisito:** | *Está sendo exibida indevidamente mensagem de consistência de prioridade de eventos que incidem em pensão, quando existe restituição de INSS no envelope, e o evento de CC 92 incide em pensão.*  *Mensagem:  "O(s) evento(s) 0111 lançado(s) para o funcionário 000101, incidem em Pensão de Folha e estão com prioridade posterior ao evento de cc13.  É necessário acertar a prioridade para que o valor da Pensão Alimentícia possa ficar correto."* |
| **Solução/Implementação:** | *Ajuste na consistência de prioridade de eventos que incidem pensão, para não exibir a mensagem indevidamente quando existir restituição de INSS no envelope do funcionário* |
| **Conversores e Parâmetros:** |  |
| **Chamados relacionados:** | *TTHX52* |
| **Requisito (ISSUE):** |  |
| **Versões/Release:** | *12.1.8* |
