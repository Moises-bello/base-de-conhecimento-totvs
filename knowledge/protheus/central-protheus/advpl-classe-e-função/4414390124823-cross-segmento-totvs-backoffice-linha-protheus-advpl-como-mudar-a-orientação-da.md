---
article_id: 4414390124823
category: ADVPL - Classe e Função
content_hash: 940995cafbe7d18591d3de8494a1ed11133495ecf8440cafeb80896aefc50961
fetched_at: '2026-06-28T22:40:20.696336+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Como mudar a orientação
  da impressão com papel de tamanho customizado
type: support-article
updated_at: '2021-11-29T17:12:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414390124823-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Como-mudar-a-orienta%C3%A7%C3%A3o-da-impress%C3%A3o-com-papel-de-tamanho-customizado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como mudar a orientação da impressão com papel de tamanho customizado para classe FWMsPrinter?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - ADVPL - Todas versões  
  
**Solução**Como agora o método **setpapersize** suporta um tamanho totalmente customizado caso o primeiro parâmetro seja igual a 0, o comando **setlandscape** não produz o efeito desejado, não muda a orientação do papel. Nesse caso, o mais indicado seria inverter as posições de altura e largura passadas no **setpapersizer**.  
  
**Saiba mais**  
[FWMsPrinter](https://tdn.totvs.com/display/public/PROT/FWMsPrinter)
