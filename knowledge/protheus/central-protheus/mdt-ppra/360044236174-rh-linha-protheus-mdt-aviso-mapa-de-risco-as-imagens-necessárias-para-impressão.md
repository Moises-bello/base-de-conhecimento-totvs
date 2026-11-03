---
article_id: 360044236174
category: MDT - PPRA
content_hash: e56177582b545c19b6e905ed1c50ffcbeb256f6d91937e14a74efdb5947359b7
fetched_at: '2026-06-28T22:44:27.257375+00:00'
product: protheus
section_id: 360010945454
source: central-protheus
title: 'RH - Linha Protheus - MDT - Aviso Mapa de Risco: As imagens necessárias para
  impressão do Mapa de Risco não foram encontradas no servidor'
type: support-article
updated_at: '2025-08-14T12:36:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044236174-RH-Linha-Protheus-MDT-Aviso-Mapa-de-Risco-As-imagens-necess%C3%A1rias-para-impress%C3%A3o-do-Mapa-de-Risco-n%C3%A3o-foram-encontradas-no-servidor
---

**Ocorrência**Ao tentar acessar a rotina **Mapa de Risco** ocorre o aviso:   
As imagens necessárias para impressão do **Mapa de Risco** não foram encontradas no servidor. As seguintes imagens devem estar no diretório configurado no parâmetro **MV\_DIRACA**: *NgMapa01.Bmp, NgMapa02.Bmp, NgMapa03.Bmp, NgMapa04.Bmp, NgMapa05.Bmp, NgMapa06.Bmp, NgMapa07.Bmp, NgMapa08.Bmp,*

Parâmetro **MV\_DIRACA** = \SAMPLES\  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Causa**Não existe as imagens *NgMapa01.Bmp* até NgMapa08.Bmp ou o diretório onde as imagens estão não foi definido no parâmetro**MV\_DIRACA**.  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Coloque as imagens **NgMapaXX**.**Bmp** dentro de um diretório na pasta **protheus\_data.** As imagens estão disponíveis no pacote de expedição continua do MDT, para saber como baixar acesse o artigo: [MP - MDT - Como fazer o download (baixar) do pacote de expedição continua (acumulado) do modulo medicina e segurança do trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057956773-MP-MDT-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-continua-acumulado-do-modulo-medicina-e-seguran%C3%A7a-do-trabalho?source=search);  
  
2. Acesse no modulo configurador (SIGACFG) o parâmetro **MV\_DIRACA** e defina o caminho da pasta onde estão as imagens.   
Exemplo: \imagens\mdt\ngmapa;  
  
3. Execute a rotina **Mapa de Risco** (MDTR650) novamente.  
![mapa_risco.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360060017274)  
  
**Saiba Mais**Para saber mais consulte os links abaixo:   
[Artigos - PPRA](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010945454-MDT-PPRA)  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206971487-RH-Medicina-e-Seguran%C3%A7a-do-Trabalho%20%20)
