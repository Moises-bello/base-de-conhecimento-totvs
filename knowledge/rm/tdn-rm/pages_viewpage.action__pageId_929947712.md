---
content_hash: 7dd71b46e32663ec7f4ec75ded8f48531e4bc53c6bb5c69745169729cf0d66ef
fetched_at: '2026-06-29T00:12:08.344246+00:00'
page_id: '929947712'
product: rm
source: tdn-rm
title: DT - S-1020 - Adequação do proprietário do CNO
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=929947712
version: 11
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS -  Folha de Pagamento |
| Linha deIm Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS RH (Linha RM) - Folha de Pagamento (LABORE) |
| Função: | S-1020 - Adequação do proprietário do CNO |
| País: | Brasil |
| Issue: | [DRHROTRM-13342](https://jiraproducao.totvs.com.br/browse/DRHROTRM-13342) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2406.262
* 12.1.2410.207
* 12.1.2502.126e superiores

## **03. SITUAÇÃO/REQUISITO**

Adequar a geração do XML do evento **S-1020 - Tabela de Lotações Tributárias** referente aos dados do proprietário do CNO, conforme previsto no layout do eSocial S-1.3.

## **04. SOLUÇÃO**

A geração do XML do evento **S-1020 - Tabela de Lotações Tributárias** foi ajustada para que as tags `<tpInscProp>` e `<nrInscProp>`não sejam geradas quando, no menu eSocial | Lotação Tributária, o campo **"Tipo da Lotação"** estiver definido como **"02 - Obra de Construção Civil - Empreitada Parcial ou Subempreitada"** eo CNO estiver preenchido no campo **"CEI"**.

Ao gerar o XML do evento **S-1020 - Tabela de Lotações Tributárias**serão geradas as tag conforme abaixo
