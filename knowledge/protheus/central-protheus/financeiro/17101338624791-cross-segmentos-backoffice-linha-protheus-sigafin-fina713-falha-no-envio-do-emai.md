---
article_id: 17101338624791
category: Financeiro
content_hash: da38b2da13db22fa700a90a52513c3faef46fd42b5f9a28e6687b80f19da8419
fetched_at: '2026-06-28T22:38:03.133829+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA713 - Falha no
  envio do Email
type: support-article
updated_at: '2023-08-28T21:58:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17101338624791-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA713-Falha-no-envio-do-Email
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17101625732119) Tempo aproximado para leitura: **00:10:00 min**

**Ocorrência**  
No módulo Financeiro, ao realizar o envio do boleto via API é apresentado erro no envio do boleto.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/17101735126167)  
**Causa**

O erro pode ser apresentado por não constar o e-mail configurado no cadastro do cliente ou por falta de configuração nos parâmetros.

**Solução**

No **cadastro do cliente**, clique em **alterar,** Outras Ações >**Complemento do Cliente**. Preencha os campos em vermelho conforme print **![](https://totvssuporte.zendesk.com/attachments/token/gUYXQjscnby6S3fKsM6Kd9fuJ/?name=image.png)**

Para envio das cartas por e-mail são utilizados os seguintes parâmetros:

[Carta de Cobrança - Financeiro - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=492706741)

![](https://totvssuporte.zendesk.com/attachments/token/3AGZvzKIoheJ5TITHNOdv6Kbr/?name=image.png)  
   
Após configurar os parâmetros acima, deve entrar no **Configurador**>**menu ambiente**>**e-mail/proxy(1)**>**Configurar**  
   
![](https://totvssuporte.zendesk.com/attachments/token/Nj7BUFWPF4fFpgUoyoE1D1DWk/?name=image.png)  
   
Adicione o e-mail e senha e avance até a próxima imagem  
   
![](https://totvssuporte.zendesk.com/attachments/token/FCuPUTj5XS2gD3IvBSQpZKoo3/?name=image.png)  
   
   
Ajuste as configurações conforme a imagem abaixo:  
   
![](https://totvssuporte.zendesk.com/attachments/token/U9GKVg9vwERt8JTTtHRD4dbmb/?name=image.png)  
 

**Saiba mais**  
[Envio de boleto - Visão geral](https://tdn.totvs.com/pages/releaseview.action?pageId=635983295)

Ponto de entrada para customização do Boleto  
[JOB Transmissão e Envio de E-mail - FINA713](https://tdn.totvs.com/pages/releaseview.action?pageId=619130482)
