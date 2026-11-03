---
article_id: 7317584256919
category: Materiais - Compras (SIGACOM)
content_hash: 4d183c5d7c55b05f07f79c7e2873050b17d34eb6fd305dad4998c3255d599b4a
fetched_at: '2026-06-28T22:41:16.176344+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Controle de Alçada
  - Bloqueio de Títulos referente a Pedido com Adiantamento
type: support-article
updated_at: '2026-05-29T19:12:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7317584256919-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Controle-de-Al%C3%A7ada-Bloqueio-de-T%C3%ADtulos-referente-a-Pedido-com-Adiantamento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/40833994616215) Tempo aproximado para leitura: **00:02:00 min**  
  
**Dúvida**

Quando utilizado o controle de alçadas o pedido de compras fica com bloqueio aguardando as aprovações, mas o título PA no financeiro fica ativo/liberado para que a área financeira trabalhe com este título. Nos casos em que o pedido de compras não é aprovado, gera um retrabalho de estornar os processos.

**Ambiente**

Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS - Versão 12

**Solução**

Para utilizar as funcionalidades implementadas é necessário criar o parâmetro MV\_BLQPAPC

![mvv.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7317509339031)

**FUNCIONALIDADE :**

1 - Bloqueio do título (Liberação para Baixa - FINA580) junto com o pedido, quando utilizar alçada e Pedido estiver bloqueado.   
2 - Desbloqueio do título automaticamente quando ele estiver associado ao pedido de compras  
3 - Não permitir liberar um título vinculado a um pedido de compras bloqueado.

***Obs:***

Para o uso desta funcionalidade, se faz necessário estar ativada a funcionalidade de "Liberação pra Baixa" (FINA580) do artigo abaixo do Módulo Financeiro (SIGAFIN):

[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA580 - Como utilizar a rotina liberação para baixa](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016596851-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA580-Como-utilizar-a-rotina-libera%C3%A7%C3%A3o-para-baixa)

Para dúvidas no processo de "Liberação para Baixa (FINA580)" do artigo acima do módulo Financeiro, orientamos o contato junto ao suporte ao SIGAFIN para o apoio.

***Saiba Mais:***

[Parâmetro MV\_BLQPAPC - Controle de Alçadas Pedido de Compras com Adiantamento BRA](https://tdn.totvs.com/x/QtthE)

[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA580 - Como utilizar a rotina liberação para baixa](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016596851-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA580-Como-utilizar-a-rotina-libera%C3%A7%C3%A3o-para-baixa)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
