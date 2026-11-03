---
article_id: 34873382055703
category: Financeiro
content_hash: 0ea340c8a5613729788d06f6d8c6d6e4a65ecd8e1f083686a7421d9d626e9ced
fetched_at: '2026-06-28T22:38:01.024678+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - SIGAFIN- Qual a configuração
  necessária para gerar nota fiscal com cálculo de PIS e COFINS apuração?
type: support-article
updated_at: '2025-09-11T19:50:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34873382055703-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-Qual-a-configura%C3%A7%C3%A3o-necess%C3%A1ria-para-gerar-nota-fiscal-com-c%C3%A1lculo-de-PIS-e-COFINS-apura%C3%A7%C3%A3o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34873389959319) Tempo aproximado para leitura: **00:15 min**

**Dúvida**  
Qual a configuração necessária para gerar nota fiscal com cálculo de PIS E COFINS via apuração?  
  
**Ambiente**  
Cross Segmento - BackOffice Linha Protheus – Financeiro – A partir da versão 11.80  
  
**Solução**

**TES – Notas de Entrada**

* **PIS/COFINS (F4\_PISCOF):** Ambos
* **Crédito PIS/COFINS (F4\_PISCRED):** Credita
* **Tipo de Regime (F4\_TPREG):** Cumulativo ou Não Cumulativo
* **Situação Tributária PIS (F4\_CSTPIS):** 50 a 66
* **Situação Tributária COFINS (F4\_CSTCOF):** 50 a 66
* **Livro Fiscal ICMS (F4\_LFICM) / IPI (F4\_LFIPI) / ISS (F4\_LFISS):** Preenchimento obrigatório com valor **diferente de “NÃO”**, pois é necessário configurar ao menos um dos livros fiscais para que os valores de PIS e COFINS sejam gerados nas tabelas **SF3** e **SFT**.

### 

### TES – Notas de Saída

* **PIS/COFINS (F4\_PISCOF):** Ambos
* **Crédito PIS/COFINS (F4\_PISCRED):** Debita
* **Tipo de Regime (F4\_TPREG):** Cumulativo ou Não Cumulativo
* **Situação Tributária PIS (F4\_CSTPIS):** 01 a 49
* **Situação Tributária COFINS (F4\_CSTCOF):** 01 a 49
* **Livro Fiscal ICMS (F4\_LFICM) / IPI (F4\_LFIPI) / ISS (F4\_LFISS):** Preenchimento obrigatório com valor **diferente de “NÃO”**, garantindo a geração dos valores de PIS e COFINS nas tabelas **SF3** e **SFT**.

### Produto

* **Percentual PIS (B1\_PPIS):** Informar a alíquota
* **Percentual COFINS (B1\_PCOFINS):** Informar a alíquota

> Para a apuração, o sistema considera primeiramente as alíquotas definidas na **Exceção Fiscal**. Caso não existam, utiliza as alíquotas do **produto** e, na ausência destas, recorre aos parâmetros **MV\_TXPIS** e **MV\_TXCOFIN**.

### 

### Fornecedor

* **Recebe PIS (A2\_RECPIS):** Não
* **Recebe COFINS (A2\_RECCOFI):** Não

### 

### Cliente

* **Recebe PIS (A1\_RECPIS):** Não
* **Recebe COFINS (A1\_RECCOFI):** Não

### Parâmetros – Apuração de PIS/COFINS

* **MV\_TXPIS:** Taxa para cálculo do PIS → **1.65** ou **0.65** (usar ponto como separador decimal)
* **MV\_TXCOFIN:** Taxa para cálculo do COFINS → **7.60** ou **3.00** (usar ponto como separador decimal)

**Saiba Mais**

[Retenção de PIS COFINS CSLL](https://tdn.totvs.com/pages/releaseview.action?pageId=6076816)
