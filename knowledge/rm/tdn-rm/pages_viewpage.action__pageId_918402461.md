---
content_hash: 2fd8b3c003d55a16653f63bb8c803bb65663b0dc0b265a4a4a569dd9b235722b
fetched_at: '2026-06-29T00:12:06.934003+00:00'
page_id: '918402461'
product: rm
source: tdn-rm
title: 'Função de Fórmula: NDFALT'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=918402461
version: 4
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Exemplo de utilização**
3. **Tabelas utilizadas**

## **01. VISÃO GERAL**

Retorna o número de dias de faltas no período aquisitivo. A variável **NDFALT** é utilizada somente para buscar o número de faltas cadastradas no controle de faltas, que estão cadastradas dentro do último período aquisitivo em **aberto.**

## **02. EXEMPLO DE UTILIZAÇÃO**

**Exemplo de Cálculo de Faltas no Período Aquisitivo de Férias**

**Período Aquisitivo (Aberto):** 03/03/2011 a 02/03/2012  
  
  
  
**Faltas registradas:**

* 01 dia em 02/03/2011 (fora do período aquisitivo – **não contabiliza**)
* 01 dia em 21/09/2011 (dentro do período aquisitivo – **contabiliza**)
* 01 dia em 22/09/2011  (dentro do período aquisitivo – **contabiliza**)
* 01 dia em 10/10/2011  (dentro do período aquisitivo – **contabiliza**)
* 01 dia em 03/03/2012(após o período aquisitivo – **não contabiliza**)

**Resultado:** Apenas as 3 faltas ocorridas durante o período aquisitivo **ABERTO** (de  03/03/2011 a 02/03/2012) serão consideradas.  
Essas 3 faltas serão informadas no campo **"Dias de Faltas"** do cadastro de férias do funcionário, pois apenas as faltas **dentro do período aquisitivo vigente** impactam o cálculo.

Com essas informações podemos executar a Fórmula **NDFALT**

## **03. TABELAS UTILIZADAS**

* **PFHSTFALTA**
* **PFUFERIAS**
