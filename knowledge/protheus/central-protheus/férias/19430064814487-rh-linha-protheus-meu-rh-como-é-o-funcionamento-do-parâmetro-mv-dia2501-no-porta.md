---
article_id: 19430064814487
category: FÉRIAS
content_hash: 4447551a6008733a2ca6a64730698f666a9441e5fb4bd8c5614c5c69eafccc5c
fetched_at: '2026-06-28T22:44:34.511082+00:00'
product: protheus
section_id: 10299705719575
source: central-protheus
title: RH - Linha Protheus - MEU RH - Como é o funcionamento do parâmetro MV_DIA2501
  no Portal Meu RH
type: support-article
updated_at: '2026-06-24T11:50:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/19430064814487-RH-Linha-Protheus-MEU-RH-Como-%C3%A9-o-funcionamento-do-par%C3%A2metro-MV-DIA2501-no-Portal-Meu-RH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19430048429719) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**  
O Portal Meu RH acata o conteúdo do parâmetro **MV\_DIA2501** quando existem férias que contemplam os dias **25/12** e **01/01**?  
  
**Ambiente**  
TOTVS RH (Linha Protheus) - Meu RH - Todas as versões  
  
**Solução**  
O parâmetro **MV\_DIA2501**tem como objetivo pagar como licença remunerada os dias comemorativos de final de ano (Natal e/ou véspera – dias 24 e 25/12, e Ano Novo e/ou véspera, dias 31/12 e 01/01), no cálculo das férias.  
  
Para alterar o parâmetro, acesse o Configurador (SIGACFG) em **Ambiente > Cadastros > Parâmetros**  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/19431025596951)**  
  
A configuração do parâmetro permite as seguintes opções:   
**S** – Assume como dias de Licença Remunerada, somente os dias **25/12** e **01/01**;  
**N** – Não considera dias de Licença Remunerada para o cálculo;  
  
Quando é solicitada as férias no Portal **Meu RH**, até que seja de fato realizado o **cálculo** pelo módulo de SIGAGPE, o Portal Meu RH irá considerar os dias de férias corridos.  
  
Exemplo do aviso antes do calculo de férias dentro do Portal:  
![unnamed.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19430076616471)  
  
**Posterior ao cálculo das férias**, no sistema será considerado a configuração do parâmetro **MV\_DIA2501= S,** assim, serão considerados dois dias a mais de férias visto que os dias **25/12** e **01/01** serão remunerados:  
![unnamed.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19430081183639)  
  
**Saiba Mais**  
[**CLIQUE AQUI** para acessar mais artigos e FAQs sobre o MEU RH](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360005048113-RH-Meu-RH)  
[**CLIQUE AQUI** para acessar a documentação de referências sobre o MEU RH](https://tdn.totvs.com/pages/releaseview.action?pageId=284477421)
