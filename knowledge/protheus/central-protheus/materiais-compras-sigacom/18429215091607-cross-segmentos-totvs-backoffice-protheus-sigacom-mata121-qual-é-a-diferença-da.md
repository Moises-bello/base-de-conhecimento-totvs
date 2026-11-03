---
article_id: 18429215091607
category: Materiais - Compras (SIGACOM)
content_hash: b24b7e6e2fe268a1067e10c497e5f6eae5bf990f439008c0a886d6adb9824715
fetched_at: '2026-06-28T22:41:20.152649+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - MATA121 - Qual é a
  diferença da utilização dos parâmetros MV_ALTPC e MV_ALTPEDC ?
type: support-article
updated_at: '2024-01-18T13:49:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18429215091607-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-MATA121-Qual-%C3%A9-a-diferen%C3%A7a-da-utiliza%C3%A7%C3%A3o-dos-par%C3%A2metros-MV-ALTPC-e-MV-ALTPEDC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18429204275991) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Qual é a diferença da utilização dos parâmetros MV\_ALTPC e MV\_ALTPEDC na rotina MATA121?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras -  A partir da versão 12.1.33  
  
**Solução**O parâmetro **MV\_ALTPEDC** define se poderá ser alterado, ou não os campos de quantidade e valor unitário do pedido de compras. Quando o seu conteúdo é N, o sistema não permite alteração desses dois campos, gerando um Help quando tenta-se alterar. Quando seu conteúdo é S, o sistema permite que os dois campos, sejam alterados.  
Já o parâmetro **MV\_ALTPC** define se haverá a possibilidade de abrir a tela de alteração do pedido. Ou seja, quando o seu conteúdo é .T.  o sistema gera o help no momento em que o usuário clica no botão "ALTERAR" da rotina do pedido de compras, nem chega a abrir a tela para alteração. Quando o conteúdo  .F., o sistema permite que o usuário clique em alterar e que a tela de alteração seja aberta.   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18429489206167)

![](https://totvssuporte.zendesk.com/attachments/token/QlC6EULOApVlWu7iNAnRlZlF7/?name=image.png)

Na prática segue a lógica abaixo:

O parâmetro **MV\_ALTPC** olha se todos os itens do PC foram atendidos. Se sim, e o parâmetro estiver habilitado (.T.) o sistema gera o help no momento em que o usuário clica no botão "ALTERAR" da rotina do pedido de compras, nem chega a abrir a tela para alteração. Porém quando pelo menos um dos itens não estiver totalmente atendido, o sistema vai abrir a tela de alteração pois alguns itens estão totalmente atendidos e não o pedido inteiro. Dessa forma, para bloquear a alteração da quantidade e valor unitário, será necessário utilizar o parâmetro **MV\_ALTPEDC = N.**

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como bloquear Alteração de Pedido de Compras Atendido - MV\_ALTPC ?](Cross%20Segmentos%20-%20Totvs%20Backoffice%20Protheus%20-%20SIGACOM%20-%20Como%20bloquear%20Altera%C3%A7%C3%A3o%20de%20Pedido%20de%20Compras%20Atendido%20-%20MV_ALTPC%20?)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Bloquear alteração do pedido de compras](Cross%20Segmentos%20-%20Totvs%20Backoffice%20Protheus%20-%20SIGACOM%20-%20Bloquear%20altera%C3%A7%C3%A3o%20do%20pedido%20de%20compras)
* <https://tdn.totvs.com/pages/viewpage.action?pageId=312158126>
