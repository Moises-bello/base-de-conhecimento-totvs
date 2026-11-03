---
article_id: 360061261834
category: Financeiro - Contas a Pagar
content_hash: f168f3bdaa6e8ebe632b2a7e511d81cebe686594d29dc430e6f62b28fd0f90f3
fetched_at: '2026-06-28T22:38:09.805341+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Projeção Moedas com
  casas decimais diferentes '
type: support-article
updated_at: '2023-03-06T17:09:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061261834-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Proje%C3%A7%C3%A3o-Moedas-com-casas-decimais-diferentes
---

**Dúvida**No cadastro de moeda, na opção projetar, na imagem está somente com três casas decimais, sendo que no dicionário está com quatro casas decimais.

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002636121/mceclip2.png)  
  
**Ambiente**Microsiga Protheus - Financeiro - MATA090 -  versão 12  
  
**Solução**O campo que é usado na projeção não é o apresentado em tela, é usado para o calculo e salvo, o campo que se vê na tela já é a taxa da moeda, para mostrar 4 casas decimais é necessário aumentar o M2\_TXMOED2, o campo que aparece no browser é o M2\_MOEDA2.  
Nesse campo tem que digitar o valor da taxa que deseja aplicar para os cálculos de projeção ou regressão, caso ele deseje aumentar a precisão dessa taxa, ele deve aumentar o tamanho do campo forme a o link abaixo.  Esse campo não é o mesmo do campo MOEDA.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360103643133/mceclip3.png)

**Saiba mais**Foi realizado uma correção em relação a picture do campo para representar o campo correto que é o TXMOED...  onde esse é criado originalmente com tamanho 3.  
[MP - SIGAFIN - TAXA DA MOEDA - Como alterar a quantidade de Casas Decimais de moeda estrangeira no módulo SIGAFIN](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034970673-MP-SIGAFIN-TAXA-DA-MOEDA-Como-alterar-a-quantidade-de-Casas-Decimais-de-moeda-estrangeira-no-m%C3%B3dulo-SIGAFIN?source=search)

<https://tdn.totvs.com/x/Y_gpIQ>
