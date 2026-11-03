---
article_id: 360021775612
category: Materiais - Compras (SIGACOM)
content_hash: 635732e30381aa3f931532245a8d2e4014cc7116151b931fcc3546682cf83f16
fetched_at: '2026-06-28T22:41:18.912352+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Help FA050BAIXA na
  Exclusão do Documento de Entrada
type: support-article
updated_at: '2023-03-07T18:05:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360021775612-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Help-FA050BAIXA-na-Exclus%C3%A3o-do-Documento-de-Entrada
---

**Ocorrência**

Help FA050BAIXA na Exclusão do Documento de Entrada  
  
**Ambiente**

Microsiga Protheus – Compras – A partir da versão 11.80  
  
**Causa**

Para que a mensagem FA050BAIXA não seja mostrada quando se utiliza o financeiro compartilhado, terá que ter as tabelas abaixo compartilhadas.  
  
**Possíveis soluções :**

1- )Tabelas a ser compartilhada para que considere o Pedido X Adiantamento

(FIE - Relacionamento Pedidos X Adiantamento)

(FR3 - Relacionamento Pedidos X Compensação)

Tabelas envolvidas no processo:

​FIE, FR3, FK1, FK2, FK3, FK4, FK5, FK6, FK7, FK8, FK9, FKA, SE1, SE2, SE5

2- ) Tabelas a serem observados o conteúdo:

No(s) título(s) a pagar gerado(s) a partir da nota de entrada que precisa ser excluída, verifique como estão os conteúdos dos campos : E2\_BAIXA e E2\_SALDO pode haver alguma informação de baixa nos títulos a pagar.

Verificar se a baixa foi cancelada, se existe registro deste cancelamento na tabela FK2, pois o help é exibido quando o sistema somente localiza o movimento de baixa dentro da FK2 e não localiza o movimento do estorno/cancelamento/exclusão da baixa. 

**IMPORTANTE** :

Se em seu ambiente o sistema estiver pemitindo a exclusão de um documento de entrada, mesmo com títulos baixados no financeiro, verifique se o processo de baixa gerou movimento na tabela FK2 ( movimentação gerada por padrão do sistema ), pois para permitir ou não a exclusão da NFE ( executado pelo fonte FINXAPI ) **o sistema verifica os conteúdos dos campos FK2\_VALOR com o E2\_VALOR, se forem diferentes, é porque houve alguma inconsistência no momento da realização da baixa e por isso, a exclusão ocorreu. Os campos de IDDOC também são verificados para a localização dos movimentos dentro das tabelas FK´s.**

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
