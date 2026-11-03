---
article_id: 4411317045271
category: Materiais - Compras (SIGACOM)
content_hash: 90558cc6a43c0fb559b5137c999dee2be30dc579e95b282a878f61595e08d438
fetched_at: '2026-06-28T22:41:15.865346+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como fazer a entrada
  de uma Devolução Compra ( NF Saida ) que não foi aceita pelo fornecedor ?
type: support-article
updated_at: '2022-10-26T13:55:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4411317045271-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-fazer-a-entrada-de-uma-Devolu%C3%A7%C3%A3o-Compra-NF-Saida-que-n%C3%A3o-foi-aceita-pelo-fornecedor
---

**Dúvida**Fiz a compra de um material e tive que realizar a devolução dele porém o fornecedor não aceitou a devolução (seja por divergência de acordo comercial ou erro de emissão de nota fiscal).

Como fazer a entrada dessa devolução para que seja possível refazer a devolução corretamente?

**OBS: CASOS EM QUE IRÁ RETORNAR NOTA FISCAL E PRODUTO**  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - Todas as versões

**Solução**

Por padrão não temos o conceito de dar entrada em uma devolução sendo o próprio documento uma devolução.  
  
Porém um paliativo nesse sentido seria:

-Fazer a entrada da nota fiscal como tipo "N"

- Puxar o cadastro de fornecedor normalmente

-Digitar as informações normalmente de produto, valor e quantidade  
-No campo nota fiscal origem na linha do item informar a nota origem e série origem, **somente de forma informativa**, digitar os números da nota e série da nota de devolução (que está querendo cancelar).

Essas informações serão somente informativas.

Sendo assim o modo paliativo acima atenderia a necessidade.

Veja a documentação abaixo sobre esses casos:  
  
[O fornecedor pode recusar o recebimento do produto?](https://www.totvs.com/blog/gestao-varejista/devolucao-de-mercadorias/#:~:text=Mandar%20um%20produto%20adquirido%20de,quanto%20um%20retorno%20de%20mercadoria.&text=Ele%20se%20recusar%20a%20receber,fiscal%20emitida%2C%20entre%20outros%20motivos)  
  
![](https://totvssuporte.zendesk.com/attachments/token/8pmnG1ZHu6A9pT3Qd7t6WbJGL/?name=inline-1603593919.png)​  
  
Para fazer uma nova entrada deve fazer outro pedido de compra , refazer a entrada e assim gerar uma devolução correta.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
