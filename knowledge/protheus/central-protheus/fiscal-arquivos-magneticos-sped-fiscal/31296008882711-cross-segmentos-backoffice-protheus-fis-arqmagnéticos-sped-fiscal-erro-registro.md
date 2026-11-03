---
article_id: 31296008882711
category: Fiscal Arquivos Magneticos - SPED Fiscal
content_hash: 9f8263d40801abf01a7063eed885284978a951ccf0be11ba9f9540ff0683881a
fetched_at: '2026-06-28T22:42:00.776933+00:00'
product: protheus
section_id: 1500001535141
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - SPED FISCAL  -  ERRO
  REGISTRO D130
type: support-article
updated_at: '2025-04-09T19:54:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/31296008882711-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-SPED-FISCAL-ERRO-REGISTRO-D130
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/31296061350679) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Erro ao validar o arquivo do Sped Fiscal: Registro filho não informado.   
  
**Ambiente**

Protheus – Livros Fiscais – A partir da versão 12.1.2310

**Solução:**

O erro relacionado ao registro D130 passou a ocorrer devido à nova atualização do PVA(5.0.1).

Com base no próprio layout do SPED FISCAL o registro D130 deverá ser apresentando somente para CTE **simplificado** ou **substituto simplificado**, mais a nova versão do PVA, passou a validar todos os tipos de CTE.

**REGISTRO D130: COMPLEMENTO DO CONHECIMENTO RODOVIÁRIO DE CARGAS (CÓDIGO 08), DO CONHECIMENTO RODOVIÁRIO DE CARGAS AVULSO (CÓDIGO 8B) E DO CONHECIMENTO DE TRANSPORTE ELETRÔNICO SIMPLIFICADO (CÓDIGO 57)**

Este registro tem por objetivo informar o complemento do Conhecimento de Transporte Rodoviário de Cargas (Código 08), Conhecimento de Transporte de Carga**s Avulso (Código 8B) e, a partir de janeiro de 2025, o Conhecimento de Transporte Eletrônico Simplificado (Código 57, TP\_CT-e 5 e 6)**.

Alteração da descrição do **registro D130:**

Nova Validação: Este registro tem por objetivo informar o complemento do Conhecimento de Transporte Rodoviário de Cargas (Código 08), Conhecimento de Transporte de Cargas Avulso (Código 8B) e, a partir de janeiro de 2025, o **Conhecimento de Transporte Eletrônico Simplificado (Código 57, TP\_CT-e 5 e 6).** **(Código 57, TP\_CT-e 5 e 6).**

**5 = Simplificado**

**6 = Substituto Simplificado**

<http://sped.rfb.gov.br/estatico/30/007F992E2E9F284F1DC7D9AC50A4CF3BE4513C/Guia%20Pr%c3%a1tico%20EFD%20-%20Vers%c3%a3o%203.1.8.pdf>

Desta forma, para que o erro não ocorra, deverá ser realizado **a atualização do PVA para versão 5.0.2**.

**Segue abaixo o link para atualização do PVA.**

<http://sped.rfb.gov.br/pagina/show/7769>
