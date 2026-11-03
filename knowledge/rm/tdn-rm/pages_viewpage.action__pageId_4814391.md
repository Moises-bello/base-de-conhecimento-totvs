---
content_hash: bd98552a3b312ce366cbcdf0adf59c6a8d17a68d5ff8a322f425923f403ad70d
fetched_at: '2026-06-29T00:10:19.468160+00:00'
page_id: '4814391'
product: rm
source: tdn-rm
title: Aditivo Contratual - Renegociação de contrato com fórmula
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4814391
version: 5
---

BLOCK

Aditivo Contratual - Renegociação de contrato com fórmula

FAQ: **Aditivo Contratual - Renegociação de contrato com fórmula**

|  |  |
| --- | --- |
| Produto: | RM |
| Ambiente: | Unspecified |
| Versão: | 10.70 |

Avaliação

Ao realizar um aditivo de renegociação de contrato com fórmula as opções **“Simular Novo Plano”** e **“Avançar”** estão desabilitadas?

Causa

Ao criar um aditivo de renegociação de contrato com fórmula o valor do “Saldo Devedor Selecionado” **difere** do valor do “Saldo Devedor Negociado”.

Solução

Para que a simulação do novo plano de financiamento e o avanço da etapa ocasionando em conclusão do processo estejam habilitados, o “Saldo Devedor Selecionado” **OBRIGATORIAMENTE** deve ser **IGUAL** ao “Saldo Devedor Negociado”. O saldo devedor selecionado é oriundo da seleção das parcelas do plano de financiamento antigo. Já o saldo devedor negociado faz jus a nova regra estipulada para o financiamento pós aditivo.

**Informações Adicionais**

O processo de renegociação de contrato **SEM** fórmula não obriga os saldos a serem iguais, pois há um parâmetro que controla a permissão de saldos diferentes, ou seja, caso a permissão esteja habilitada os saldos poderão ser diferentes. Este parâmetro não existe para a renegociação de contrato com fórmula.
