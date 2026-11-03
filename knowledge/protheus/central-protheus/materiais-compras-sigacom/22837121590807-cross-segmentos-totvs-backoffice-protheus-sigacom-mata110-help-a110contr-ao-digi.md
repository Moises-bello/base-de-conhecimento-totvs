---
article_id: 22837121590807
category: Materiais - Compras (SIGACOM)
content_hash: dd65d9668d039bd1fb573f8c2dd622ecb906ed3a33fd42acb154ef170723ae1f
fetched_at: '2026-06-28T22:41:20.113592+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - MATA110 Help A110CONTR
  ao digitar código do produto na inclusão de uma solicitação de compras
type: support-article
updated_at: '2026-02-11T13:24:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22837121590807-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-MATA110-Help-A110CONTR-ao-digitar-c%C3%B3digo-do-produto-na-inclus%C3%A3o-de-uma-solicita%C3%A7%C3%A3o-de-compras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22837121573911) Tempo aproximado para leitura: **00:02:00 min**  
  
**Ocorrência**  
Ao digitar o código do produto na inclusão de uma nova solicitação de compra na rotina MATA110 o sistema gera o help A110CONTR.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22837121575191)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - Todas as versões  
  
**Causa**  
Na rotina de solicitação de compras (**MATA110**), o sistema verifica o campo **B1\_CONTRAT** do cadastro de produto (**MATA010**) que está sendo digitado. Isso acontece pois esse campo determina se o produto deverá ser utilizado no contrato de parceria. Esse campo pode ter três conteúdos: Sim, Não e Ambos. Quando o conteúdo desse campo for Sim, ele poderá ser utilizado apenas no contrato de parceria e se tentar incluí-lo na solicitação de compra (**MATA110**) vai gerar o help **A110CONTR** e quando tentar incluir pelo pedido de compras (**MATA121**) vai gerar o help **A120CONTR**.  
  
**Solução**  
Para solucionar essa ocorrência é necessário alterar o campo **B1\_CONTRAT** para **Não** ou **Ambos** no Cadastro do Produto (**MATA010**) ou habilitar o parâmetro **MV\_PRODCTR.**

***Saiba Mais:***

* [MV\_PRODCTR - Incluir no pedido de compras, produto com contrato de parceria](https://tdn.totvs.com/display/public/PROT/MV_PRODCTR+-+Incluir+no+pedido+de+compras%2C+produto+com+contrato+de+parceria)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Help A120CONTR ao incluir um pedido de compra](https://centraldeatendimento.totvs.com/hc/pt-br/search/click?data=BAh7DjoHaWRsKwhnjwvTUwA6D2FjY291bnRfaWRpAy6NDToJdHlwZUkiDGFydGljbGUGOgZFVDoIdXJsSSIBpWh0dHBzOi8vY2VudHJhbGRlYXRlbmRpbWVudG8udG90dnMuY29tL2hjL3B0LWJyL2FydGljbGVzLzM2MDAyMzAzNTc1MS1Dcm9zcy1TZWdtZW50b3MtVG90dnMtQmFja29mZmljZS1Qcm90aGV1cy1TSUdBQ09NLUhlbHAtQTEyMENPTlRSLWFvLWluY2x1aXItdW0tcGVkaWRvLWRlLWNvbXByYQY7CFQ6DnNlYXJjaF9pZEkiKTk0MTRhYmIwLThiMmItNDJkMy1hYTMzLWY1ZWM2ZTI2ZGE2ZAY7CEY6CXJhbmtpBjoLbG9jYWxlSSIKcHQtYnIGOwhUOgpxdWVyeUkiD0ExMjBDT05UUiAGOwhUOhJyZXN1bHRzX2NvdW50aQY%3D--a594da42f4eb0c48f0be7f91125d28a91834b05d)
