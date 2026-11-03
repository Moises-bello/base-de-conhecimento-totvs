---
article_id: 360039765493
category: FATURAMENTO - PEDIDO DE VENDAS
content_hash: dca911d4bc5d9c4cc7beed6abd1470cad84a4b1b6d903d6580d4166b02412344
fetched_at: '2026-06-28T22:38:41.286207+00:00'
product: protheus
section_id: 1500001550322
source: central-protheus
title: MP-FAT-arrayounds ( 0 of 118 )  on A410LOTCTL(MATV410A.PRW)
type: support-article
updated_at: '2025-10-14T14:37:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039765493-MP-FAT-arrayounds-0-of-118-on-A410LOTCTL-MATV410A-PRW
---

**Ocorrência**

Após dar enter+F4 no campo **c6\_lotectl** do pedido de venda (**Mata410**) para a escolha do lote, escolher e confirmar o número de lote para o preenchimento do campo, quando clica em enter para sair do campo com o lote já preenchido, o sistema gera error.log com a mensagem abaixo:

**array out of bounds ( 0 of 118 ) on A410LOTCTL(MATV410A.PRW) 12/09/2019 10:35:53 line : 4369**

**Ambiente**

Microsiga Protheus - todas as versões.  
   
 **Causa**

O erro de array out of bounds significa que o campo chamado no array ou não existe na base de dados/e ou sx3, não está marcado como usado ou teve o nível de campo mudado do padrão.

Neste caso,o sistema aponta para o campo  **C6\_LOCALIZ** que pode não estar com o seu uso marcado ou ter tido o seu nível de campo mudado do padrão.

Campos que também fazem parte do array e que podem gerar o erro caso não exista no banco de dados e dicionário de dados, ou não tenha seu uso marcado ou tenha seu nível de campo mudado: **C6\_NUMLOTE** e **C6\_LOTECTL**.

**Solução**  
 Para solucionar essa ocorrência, realize os seguintes passos:

1. Via configurador, acesse Dicionário, Base de Dados,Dicionário de Dados ;

2. Localize a tabela **SC6** e edite;

3. Dentro da tabela **SC6**, localize o campo em questão, e deixe o nível de campo igual a 1, e marque a opção usado.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360051693194/mceclip0.png)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360051693234/mceclip1.png)

4.Salve as alterações e atualize o dicionário de dados.

5.Reinicie o Smartclient para que as configurações surtam efeito no sistema.

**Obs...na release 12.1.25, por padrão de dicionário de dados,  as opções de nível de campo e usado, não podem ser alteradas, já vem configurados conforme as imagens acima.**
