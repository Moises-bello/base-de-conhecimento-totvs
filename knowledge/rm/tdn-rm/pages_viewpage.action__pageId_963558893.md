---
content_hash: 903e63ebde7ea1af7acc09e31212c02e3e8b2907f86bc950b4af5951ce5bd109
fetched_at: '2026-06-29T00:12:14.070443+00:00'
page_id: '963558893'
product: rm
source: tdn-rm
title: 'Fiscal01 - 26226 - Campo: NCM'': Conteúdo do campo não obedece ao Esquema
  da NF-e.'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=963558893
version: 1
---

## **01. DADOS GERAIS**

| Produto: | TOTVS |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | Envio NF-e / NFC-e |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-226226 |

## **02. SITUAÇÃO/REQUISITO**

Ao enviar NF-e/NFC-e que utiliza item do tipo serviço, apresentou a seguinte mensagem de inconsistencia:

Campo: NCM: Conteúdo do campo não obedece ao Esquema da NF-e. O valor '' não é aceito pelo padrão estabelecido pela SEFAZ: [0-9]

{2}|[0-9]{8}.\*  
**Mensagem Original:**  
\*Element '{[http://www.portalfiscal.inf.br/nfe](http://www.portalfiscal.inf.br/nfe "Follow link")}NCM': [facet 'pattern'] The value '' is not accepted by the pattern '[0-9]{2}

|[0-9]

{8}

## **03. SOLUÇÃO**

Realizado ajuste no envio de NF-e e NFC-e, para quando o NCM estiver vazio e o tipo de item for "Serviço", seja enviado como "00".
