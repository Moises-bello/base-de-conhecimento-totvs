---
content_hash: 9868925d54b375c0fdbe50c4166bcfad9a30ce2deb809d947af89ba108ae8a76
fetched_at: '2026-06-29T00:10:00.946724+00:00'
page_id: '452718644'
product: rm
source: tdn-rm
title: Código de Cálculo 116 - Estorno Base INSS Dissídio Retroativo Férias
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452718644
version: 4
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Base de cálculo do tipo valor.  
Este evento será utilizado para o cálculo de diferença de férias dissídio e será o somatório da diferença calculada dos eventos de férias que tenham incidência em INSS incluindo os descontos com incidência em estorno de inss.

## **02. EXEMPLO DE UTILIZAÇÃO**

Supondo um cálculo de férias com os valores abaixo:

Cálculo da diferença de férias por dissidio:

Veja que no cálculo do código de cálculo 116 - Estorno Base INSS Dissídio Retroativo Férias, somente os eventos com incidência em INSS foram considerados, ou seja, foram somados os valores:

(0045 - DIF.FERIAS) + (0079 - DIF 1/3FERIAS MÊS) + (0107 - DIF. OUTROS EVENTOS DE FERIAS PROVENTO COM INCIDÊNCIAS) – (0245 - DIF. OUTROS EVENTOS DE FERIAS DESCONTO COM INCIDÊNCIAS)

166,67 + 55,56 + 150,00 – 5,00 = 367,23

Veja também TDN [Código de Cálculo 88 – Diferença Outros Eventos Férias](https://tdn.totvs.com/pages/releaseview.action?pageId=452719641)

## **03.** **TABELAS UTILIZADAS**

* PEVENTO

---

Códigos de Cálculo
