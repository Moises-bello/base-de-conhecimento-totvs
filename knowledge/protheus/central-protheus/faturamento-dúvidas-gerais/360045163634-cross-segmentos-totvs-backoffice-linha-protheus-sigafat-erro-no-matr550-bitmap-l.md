---
article_id: 360045163634
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 4c51f22bda9f6e9f4cf7099df1265c0f9c8c4bb65ef754be1a6a1e3eff1964eb
fetched_at: '2026-06-28T22:38:30.101629+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT-Erro no MATR550 -
  Bitmap logo with size error, equal to 0 or greater then 97 kB. in file
type: support-article
updated_at: '2023-04-17T13:17:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045163634-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Erro-no-MATR550-Bitmap-logo-with-size-error-equal-to-0-or-greater-then-97-kB-in-file
---

**Ocorrência**Ao gerar o relatório de Notas Fiscais (**MATR550**) e demais relatórios, o sistema etá gerando o erro:

**Bitmap logo with size error, equal to 0 or greater then 97 kB. in file ../../../interface/srvprinterfunctions.inl at line 931**  
**on TREPORT:SETLOGO(REPORT01.PRW) 28/06/2019 18:27:40 line : 1747**

**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT- todas as versões.

**Causa**

O erro ocorre ao utilizar um  logo bitmap que esteja maior que 97 KB.

**Solução**

O arquivo de logo para ser inserido em um relatório, deve possuir no máximo 96kb com as medidas 100 pixels de largura por 20 pixels de altura.
