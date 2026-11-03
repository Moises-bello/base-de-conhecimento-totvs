---
article_id: 4409018204951
category: Materiais - Compras (SIGACOM)
content_hash: f3654dffa5198b8be00a67bbb4fd6b3ee7679e8b13bcb988879c9328a586c9c3
fetched_at: '2026-06-28T22:41:13.133755+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Alteração do campo
  E2_NATUREZA no título a pagar gerado por um documento de entrada
type: support-article
updated_at: '2022-05-16T22:56:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409018204951-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Altera%C3%A7%C3%A3o-do-campo-E2-NATUREZA-no-t%C3%ADtulo-a-pagar-gerado-por-um-documento-de-entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **HH:MM:SS min** **Dúvida**Sistema não permite alterar o campo ***E2\_NATUREZA*** no título a pagar gerado a partir de um documento de entrada.

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Compras - Todas as versões  
  
**Solução**Após análise em conjunto com a equipe do financeiro (contas a pagar), ao tentarmos alterar o campo Natureza no título a pagar, verificamos algumas situações, as quais relatamos abaixo :

1- Os títulos a pagar com origem no módulo do compras sempre serão incluídos na tabela SE2 com o campo E2\_LA = Sim, pois a contabilização ocorre pela nota de entrada.

Logo, mesmo o campo estando aberto para alteração da natureza, ela não será permitida por conta dessa regra e ao tentar será emitido o help TITCONTAB.

![](https://totvssuporte.zendesk.com/attachments/token/NFm3g6eu70TQ7AJ8awDw5bjiR/?name=inline-152328773.png)​  
![](https://totvssuporte.zendesk.com/attachments/token/kGpAS7BgnERAQgzHwNM3NR5Dm/?name=inline953303750.png)​  
  
  
2- Quando a natureza utilizada no documento de entrada e levada para o título a pagar, possuir algum campo para o cálculo de  imposto configurado como Sim, conforme print abaixo, por padrão a rotina FINA050 na opção alterar não habilitará o campo E2\_NATUREZA para alteração, pois títulos que possuem impostos não podem ter a natureza alterada.  
![](https://totvssuporte.zendesk.com/attachments/token/gRF2iJaZlkaf2nL6RG82xdSjP/?name=inline626385864.png)​  
![](https://totvssuporte.zendesk.com/attachments/token/hvMFZYdh8GLgyVhAF9OfMsm6K/?name=inline-118865839.png)  
![](https://totvssuporte.zendesk.com/attachments/token/NyHBEMtQj6wvqAl8BSF5IlDue/?name=inline-1577671228.png)  
  
Baseado nessas análises o processo correto para correção no título a pagar seria a exclusão da nota de entrada e novo lançamento com a natureza correta.

Não identificamos ponto de entrada para efetuar essa alteração em nenhuma das situações.

***Saiba Mais :***

*[PÁGINA CENTRALIZADORA DO COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)*

*[Mais Artigos Materiais - Compras ( SIGACOM )](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)*
