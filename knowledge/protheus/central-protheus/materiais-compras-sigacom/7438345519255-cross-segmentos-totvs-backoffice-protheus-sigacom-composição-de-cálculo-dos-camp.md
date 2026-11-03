---
article_id: 7438345519255
category: Materiais - Compras (SIGACOM)
content_hash: b46a0f09554b9d80a68f783627946e7ba238372123822aaa240f96456c0bfb33
fetched_at: '2026-06-28T22:41:16.128249+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Composição de cálculo
  dos campos: Consumo, Sld.Abast e Nec. Calc da rotina Central de Compras?'
type: support-article
updated_at: '2022-07-13T16:39:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7438345519255-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Composi%C3%A7%C3%A3o-de-c%C3%A1lculo-dos-campos-Consumo-Sld-Abast-e-Nec-Calc-da-rotina-Central-de-Compras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **02:MM**

**Dúvida**  
Como funciona as informações dos campos: Consumo, Sld. Abast. e Nec. Calc,  da rotina Central de Compras?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Compras - Todas as versões]  
  
**Solução**

A demonstração do cálculo utilizando a quantidade 6 apenas como exemplo.

Na rotina MATA220-Cadastro de saldo inicial, cujo produto considerando o saldo inicial = 6

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7439093326359/mceclip0.png)

No cadastro de produto, o campo B1\_ESTSEG estiver preenchido com a quantidade = 6

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7439083226391/mceclip1.png)  
  
Houver movimentação de quantidade 2, no qual o saldo atual será = 4

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7439155575319/mceclip2.png)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7439161833239/mceclip3.png)  
  
Ao visualizar, será apresentado a tela com a composição dos campos marcados tais como:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7439275258391/mceclip4.png)

O campo CONSUMO com a informação de 2,20, refere-se à movimentação de saída, demonstrada no Kardex com a quantidade de 2 + 10% informada no campo: Increm (%) e dias Cobert. na rotina de Sugestão de Compras.

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7439376097559/mceclip6.png)  
  
O campo Sld Abast com a informação de -2,00 é composto da seguinte forma:  
B9\_Qtd.Ini.Mês - Saldo Inicial = 6   
(-) Movimentaçao / saída = 2 ( Demonstrada no Kardex )  
B2\_QATU - Saldo Atual = 4 ( Demonstrado no Kardex )  
Devido ao campo B1\_EstNeg - Segurança ( Cadastro de Produto ), estar preenchido com 6, indica que para atingir seu estoque de segurança, existe a necessidade de abastecer com mais 2 quantidades. Sendo assim o cálculo é baseado no saldo atual porém considerando o estoque de segurança = 6.

O campo Nec. Calc com a informação de 4,20, é composto da soma dos campos Consumo + Sld Abast, totalizando 4,20

**SAIBA MAIS EM :**

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
