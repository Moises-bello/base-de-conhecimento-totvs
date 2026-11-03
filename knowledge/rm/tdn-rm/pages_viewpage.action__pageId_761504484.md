---
content_hash: 78ef7cd9098b7ffc6f968074fb17b191f46bc62f5a3ed1f70e7326ae8db7089f
fetched_at: '2026-06-29T00:11:33.881005+00:00'
page_id: '761504484'
product: rm
source: tdn-rm
title: Cancelamento Manual da transação com cartão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=761504484
version: 3
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**

## **01. VISÃO GERAL**

Este processo irá atualizar a informação apenas no TOTVS Gestão Financeira.  Em nenhum momento será feita alguma integração com a **adquirente** do cartão de crédito. Para realizar o cancelamento manual de uma transação com cartão, deve ser executado o processo **Cancelamento manual da transação** na visão de transações com cartão de crédito/débito. Uma vez executado este processo, a transação selecionada não irá receber nenhuma atualização por parte da adquirente, e não será possível revertê-lo.

Será possível cancelar manualmente as transações de cartão onde o status da transação for **Pagamento Confirmado** ou **Pagamento Concluído**. Para o modelo **SiTef**, também será permitido cancelar as transações com status **Pagamento Solicitado**, Ao solicitar o cancelamento manual da transação, o status da transação no TOTVS Gestão Financeira será alterado para **Cancelamento Manual.** A transação será atualizada após a execução do processo. Caso o lançamento possua baixa, o sistema tentará realizar o cancelamento da baixa. Não sendo possível, será preciso cancelá-la manualmente.

Como este processo irá atualizar a informação apenas no TOTVS Gestão Financeira, a **movimentação financeira** (extratos de taxas e transferências, por exemplo) deve ser ajustada manualmente.

## **02. EXEMPLO DE UTILIZAÇÃO**
