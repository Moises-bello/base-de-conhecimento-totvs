---
content_hash: 7ceb167ab6e7ff633a388a0ee41a4195cb8d5c351bbbe0db551ac2659fcc2d7a
fetched_at: '2026-06-29T00:12:14.678257+00:00'
page_id: '969992514'
product: rm
source: tdn-rm
title: FISCAL01-26310 - NT_2025.001- Dados de Pagamento com cartão/PIX
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=969992514
version: 2
---

## **01. DADOS GERAIS**

| Produto: | TOTVS |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | BackOffice |
| Módulo: | Gestão de Estoque, Compras e Faturamento |
| Função: | Envio NF-e / NFC-e |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-26310 |

## **02. SITUAÇÃO/REQUISITO**

De acordo com a regra de validação abaixo, precisamos alterar a geração do xml da nota, para aplicar a mesma regra da validação de forma que não corra a rejeição 391

> **Y04-10:** Se informado o grupo de pagamentos (tag:pag): - Se o Pagamento for por cartão (tag:tPag=03, 04), ou PIX (tpag=17), deve ser informado   
> o grupo de cartões (tag:card)
>
> **391/Rejeicao:** Não informados os dados do cartão de crédito / débito nas Formas de Pagamento da Nota Fiscal [nOcor:999]

## **03. SOLUÇÃO**

Realizado ajuste para enviar a tag: card no grupo de pagamento, quando for por cartão de débito ou credito ou se for pix. Tanto para NF-e quanto para NFC-e. Comportamento já aplicado em ambiente de homologação e será aplicado após a data de entrada em vigor em produção da NT2025.001 (01/09/2025);
