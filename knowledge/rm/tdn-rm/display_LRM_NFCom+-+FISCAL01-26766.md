---
content_hash: 99f3b38df62232e4dd29930041c77e8a4408bbdb779649b334f55f75f09b9f42
fetched_at: '2026-06-29T00:12:16.273725+00:00'
page_id: '984978105'
product: rm
source: tdn-rm
title: NFCom - FISCAL01-26766
type: documentation
url: https://tdn.totvs.com/display/LRM/NFCom+-+FISCAL01-26766
version: 1
---

## **01. DADOS GERAIS**

| Produto: | TOTVS |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | NFCom |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [FISCAL01-26766](https://jiraproducao.totvs.com.br/browse/FISCAL01-26766) |

## **02. SITUAÇÃO/REQUISITO**

Habilitar o campo Data de Competência (Integrações | Fiscal) para ficar visível nos Movimentos da NFCom (Modelo 62)

## **03. SOLUÇÃO**

Foi implementada uma validação no campo DTCOMPETENCIASERVICO para ficar habilitado no movimento, sempre que for NFCOM com status integrado ou integradoPorTerceiros
