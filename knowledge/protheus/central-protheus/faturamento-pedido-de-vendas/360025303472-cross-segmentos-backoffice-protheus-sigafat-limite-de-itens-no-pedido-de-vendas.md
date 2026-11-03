---
article_id: 360025303472
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: ef2485ef8e176b40794c2a193a1b9122c58db18349121a489aa15570fc7ac8a7
fetched_at: '2026-06-28T22:38:39.875142+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Limite de itens no Pedido
  de Vendas e Documento de saída
type: support-article
updated_at: '2026-06-03T18:20:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025303472-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Limite-de-itens-no-Pedido-de-Vendas-e-Documento-de-sa%C3%ADda
---

**Duvida**  
Qual o limite de itens no Pedido de Vendas e Documento de saída?  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT - A partir da release 12  
  
**Solução**  
**Limite de Itens - Pedido de Vendas**  
O limite permitido para inserção de itens em um Pedido de Vendas com grade é de 300 itens. Isso porque, o pedido de venda utiliza um objeto chamado getdados para compor as linhas e armazenar as informações, e como se utiliza a configuração de produto com grade na rotina (MATA410), e esta configuração possui 3 posições; como uma matriz, o limite de 999 itens é dividido por 3,33, limitando a quantidade de itens permitido.

* Limite com grade = 300 itens
* Limite sem grade = 999 itens

**Limite de Itens - Documento de Saída**  
O limite de itens na Nota de saída seguem o padrão do Sefaz. Há uma limitação do próprio SEFAZ de que a Nota eletrônica deve possuir um limite de 990 itens.

Outra informação que é necessário atentar-se, é o parâmetro **MV\_NUMITEN**, onde pode ser configurado o número máximo que deseja permitir de itens por Nota fiscal (respeitando os 990 de limite), para controlar a quebra de Nota automaticamente. Deve estar com um conteúdo que comporte a quantidade de itens dos Pedidos a Faturar.

**Considere:**

* Os campos **C6\_ITEM** e **D2\_ITEM**são alfanuméricos, assim, ao alcançar o limite de números, são feitas novas combinações com letras, não se fazendo assim necessário aumentar o tamanho dos campos que atualmente é de 2 dígitos;
* Os mesmos não são habilitados no Configurador **SIGACFG** para alteração de tamanho, ou alterações em campo conforme regras do cliente; sendo exclusivos de controle do Protheus (Campo **C5\_NUM** com 6 dígitos entra nesse mesmo critério);
* O suporte não orienta alterações em Base de Dados, alterações na Base podem comprometer a integridade do sistema. A orientação é que inclua um novo Pedido / Nota ao completar o limite.

Caso necessite de uma quebra personalizada de itens na nota, avalie o tratamento através do ponto de entrada **M460QUEB:** [**https://tdn.totvs.com/x/xoRn**](https://tdn.totvs.com/x/xoRn)

**Na transmissão:**

No manual do contribuinte informa que o tamanho máximo do XML é de 500k, caso passe desse tamanho a SEFAZ rejeitará com erro 214 "Tamanho do XML de Dados superior a 500 KB".

Não há um numero exato de itens para que a nota seja autorizada, o que influencia é a quantidade de informações existentes na NFE, obviamente quanto mais itens maior a quantidade de informação.  
  
Caso o total de itens na nota fiscal passe de 500kb será necessário dividir essa pedido em mais notas.  
  
**OBSERVAÇÃO:** Já relacionado em quantas notas que precisa separar, não há como informar com precisão, uma vez que cada item contribui com diferentes tamanhos de bytes no conteúdo do XML, por exemplo os itens possui diferentes quantidades de caracteres na descrição, isto dificulta informa-lo em quantas notas separar.  
  
O parâmetro MV\_NUMITEN faz automaticamente a divisão dos pedidos por quantidade de itens, exemplo: MV\_NUMITEN = 35, ao faturar com 80 itens, ele irá dividir em três notas, sendo 2 notas com 35 itens cada, e a terceira nota com as 10 faltantes.

* Dúvidas nas informações da transmissão acima, contate a Equipe Protheus SPED!

**Saiba mais:**

[**Limite para inclusão de Itens no Pedido de Vendas e no Documento de Saída NF**](https://tdn.totvs.com/x/5Cr2Dw)
