---
article_id: 360034177533
category: RH - GPS (Guia da Previdência Social)
content_hash: 5eaa605bb75bf5b29f479b8c217ddefd925c8f708f7b7237c6fb92e2023ae663
fetched_at: '2026-06-28T22:43:11.590086+00:00'
product: protheus
section_id: 360011996273
source: central-protheus
title: RH - Linha Protheus - GPE - Como incluir o logo da Previdência Social na Guia
  da GPS
type: support-article
updated_at: '2025-06-25T21:47:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034177533-RH-Linha-Protheus-GPE-Como-incluir-o-logo-da-Previd%C3%AAncia-Social-na-Guia-da-GPS
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33057780501015) Tempo aproximado para leitura: 00:01:00 min**  
**Dúvida**Como incluir o logo da Previdência Social na Guia da GPS  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal – A partir da versão 12.1.17  
  
**Solução**Para incluir a logo da receita no informe de rendimentos deverá ser efetuado o seguinte procedimento:

1. O logo para ser considerada na impressão da **GPS** além de possuir extensão **.bmp** deve possuir **dimensão 119x94, largura: 119, altura: 94.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043295374)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044133753)**2. Cole o arquivo abaixo com nome gps.bmp na pasta system  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043295554)  
  
3. Execute a geração da GPS conforme prints abaixo:  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360044133993)  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043295734)  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043295774)  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360043295874)

**Observações:**Para ambiente Linux, deverá ser configurado da maneira abaixo:

-A system deve conter a imagem da receita com a seguinte nomenclatura para ambiente Linux:**GPS.BMP (Maiúsculo);**-Abra o**appserver.ini** e informe no caminho do **StartPath=/system****\** **(com barra invertida após a palavra System)**.

**Saiba Mais**  
[Artigos Gestão de Pessoal](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867)
