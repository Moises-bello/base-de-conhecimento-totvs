---
article_id: 360028510331
category: ADVPL - Classe e Função
content_hash: e63496d65207f03e020a74069df656a709e63f3480e2323e53c7714ca3c06560
fetched_at: '2026-06-28T22:40:18.098778+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Tipos de imagem
  na classe MSCBLoadGRF
type: support-article
updated_at: '2021-09-09T15:18:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028510331-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Tipos-de-imagem-na-classe-MSCBLoadGRF
---

**Dúvida**Qual o tipos de imagem pode ser utilizado na classe MSCBLoadGRF ?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 11.80  
  
**Solução**É que para esse padrão RGB a classe não atende seria apenas no nos seguintes padrões conforme documentação.  
Para o padrão Zebra, o arquivo do gráfico (cImagem) tem que ser do tipo GRF, gerado através de um PCX ou TIF no software fornecido pelo fabricante da zebra.  
  
Para o padrão Intermec, o arquivo do gráfico (cImagem) tem que ser do tipo UDC, gerado através de um BMP ou TIF(não compactado) no software fornecido pelo fabricante da intermec.  
Para o padrão Datamax, o arquivo do gráfico pode ser do tipo BMP, PCX, não sendo necessário ser convertido.  
Para o padrão Eltron, o arquivo do gráfico tem que ser do tipo PCX, não sendo necessário ser convertido.  
  
**Saiba mais**  
[**MSCBLoadGraf**](http://tdn.totvs.com/pages/releaseview.action?pageId=6090939)
