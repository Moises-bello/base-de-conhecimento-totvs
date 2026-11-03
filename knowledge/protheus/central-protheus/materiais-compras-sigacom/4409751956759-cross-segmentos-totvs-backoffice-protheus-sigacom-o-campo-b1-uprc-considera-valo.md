---
article_id: 4409751956759
category: Materiais - Compras (SIGACOM)
content_hash: 4ddfd146c678b9203c9e6871b8e9f4e41a5e2e020871d33a7a94b97a944d62d3
fetched_at: '2026-06-28T22:41:21.961475+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - O campo B1_UPRC considera
  valor de impostos e frete?
type: support-article
updated_at: '2022-12-06T13:25:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409751956759-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-O-campo-B1-UPRC-considera-valor-de-impostos-e-frete
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:00** **Dúvida**

O campo B1\_UPRC , (último preço de compra) , do Produto considera valor de Impostos e Frete?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras - Todas as versões  
  
**Solução**

O campo B1\_UPRC,   considera apenas o **valor unitário**, sendo assim, não considera valor de impostos e frete.

Para que o campo B1\_UPRC seja atualizado no cadastro de produto é necessário informar o campo: F4\_UPRC = Sim, no cadastro de TES, conforme exemplo abaixo:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409752722583/mceclip2.png)

Ao inserir um documento de entrada, o campo Ult.Preço, será atualizado sempre com o último valor unitário informado.  Exemplo para o produto abaixo, o último preço gravado havia sido 700,00

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409752511895/mceclip0.png)

Ao incluir um novo documento de entrada com o valor unitário de 1.000,00

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409757756311/mceclip4.png)

O produto foi atualizado conforme último preço unitário, **sem o considerar o valor do frete ou impostos**.

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409752876951/mceclip5.png)

OBS :

O documento de entrada possui uma funcionalidade que permite atualizar o último preço de compra do produto no momento da inclusão.  
Dentro dela existe um ponto de entrada chamado MT103UPC flexibilizando o processo de composição do último preço 

![image.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10753122920215)

***Saiba Mais :***

[MT103UPC - Manipula campo "Ultimo Preço de Compra"](https://tdn.totvs.com/x/Stxc)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
