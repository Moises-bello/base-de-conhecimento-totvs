---
article_id: 4418236529431
category: Meu RH - Ponto
content_hash: 5b34c7c1f1a01c5719d9ec4a3b0f7acf6f52c599730a24bf5c9e6932daeacb8d
fetched_at: '2026-06-28T22:47:30.351316+00:00'
product: rm
section_id: 1500000861782
source: central-rm
title: RH - RM - Meu RH - Precisão de Geolocalização no aplicativo MeuRH
type: support-article
updated_at: '2025-09-12T19:45:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418236529431-RH-RM-Meu-RH-Precis%C3%A3o-de-Geolocaliza%C3%A7%C3%A3o-no-aplicativo-MeuRH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:07 min****Ocorrência**Quando o Usuário realiza a batida de ponto pelo aplicativo Meu RH, a precisão da localização não condiz com a realidade.  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - Meu RH - Todas as versões  
  
**Causa**  
Esse incidente pode ocorrer devido à configurações incorretas dos aparelhos, como falta do modo alta precisão, calibragem não realizada ou agentes externos que possam interferir na localização.  
  
**Solução**Podemos adotar medidas para trazer as latitudes/longitudes mais próximas a localização real do usuário como:

**Ativar o modo de alta precisão**  
Para ajudar o **Google Maps** a encontrar seu local e indicar a localização com mais precisão, use o modo de alta precisão.

1. No seu *tablet* ou *smartphone* **Android**, abra o app Configurações ![](https://lh3.googleusercontent.com/PzFeiQQaPASuntRuvWiXoqZjQqUj0s0q0w_jI4Nx9vL6x7rGmmS9f-xQr1Kj9S91WMlm=w36-h36).
2. Toque em **Local**.
3. Na parte superior, ative o local.
4. Toque em **Modo** ![](https://lh3.googleusercontent.com/SaY5lqCwN7kppnS546l9ys-E2sZftTTIHjBrdV-WsGPIhGjaxcEXjfgdIfW_UNG7Sw0=w26-h36) **Alta precisão**.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418236510487/mceclip0.png)

**Calibrar seu smartphone ou tablet**

1. No seu *smartphone* ou *tablet* **Android**, abra o app **Google Maps** ![](https://storage.googleapis.com/support-kms-prod/zvYEMw88qc8J2qhmJrzVWX85sBovhBKB9FR9)
2. Movimente o *smartphone* desenhando um 8 no ar até calibrar sua bússola. É necessário fazer isso apenas algumas vezes.
3. O feixe ficará estreito e apontará na direção certa.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418236526231/mceclip1.png)

**Importante**  
A geolocalização é apenas uma funcionalidade consumida dentro da nossa solução, não é nativo do aplicativo **MeuRH**.

A localização pode ser realizada através de algumas possibilidades, como por exemplo, através do **IP** (Internet Protocol) da rede, triangulação **GPRS** (Serviços Gerais de Pacote por Rádio) ou mesmo pelo **GPS** **físico** (Sistema de Posicionamento Global).

O **MeuRH** quando está sendo utilizado no *browser* não existe a opção do **GPS Físico**, então são utilizados funcionalidades disponibilizadas pelos *browsers* compatíveis para realizar essa busca via endereço de sua conexão na internet, o resultado dessa avaliação pode ser impreciso, pois além de não ser um *hardware* físico, o usuário precisa realizar a permissão e configuração de execução no *browser*, no caso do **Google Chrome** também habilitar o modo "alta precisão", quando concordamos em enviar informações detalhadas para os servidores do Google.

Todavia, quando nossa solução é utilizada pelo celular utilizamos o serviço de localização baseado em GPS físico, pré-existentes nos aparelhos, podendo trazer as latitudes/longitudes mais próximas a localização real do usuário.  
  
**Saiba Mais**  
[Utilização da geo-localização no aplicativo MeuRH](https://tdn.totvs.com/pages/releaseview.action?pageId=516629620)
