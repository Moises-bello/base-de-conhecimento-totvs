---
content_hash: 2f8c5a70e506f6b608f182fbc328af7312f99e0446309f2a7801afc98f282916
fetched_at: '2026-06-29T00:11:33.407389+00:00'
page_id: '759926970'
product: rm
source: tdn-rm
title: DT - FISCAL01-18921 - Criar Objeto de Negocio para o Evento R-4020
type: documentation
url: https://tdn.totvs.com/display/LRM/DT+-+FISCAL01-18921+-+Criar+Objeto+de+Negocio+para+o+Evento+R-4020
version: 2
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | EFD Reinf |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-18921 |

## **02. SITUAÇÃO/REQUISITO**

Evento Reinf R-4020 não tem seus dados fornecidos pelo objeto de negócio consumido pelo TReports.

## **03. SOLUÇÃO**

Criação do provedor nativo para os objetos de negócio do TReports;

Objeto de negócio para disponibilizar os dados dos eventos do bloco 40 da REINF (atualmente com o evento R-4020);

Novos campos disponibilizados no provedor:

* VlrBaseIRRFPJ
* VlrIRRFPJ
* VlrBaseAgreg
* VlrAgreg
* VlrBaseCSLL
* VlrCSLL
* VlrBaseCofins
* VlrCofins
* VlrBasePP
* VlrPP

Disponível a partir da biblioteca 12.1.2302
