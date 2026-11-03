---
article_id: 24572701787159
category: Materiais - Compras (SIGACOM)
content_hash: d45af316fd4f943b6f27bf2c57527b04267b5ee1fc2666251daa26da31f667b5
fetched_at: '2026-06-28T22:41:18.942187+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Help Não é permitido
  utilizar o Rateio por Centro de Custos e por item simultaneamente. Verifique a coluna
  centro de custo rateio e o rateio por item do pedido
type: support-article
updated_at: '2024-07-01T19:21:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24572701787159-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Help-N%C3%A3o-%C3%A9-permitido-utilizar-o-Rateio-por-Centro-de-Custos-e-por-item-simultaneamente-Verifique-a-coluna-centro-de-custo-rateio-e-o-rateio-por-item-do-pedido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24572701739031) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Ao tentar incluir uma Solicitação de Compras (MATA110) ou Pedido de Compras (MATA121) o sistema gera help "Não é permitido utilizar o Rateio por Centro de Custos e por item simultaneamente. Verifique a coluna centro de custo rateio e o rateio por item do pedido"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24572680239511)  
  
**Ambiente**Protheus – Compras – A partir da versão 12  
  
**Solução**Por padrão, na solicitação de compras MATA110 e pedido de compras MATA121 podemos declarar o rateio em apenas uma das duas possibilidades, ou seja, ou declaramos o rateio na linha do item ou no Rateio CC de "Outras Ações". Trata-se de um conceito do sistema, não havendo parâmetro nem ponto de entrada que faça essa tratativa. Diferentemente, no documento de entrada MATA103, temos o parâmetro MV\_M103LRA. Quando este parâmetro está desabilitado, é possível utilizar o rateio tanto em Outras Ações Rateio CC quanto na linha do item. Porém esse parâmetro não tem efeito nas MATA1110 e MATA121.  
   
 

***Saiba Mais :***

**[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como incluir Rateio de Entidades Contábeis na Solicitação de Compras ?](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwiX0B%2FH6Qg6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBzGh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzk4MDAxNjExNTMxNzUtQ3Jvc3MtU2VnbWVudG9zLVRvdHZzLUJhY2tvZmZpY2UtUHJvdGhldXMtU0lHQUNPTS1Db21vLWluY2x1aXItUmF0ZWlvLWRlLUVudGlkYWRlcy1Db250JUMzJUExYmVpcy1uYS1Tb2xpY2l0YSVDMyVBNyVDMyVBM28tZGUtQ29tcHJhcwY7CFQ6DnNlYXJjaF9pZEkiKTM3NjAxODU1LWJiNDctNDVmNC05ZGRjLTc3ZmI1OWEyNTA3MQY7CEY6CXJhbmtpCToLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiHXJhdGVpbyBwZWRpZG8gZGUgY29tcHJhIAY7CFQ6EnJlc3VsdHNfY291bnRpAu0D--e9c1f0c4f4ecedbe6be514bb16c62a4e23a73bac)**  
**[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Help A103RATEI na Inclusão de Documento de Entrada](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwg%2F%2FGLSUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBr2h0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAxMTk4ODAzMS1Dcm9zcy1TZWdtZW50b3MtVG90dnMtQmFja29mZmljZS1Qcm90aGV1cy1TSUdBQ09NLUhlbHAtQTEwM1JBVEVJLW5hLUluY2x1cyVDMyVBM28tZGUtRG9jdW1lbnRvLWRlLUVudHJhZGEGOwhUOg5zZWFyY2hfaWRJIikxMzk0NzM5OC1hYTZlLTQwZjItYmU0ZS1mZTZhM2JmMzYzOWEGOwhGOglyYW5raQY6C2xvY2FsZUkiCnB0LWJyBjsIVDoKcXVlcnlJIg5hMTAzcmF0ZWkGOwhUOhJyZXN1bHRzX2NvdW50aQc%3D--925d3f42be06f2dc40bb59d53258e761a0af9b07)**

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
