---
content_hash: 6fbdf1a8b8e111ce883c13d79d37b1c147ab98d51d8b2a471b2e8e6e19fcc8ce
fetched_at: '2026-06-29T00:12:08.533661+00:00'
page_id: '937704795'
product: rm
source: tdn-rm
title: FISCAL01-25604 - DT - NFSE - TPF - Código de Serviço informado (2692) da NFS-e
  não permite tributação fora do município
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=937704795
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | NFS-e |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-25604 |

## **02. SITUAÇÃO/REQUISITO**

Quando o município de prestação não é informado o grupo "prestacao" do XML é gerado sem informações o que pode gerar rejeições em algumas prefeituras.

## **03. SOLUÇÃO**

Foi feita uma alteração para quando o município de prestação de serviços não for informado o grupo prestação passa a não ser gerado no XML da NFSe do TPF

Disponível a partir da biblioteca 12.1.2406
