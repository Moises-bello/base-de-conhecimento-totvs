---
content_hash: e1c2feb14548be63d49441d4b134ff6c9f8861d055913df8d1d8bf6210966ef2
fetched_at: '2026-06-29T00:11:27.479742+00:00'
page_id: '725742498'
product: rm
source: tdn-rm
title: DT FISCAL01-19073 - NFE tag ipidevol sendo gerada com valor zerado
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+FISCAL01-19073+-+NFE+tag+ipidevol+sendo+gerada+com+valor+zerado
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | NFe (Nota Fiscal Eletrônica) |
| País: | Brasil |
| Ticket: | 15621336 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-19069 |

## **02. SITUAÇÃO/REQUISITO**

Cliente relata que ao efetuar uma devolução de Compra, o valor do tributo IPI devolvido não está sendo gerado no XML, ocasionando a rejeição 610 - Total da NF difere do somatório dos Valores que compõe o valor Total da NF.

## **03. PROBLEMA**

Ao fazer a cópia de movimento pelo "Assistente de cópia por referência", são gerados dois sequenciais de item relacionados ao movimento: um com o número zero, representando os dados do movimento, e aqueles maiores que zero, representando os dados dos itens do movimento, para quantos itens estiverem cadastrados. Para cada tributo existente, é gerada uma linha com seu respectivo sequencial. Por exemplo:

Em um movimento que possui ICMS e IPI, contendo um item, e seu item também possui ICMS e IPI:

| N° sequencial | Tributo |
| --- | --- |
| 0 | ICMS |
| 0 | IPI |
| 1 | ICMS |
| 1 | IPI |

 O primeiro tributo de IPI existente no movimento era considerado na geração da tag <vIPIDevol>. Logo, era considerado o IPI relativo ao movimento (sequencial zero), e não ao item do movimento (sequencial maior que zero).

## **04. SOLUÇÃO.**

Serão considerados na geração da tag <vIPIDevol>, no processo de envio de NFe, os sequenciais relacionados ao movimento que sejam maiores que zero.

Disponível a partir da versão 12.1.2205
