---
article_id: 1500009602461
category: Materiais - Compras (SIGACOM)
content_hash: a2de010f0f17fb59a9bc60a0cd101dbb000b20a28fe4b420d65c058d459565eb
fetched_at: '2026-06-28T22:41:18.781578+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Help " FINA050 - CONTAS
  A PAGAR - O título XXXXXXX NF XXXXXX possui movimentos sem contabilização " ao tentar
  excluir uma Documento de Entrada - MATA103
type: support-article
updated_at: '2022-10-19T21:08:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500009602461-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Help-FINA050-CONTAS-A-PAGAR-O-t%C3%ADtulo-XXXXXXX-NF-XXXXXX-possui-movimentos-sem-contabiliza%C3%A7%C3%A3o-ao-tentar-excluir-uma-Documento-de-Entrada-MATA103
---

**Dúvida**

Por que na Exclusão do Documento de Entrada o sistema apresenta o Help " FINA050 - CONTAS PAGAR - O TÍTULO XXXXXXX NF XXXXXX possui movimentos sem contabilização "  ?

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500014666242/mceclip0.png)

**Ambiente :**Cross Segmento - Protheus - COMPRAS - A partir da versão 12.

**Solução :**

O help informa que o número do título a pagar, pertencente a NF que precisa ser excluída, possui algum movimento efetuado que não está devidamente contabilizado.

Dentro das tabelas que envolvem o contas a pagar, temos a SE2 (que é a do título), a SE5 (que grava as movimentações efetuadas nos títulos, baixas ou cancelamentos de baixas) e ainda existem as tabelas FKX (X = ao número da tabela, por exemplo FK1, FK2...).

[Tabelas FK´s no financeiro](https://tdn.totvs.com/pages/releaseview.action?pageId=183730415)

Nas tabelas do financeiro, SE2 e SE5, existe o campo LA, são eles : E5\_LA e E2\_LA, que são marcados quando o movimento de contabilização é efetuado naquele registro/título. 

Sendo assim, para correção do HELP verificar os campos:

Na tabela SE5, é necessário a contabilização da baixa E5\_LA=S e a contabilização do estorno da baixa E5\_LA=S, ou seja, todos os movimentos efetuados no(s) título(s) da nota que precisa ser excluída, precisam estar contabilizados, com o campo E5\_LA = Sim..

No padrão do sistema temos Lançamentos Padrão para as inclusões e também para as exclusões e/ou cancelamentos.

Logo, quando há a contabilização de uma inclusão de um título ou de uma baixa referente a esse título e, essa é devidamente contabilizada, quando ocorre a exclusão do título ou exclusão/cancelamento da baixa desse título também é necessário ter o LP correspondente devidamente configurado.

Essa regra vale também como por exemplo, para  o documento de entrada, onde utilizamos o LP 650 para a contabilização dos itens da nota  de entrada no momento da inclusão e o LP 655 para a exclusão dos itens da nota de entrada.

[Lançamentos padrão do compras](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027616491-MP-SIGACOM-Contabiliza%C3%A7%C3%A3o-Compras-Quais-Lan%C3%A7amentos-Padr%C3%B5es-e-como-funciona-)

[Lançamentos padrão do financeiro](https://tdn.totvs.com/pages/releaseview.action?pageId=235585410)

Como o sistema valida a movimentação de contabilização em todos os processos, quando o help for exibido será necessário efetuar as verificações mencionadas acima.

Ou seja :

1) Se há LP devidamente configurado para todos os processos que envolvem o título a pagar, baixa e cancelamento/exclusão da baixa.

2) Se dentro da tabela  SE5 em todos os movimentos desse título os campos de LA estão marcados com S.

**Ponto de entrada envolvido no processo.**

[FA050DEL - Confirmação de exclusão de títulos](https://tdn.totvs.com/pages/releaseview.action?pageId=6071105)

**Obs:** Dúvidas em pontos de entrada acionar equipe Protheus Advpl.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA DE COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras ( SIGACOM )](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
