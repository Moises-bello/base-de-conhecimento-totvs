---
content_hash: 27b5951bd73f8c6649b192aaefb3b3e91b7ee4b6d7b576fde7888357094de70d
fetched_at: '2026-06-29T00:10:19.262336+00:00'
page_id: '4813162'
product: rm
source: tdn-rm
title: Faturamento de Itens Periodicos Sem Vigência Definida
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=4813162
version: 4
---

BLOCK

Faturamento de Itens Periodicos Sem Vigência Definida

FAQ: **Faturamento de Itens Periodicos Sem Vigência Definida**

|  |  |
| --- | --- |
| Produto: | Unspecified |
| Ambiente: | Unspecified |
| Versão: | 11.00 |

Avaliação

* **Introdução**

Apresentar uma solução para os casos em que existem itens de contratos “Periódicos” que não tem fim de vigência definidos.

Solução

* ***Desenvolvimento/Procedimento***

Acessar o cadastro de contrato e incluindo um contrato e em seguida o item de contrato que deverá ser “Periódico” no campo tipo de faturamento e informar a condição de pagamento para o campo “Intervalo de Faturamento”. O campo “Qtde. de Faturamento” não deverá ser preenchido.

As demais informações para este documento não são relevantes e por este motivo devem ser preenchidos conforme conveniência do caso.

*1.* *Dados do Contrato:*

Por se tratar de um item de contrato sem vidência definida o Valor Total do Item irá considerar sempre Quantidade\*Preço Faturamento + Aditivos.

*2.* *Faturamento de Contrato:*

O faturamento deste tipo de item, periódico e sem vigência definida, só deve acontecer pela opção de faturamento por lote, pois o ícone de “Faturar Contrato” da visão de Contrato considera o campo “Qtde. de Faturamento”.

Após criar o lote de faturamento filtrando o contrato desejado, basta informar o período de vencimento que deseja faturar e em seguida faturar o lote.

* **Informações Adicionais**

- Após o faturamento do contrato o “Status de Faturamento” irá ficar como faturado. Mesmo com este status o sistema não irá impedir de faturar o item de contrato para os próximos períodos.

- Por não preencher o campo de “Qtde. de Faturamento” do item de contrato deve-se ficar atento que o valor dos itens já faturados não terá o mesmo valor do contrato.

Observações

O documento em questão está postado no blog da Totvs e pode ser consultado através do link : <http://totvsconnect.blogspot.com/2010/10/como-fazer-faturamento-de-itens.html>
