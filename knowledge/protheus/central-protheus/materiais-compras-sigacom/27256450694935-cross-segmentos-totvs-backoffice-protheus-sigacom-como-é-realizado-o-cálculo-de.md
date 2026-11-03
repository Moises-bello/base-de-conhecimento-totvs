---
article_id: 27256450694935
category: Materiais - Compras (SIGACOM)
content_hash: 9a178930ea658c9b0713cb92c4cc5246f92796b6f27a13ecf62760c877798f63
fetched_at: '2026-06-28T22:41:15.824193+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como é realizado o
  cálculo de necessidade na rotina Ponto de Pedido?
type: support-article
updated_at: '2025-09-17T13:41:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/27256450694935-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-%C3%A9-realizado-o-c%C3%A1lculo-de-necessidade-na-rotina-Ponto-de-Pedido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/27256435869591) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**  
Como é realizado o cálculo de necessidade na rotina Ponto de Pedido?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Compras - Todas as versões

**Solução**

**Exemplo**

**Cenário 1**  
 

1.**Aba Mrp/Suprimentos do Cadastro de Produto**  
   
Ponto de Pedido = **3**  
   
Estoque de Segurança = **20**  
   
![](https://totvssuporte.zendesk.com/attachments/token/novOz0dniadEZqvIw3KElbxIg/?name=image.png)  
 

2.Saldo de Estoque do produto  = **3**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/27256450670743)

3.Pergunte da Rotina **MATA170** Considera Est. Segurança =  **Sim**  
![](https://totvssuporte.zendesk.com/attachments/token/XkguvfIHMtft8ChdJfdO32tKO/?name=image.png)  
   
  
4.Pergunte da Rotina **MATA170** com o Pergunte **Cons.Necess Bruta**igual a **Sim.**  
   
![](https://totvssuporte.zendesk.com/attachments/token/pLP47bHADDlbbOnpFpyzwHZAE/?name=image.png)  
   
5.Ao Executar a Rotina de Solicitação de Ponto de Pedido foi incluso uma Solicitação de compras por Ponto de Pedido com a Quantidade de **Estoque de Segurança(20) + 1.**  
   
![](https://totvssuporte.zendesk.com/attachments/token/wGCB05Z5TH9mg2zEUJOFvRq5q/?name=image.png)  
 6. Após executado a rotina é gerado a solicitação/pedido de compras seguindo o seguinte calculo:  **P****onto de pedido + estoque de segurança - estoque atual + 1  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34611354765591)**

**Cenário 2**  
   
Realizar a mesma configuração do  **Cenário 1** , porém , ajustar o pergunte da rotina MATA170 

**Cons.Necess Bruta** para  **Não.**

Dessa forma foi incluso uma Solicitação de Compras com a  **Quantidade de Estoque de Segurança** **- Saldo Estoque + 1**.  
   
![](https://totvssuporte.zendesk.com/attachments/token/BwGnVANGZNZ3Zc02hdVoZPIG1/?name=image.png)

**IMPORTANTE :**

Quando o Item do pedido não alimentar o campo SB2\_SALPED é porque a TES esta configurada para atualiza estoque = NÃO.

**Obs:**

O campo Ajuste Estoque Máximo , não é considerado no cálculo da rotina de Solicitação por Ponto de Pedido

**Obs 2:**

Para o calculo ser realizado de acordo com as configurações acima, o parâmetro **MV\_ARQPROD** precisa estar configurado como **SB1.**

***Saiba Mais :***

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Não está considerando Solicitação de Compras bloqueadas para o cálculo da necessidade na Rotina de solicitação de Compras por Ponto de Pedido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/27310881678615-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-N%C3%A3o-est%C3%A1-considerando-Solicita%C3%A7%C3%A3o-de-Compras-bloqueadas-para-o-c%C3%A1lculo-da-necessidade-na-Rotina-de-solicita%C3%A7%C3%A3o-de-Compras-por-Ponto-de-Pedido)

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como gerar Solicitação de Compras/Pedido de Compras por ponto de pedido ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360011967491-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-gerar-Solicita%C3%A7%C3%A3o-de-Compras-Pedido-de-Compras-por-ponto-de-pedido)

[Cross Segmentos - TOTVS Backoffice Protheus - SIGACOM - Ponto de Pedido por Filial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/28214204601239-Cross-Segmentos-TOTVS-Backoffice-Protheus-SIGACOM-Ponto-de-Pedido-por-Filial)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
