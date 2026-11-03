---
article_id: 360022702531
category: Materiais - Compras (SIGACOM)
content_hash: 1deac4bdbc9df1895cda5bc6ee75bd86f0f3c425b84e24398f0c87a7b56acd7f
fetched_at: '2026-06-28T22:41:08.836442+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Em qual momento é apresentado
  o Help A103F4 ?
type: support-article
updated_at: '2025-10-22T14:01:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022702531-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Em-qual-momento-%C3%A9-apresentado-o-Help-A103F4
---

**Dúvida**Em qual situação é apresentado o Help A103F4 ?

**Ambiente**Cross Segmento - TOTVS Backoffice (Protheus Compras) – A partir da versão 12

**Solução:**

O Help em questão (**A103F4**) é apresentado quando o sistema não localiza o pedido, considerando algumas verificações :

**1-) O Fornecedor e loja em questão.**

Por exemplo, o pedido de compras é feito para o fornecedor XXXXXX e a loja do fornecedor XX., porém a nota foi emitida pelo fornecedor XXXXX porém a loja do fornecedor é a YY.

Nesse caso é necessário verificar a pergunta no F12 da MATA103 ( documento de entrada ). Ou, caso a nota seja incluída pela rotina MATA140 ( pré nota ).

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35804860076695)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35804860079127)

**2-) Quando a filial de entrega do pedido é diferente da filial em que a nota de entrada, está sendo incluída.**

Por exemplo um Pedido de compras foi incluído na filial 01, porém com filial de entrega 02.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35804860080023)

Para que o sistema localize esse pedido de compras é necessário incluir a nota de entrada, posicionado na filial 02.

**Observação :**

Ao utilizarmos o conceito de filial de entrega somente a filial de entrega pode associar o pedido de compras ao documento de entrada.A entidade remetente somente emite o pedido, onde não possui registro local do pedido **C7\_FILENT**(número da filial de entrega), pois sua  visualização / alteração são feitos da filia de entrega, analise o parâmetro **MV\_PCFILEN** e o campo **C7\_FILENT** .Abaixo maiores explicações sobre o parâmetro:

* Se o SC7 está com o X2\_MODO como compartilhado, o ***MV\_PCFILEN*** deve obrigatoriamente estar preenchido = F (por empresa) e o controle de numeração de PC's vai ser por empresa, o ***C7\_FILENT*** ficará em branco e o campo FILIAL DE ENTREGA do cabeçalho do Pedido de Compras não permitirá digitação;
* Se o SC7 está com o X2\_MODO como exclusivo e o ***MV\_PCFILEN***for igual a F, o PC também não permite a digitação da filial de entrega (assume a filial corrente) e a numeração do PC vai ser controlada por filial, neste caso o ***C7\_FILENT*** será gravado com a filial corrente;
* Já se o SC7 for exclusivo no X2\_MODO e o ***MV\_PCFILEN***for igual a T, o PC permite a digitação da filial de entrega no cabeçalho e o controle da numeração do PC vai ser por empresa, neste caso o ***C7\_FILENT*** passará a ser gravado com a filial indicada no cabeçalho do PC.

**3-) Ou ainda quando utilizamos o processo de entrega por terceiros, porém o fornecedor que entregará o pedido não é localizado. Isso pode ocorrer de duas formas :**

3A-) O fornecedor entregador não está cadastrado no cadastro de entrega por terceiros.

[**Processo de entrega por terceiros**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004980311-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Processo-de-Entrega-Por-Terceiros)

3B-) Na entrada da nota, não foi selecionado o fornecedor correto no vínculo do Pedido de compras.

No exemplo abaixo, o fornecedor que enviou a mercadoria é o 000003 loja 01, e no pedido de compras, o fornecedor é o 000001 loja. Ambos estão amarrados no cadastro de entrega por terceiros.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/35804889238039)

***Saiba Mais***

[MP - SIGACOM - Qual o conceito do MV\_PCFILEN e sua interferência na numeração do Pedido de Compras?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022158251)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
