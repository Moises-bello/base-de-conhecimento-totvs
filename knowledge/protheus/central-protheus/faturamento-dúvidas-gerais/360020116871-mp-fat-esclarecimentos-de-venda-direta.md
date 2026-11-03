---
article_id: 360020116871
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: ebe85ede4a5a27b5993fd5762370391cb16343188f16b15e2f2f65b3364a9ef9
fetched_at: '2026-06-28T22:38:31.066236+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP - FAT - Esclarecimentos de Venda Direta
type: support-article
updated_at: '2021-04-28T15:55:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020116871-MP-FAT-Esclarecimentos-de-Venda-Direta
---

**Dúvida**

Como tratar venda interestadual no venda direta?  
   
 **Ambiente**

Microsiga Protheus – Faturamento – A partir da versão 11.80  
  
   
**Solução**

Até a versão **11.5** do Microsiga Protheus, o Venda Direta é tratado através do fontes do módulo Faturamento **FATA701** e sua família (A,B,C,D, E), **FTVD701** e sua família (A, B, C, D e E).

Até esta versão, a rotina trata a venda interestadual como interna, seguindo o legado do módulo SigaLoja, o qual é o precursor do Venda Direta. Desta forma, entende-se que o cliente está retirando o produto no balcão e com isso, o CFOP da venda sempre será para dentro do estado, iniciado por 5, não levando em conta que o cliente seja de outro estado.

**Saiba** **Mais:**  
**[FAT0113 Esclarecimentos de Venda Direta](http://tdn.totvs.com/display/public/PROT/FAT0113_Esclarecimentos_de_+venda_direta)**
