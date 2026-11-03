---
article_id: 360018011712
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 74ac5619f4ec0ffd10d366ebbceccff4707057ced5833d5513a0d9e9398f4cc1
fetched_at: '2026-06-28T22:37:20.017805+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Como melhorar a precisão
  de cálculo para o Gestão de Contratos (FloatingPointPrecise) ?
type: support-article
updated_at: '2022-05-19T20:48:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018011712-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Como-melhorar-a-precis%C3%A3o-de-c%C3%A1lculo-para-o-Gest%C3%A3o-de-Contratos-FloatingPointPrecise
---

**Dúvida**

Como melhorar a precisão de cálculo para o Gestão de Contratos (FloatingPointPrecise) ?  
  
**Ambiente**

DbAccess - Protheus a partir da versão 11.80  
  
**Solução**

Este parâmetro do Appserver.ini tem influencia na Precisão de Calculo, Arredondamento de Contrato, Planilhas, Revisões e Medições.

Primeiramente antes de qualquer teste de calculo no produto SIGAGCT e necessário ativar em seu **appserver.ini** a chave abaixo:

**[General]**  
**FloatingPointPrecise=1**

Após alterar a chave reinicie o serviço do Protheus, veja abaixo a mensagem que será exibida no console:

![](http://tdn.totvs.com/download/attachments/268598615/image2016-11-4%2011%3A8%3A8.png?version=1&modificationDate=1478264933000&api=v2)

Após a configuração acima acesse o produto SIGAGCT e realize os testes desejados.

Caso queira saber mais sobre a configuração acima acesse a documentação através do link: <http://tdn.totvs.com/display/tec/FloatingPointPrecise>

**![(ideia)](http://tdn.totvs.com/s/pt_BR/7201/3d89a43db3618502ceb73a83aa0af888aa0a285a/_/images/icons/emoticons/lightbulb_on.png)****Importante:** Esta configuração é para todo o produto Protheus e não somente para o SIGAGCT.

***Saiba Mais:***

[FloatingPointPrecise](https://tdn.totvs.com/display/tec/FloatingPointPrecise)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
