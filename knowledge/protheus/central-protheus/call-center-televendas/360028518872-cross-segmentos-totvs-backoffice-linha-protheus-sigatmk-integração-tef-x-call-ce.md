---
article_id: 360028518872
category: Call Center - Televendas
content_hash: 3256c139d0af192a7e02e00895c769d474e8888feeacd7341b42551dcc69b4d2
fetched_at: '2026-06-28T22:41:30.330826+00:00'
product: protheus
section_id: 1500001537121
source: central-protheus
title: Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK-Integração TEF x
  Call Center
type: support-article
updated_at: '2022-06-22T19:09:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028518872-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGATMK-Integra%C3%A7%C3%A3o-TEF-x-Call-Center
---

**Dúvida**

Como efetuar a integração de pagamento via TEF no Call Center?  
  
**Ambiente**

Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGATMK - todas as versões.

**Solução**  
Para configurar a integração de TEF para o Call Center, necessário efetuar as parametrizações abaixo:

1- Parâmetros:

**- MV\_Autocom = 1**  
**- MV\_Emptef= 00000000**  
**- MV\_Opfat=S**

2- Cadastrar a estação (**TMKA121**) no módulo Call Center  e ativar o uso da opção Clisitef;

3- Incluir a estação cadastrada no grupo de atendimento(**TMKA040**);

4- Associar o grupo de atendimento (com a estação em questão) ao cadastro do operador (**TMKA090**);

5- Cadastrar uma condição de pagamento (**MATA360**)com a forma de pagamento cartão de crédito;

6- Cadastrar a Administradora Financeira (**LOJA070**);

7-Efetue um atendimento televendas (**TMKA273**) do tipo faturamento utilizando a condição com forma de pagamento Cartão de Crédito:

![atendimento_televendas_com_tef.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360029460211/atendimento_televendas_com_tef.gif)

Para visualização das telas de cadastros e observações do uso da venda, acesse: **[TMK0072 Integração TMK x TEF](http://tdn.totvs.com/pages/viewpage.action?pageId=494964084#)**
