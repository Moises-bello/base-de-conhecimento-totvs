---
article_id: 360016347811
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: 6e11512ef6ccf7a64562f440b7e9ea51fdd8f8d3c5934a6f01b0301d1c5f1772
fetched_at: '2026-06-28T22:42:05.321786+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - EFD Contribuições
  - Tabelas utilizadas nas devoluções pela rotina de Apuração da EFD Contribuições
  (FISA001)
type: support-article
updated_at: '2023-01-04T17:34:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016347811-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-EFD-Contribui%C3%A7%C3%B5es-Tabelas-utilizadas-nas-devolu%C3%A7%C3%B5es-pela-rotina-de-Apura%C3%A7%C3%A3o-da-EFD-Contribui%C3%A7%C3%B5es-FISA001
---

**Dúvida**Quais são as Tabelas utilizadas nas Devoluções pela rotina FISA001?  
   
 **Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 11.80.  
  
**Solução**  
 Para solucionar essa dúvida, realize os seguintes passos:  
 1. Verifique a amarração dos campos abaixo na nota fiscal de devolução, referente a origem nas tabelas **SFT** e **CF4**:**FT\_SERORI** =? Deve estar com o mesmo conteúdo da nota fiscal original, campo **FT\_SERIE**;  
**FT\_NFORI**=? Deve estar com o mesmo conteúdo da nota fiscal original, campo igual a nota fiscal original **FT\_NFISCAL**;  
**FT\_ITEMORI** =? Deve estar com o mesmo conteúdo da nota fiscal original, campo **FT\_ITEM;**  
**CF4\_TIPO** = D.  
  
2 -Verifique o tamanho e o conteúdo dos campos na tabela **CF4** que deve estar igual a tabela **SFT**,para o correto ajuste das devoluções: **CF4\_FILIAL** e **CF4\_FLORIG** devem estar com mesmo tamanho e conteúdo do campo **FT\_FILIAL**;  
**CF4\_NOTA** deve estar com mesmo tamanho e conteúdo do campo **FT\_NFISCAL**;  
**CF4\_SERIE** deve estar com mesmo tamanho e conteúdo do campo **FT\_SERIE**;  
**CF4\_ITEM** deve estar com mesmo tamanho e conteúdo do campo **FT\_ITEM**;  
**CF4\_LOJA** deve estar com mesmo tamanho e conteúdo do campo **FT\_LOJA**;  
**CF4\_CLIFOR** deve estar com mesmo tamanho e conteúdo do campo **FT\_CLIFOR**;  
**CF4\_VALPIS** deve estar com mesmo tamanho e conteúdo do campo **FT\_VALPIS**;  
**CF4\_VALCOF** deve estar com mesmo tamanho e conteúdo do campo **FT\_VALCOF**;  
**CF4\_BASPIS** deve estar com mesmo tamanho e conteúdo do campo **FT\_BASPIS**;  
**CF4\_BASCOF** deve estar com mesmo tamanho e conteúdo do campo **FT\_BASCOF**;  
**CF4\_ALIPIS** deve estar com mesmo tamanho e conteúdo do campo **FT\_ALIQPIS**;  
**CF4\_ALICOF** deve estar com mesmo tamanho e conteúdo do campo **FT\_ALIQCOF**;  
**CF4\_CSTPIS** deve estar com mesmo tamanho e conteúdo do campo **FT\_CSTPIS**;  
**CF4\_CSTCOF** deve estar com mesmo tamanho e conteúdo do campo **FT\_CSTCOF**;  
**CF4\_DATAE** deve estar com mesmo tamanho e conteúdo do campo **FT\_EMISSAO**.
