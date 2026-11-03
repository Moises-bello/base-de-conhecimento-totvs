---
content_hash: febcc6356661a6d1c79526eae2596d33e93bb58f270a5718e9efb1f17eae6d51
fetched_at: '2026-06-29T00:12:16.394838+00:00'
page_id: '985689189'
product: rm
source: tdn-rm
title: FISCAL01-26605 - NFCom - det e prod - Movimento
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-26605+-+NFCom+-+det+e+prod+-+Movimento
version: 1
---

| Produto: | TOTVS |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | BackOffice |
| Módulo: | Gestão de Estoque, Compras e Faturamento |
| Função: | NFCom |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-26605 |

## **02. SITUAÇÃO/REQUISITO**

> # NFCom - det e prod - Movimento
>
> * Alterar o Movimento para o campo TITMMOVFISCAL.INFADICIONAISNFE também fique visivel para a NFCom, no entanto as descrições referente a NF-e também devem ser ajustada para NFCom, ou deve ser genéricas (Exemplo Informações Adicionais)
> * Dentro dos Dados Fiscais do serviço, deverá ser criado um campo para indicar a classificação do serviço conforme definido na NFCom. [https://dfe-portal.svrs.rs.gov.br/NFCOM/tabelacclass](https://dfe-portal.svrs.rs.gov.br/NFCOM/tabelacclass "Follow link")

## **03. SOLUÇÃO**

Alterado a regra de visibilidade para que o campo seja apresentado quando o parametro do tipo de movimento referente a NFCom esteja diferente de não integrado.

Incluído o lookup de Classificação item de Comunicação/Telecomunicação nos dados fiscais do produto. Lookup possui regra para apresentar somente que tenha o campo = 6.
