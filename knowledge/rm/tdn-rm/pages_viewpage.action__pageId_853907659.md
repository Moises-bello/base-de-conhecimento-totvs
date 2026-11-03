---
content_hash: 1540e7c663d06d19a41439219a80f39bab99e8682d15b2f77bde928fbc07fc47
fetched_at: '2026-06-29T00:11:54.517253+00:00'
page_id: '853907659'
product: rm
source: tdn-rm
title: DT - S-1210 - Autônomo Residente no Exterior -  Autônomos Externos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=853907659
version: 8
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | **RM** |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento - eSocial |
| Função: | S-1210 - Autônomo Residente no Exterior -  Autônomos Externos |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-8044](https://jiraproducao.totvs.com.br/browse/DRHROTRM-8044) |

## **02. VERSÕES**

**A partir das Versões:**

* 12.1.2310.232
* 12.1.2402.177
* 12.1.2406.111 e superiores

## **03.****SITUAÇÃO/REQUISITO**

Possibilitar a geração das informações relativas aos dados dos autônomos externos residentes no exterior, de forma similar aos autônomos cadastrados na folha de pagamento.

## **04. SOLUÇÃO**

O sistema agora gera as informações do evento S-1210 para autônomos externos residentes no exterior que estão cadastradas na tabela PPAGTOAUTONOMOEXTRESIDEXTERIOR. Para isso foi implementada a aba de "Dados do Residente ou Domiciliado no Exterior" no cadastro do autônomo externo para permitir a visualização dos dados na tabela PPAGTOAUTONOMOEXTRESIDEXTERIOR que foram inseridos por meio de [importação](https://tdn.totvs.com/pages/viewpage.action?pageId=543064647), [webservice](https://tdn.totvs.com/pages/releaseview.action?pageId=425459227),  conceito, entre outros métodos.

**1)** Acesse o menu Administração de Pessoal | Encargos  | Autônomos Externos.

2) Após a importação, os dados estarão disponíveis na aba "Dados do Residente ou Domiciliado no Exterior". Para visualizá-los, basta editar conforme demonstrado abaixo:

**ATENÇÃO:** Essas informações serão levadas no grupo <**infoPgtoExt**> do evento S-1210.

3) Geração do XML do evento S-1210:

## **05. DOCUMENTAÇÃO**
