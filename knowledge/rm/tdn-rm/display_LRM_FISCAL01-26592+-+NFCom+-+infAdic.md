---
content_hash: 6e9b3523a2c95b761e4326c65b2423b22c6da1f3bbc6725718dee288b3e3a612
fetched_at: '2026-06-29T00:12:16.401046+00:00'
page_id: '989560862'
product: rm
source: tdn-rm
title: FISCAL01-26592 - NFCom - infAdic
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-26592+-+NFCom+-+infAdic
version: 1
---

| Produto: | TOTVS |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | BackOffice |
| Módulo: | Gestão de Estoque, Compras e Faturamento |
| Função: | NFCom |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-26592 |

## **02. SITUAÇÃO/REQUISITO**

> * Ajuste na regra de visibilidade da aba NF-e Estadual, que contem os campos: Informações adicionais ao fisco e Informações complementares ao contribuinte, para que seja apresentada quando NFCom diferente de não integrado
> * alteração do nome de NF-e Estadual para NFCom quando modelo de documento = 62.

## **03. SOLUÇÃO**

Alterado a regra de visibilidade para que a aba seja apresentada quando o parâmetro do tipo de movimento referente a NFCom esteja diferente de não integrado.

Alterado o label para quando o tipo de documento for igual a 62.
