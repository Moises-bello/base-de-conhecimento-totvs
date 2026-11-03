---
article_id: 360035996833
category: PCO - Planilhas
content_hash: 9079b8611301c53e36bb958b6078006af3c35948ce3dd3818e33b45b98e0605b
fetched_at: '2026-06-28T22:37:05.407404+00:00'
product: protheus
section_id: 1500001539901
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAPCO -Bloqueio com controle
  por planilhas Orçamentária.
type: support-article
updated_at: '2026-03-03T17:45:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035996833-Cross-Segmento-Backoffice-Linha-Protheus-SIGAPCO-Bloqueio-com-controle-por-planilhas-Or%C3%A7ament%C3%A1ria
---

**Dúvida**Como controlar o PCO usando mais de uma planilha?  
  
  
**Solução**

No exemplo a seguir usaremos uma planilha com saldo orçado anual e uma com saldo orçado mensalmente.

1 - Configurar o lançamento do processo 000252 na rotina PCOA030

![processo000252.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/4459962629399/processo000252.PNG)

[MP - SIGAPCO - Configuração on-line dos lançamentos por processo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018567972-MP-SIGAPCO-Configura%C3%A7%C3%A3o-on-line-dos-lan%C3%A7amentos-por-processo?source=search)

2 - Cadastrar planilha anual

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047116093/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046250534/mceclip1.png)

Após a gravação o lançamento será gerado na AKD com base na configuração do processo 000252

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047116253/mceclip2.png)

3 - Cadastrar a planilha mensal

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046250674/mceclip3.png)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047116373/mceclip4.png)

Lançamentos gerados na AKD com base na configuração do processo 000252

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046250794/mceclip5.png)

4 - Configurar o Cubo Gerencial

[MP - SIGAPCO: Exemplo de como configurar um Cubo Gerencial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018810031-MP-SIGAPCO-Exemplo-de-como-configurar-um-Cubo-Gerencial?source=search)

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046250814/mceclip6.png)

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047116473/mceclip7.png)

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047116593/mceclip8.png)

5 - Configurar o Tipo de Bloqueio

![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047116653/mceclip9.png)

6 - Configurar lançamento por processo (exemplo processo 000052)

![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047116713/mceclip10.png)

7 - Configurar o lançamento de bloqueio

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047116773/mceclip11.png)

8 - Configurar o ponto de bloqueio

![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047116813/mceclip12.png)

9 - Configurar lançamento de liberação de contingência

Item 01

![mceclip13.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047116893/mceclip13.png)

Item02

![mceclip14.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047116933/mceclip14.png)

10 - Cadastrar aprovadores e Limites de aprovação

![mceclip15.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046251214/mceclip15.png)

![mceclip16.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047116993/mceclip16.png)

11 - Fazer pedido de compra para Conta orçamentária orçada e informar a planilha anual (fazer com valor maior que o orçado na planilha mensal)

![mceclip17.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047117013/mceclip17.png)

12 - Sistema apresenta o lançamento de bloqueio para a planilha Anual.

![mceclip18.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047117053/mceclip18.png)

 13 – Sistema efetua o lançamento com base na planilha anual

![mceclip19.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046251414/mceclip19.png)

Não ocorre bloqueio corretamente, o valor do lançamento é maior que o orçado mensal mas foi feito para o orçado anual, o controle é feito com base na planilha informada.

14 - Fazer um lançamento do mesmo valor R$1500,00, mas para planilha mensal que somente orçamos para janeiro R$1000,00.

15 - Irá gerar um lançamento de bloqueio para o orçamento mensal no valor de R$1500,00.

![mceclip20.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047117133/mceclip20.png)

16 – O sistema efetuará o bloqueio com base na planilha com orçamento mensal corretamente, um orçamento mensal do 1000,00 e um pedido de 1500,00 necessidade de 500,00 para solicitação de contingência.

![mceclip21.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046251514/mceclip21.png)
