---
article_id: 360061108314
category: Materiais - Compras (SIGACOM)
content_hash: a1a30c13d9aa36f590545d018cf93ad2484e6d1c3f506c7fbf4c1f5e76b325f6
fetched_at: '2026-06-28T22:41:24.030352+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Possibilidade para
  não aglutinar o mesmo produto na geração da cotação
type: support-article
updated_at: '2025-11-10T17:42:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061108314-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Possibilidade-para-n%C3%A3o-aglutinar-o-mesmo-produto-na-gera%C3%A7%C3%A3o-da-cota%C3%A7%C3%A3o
---

**Dúvida**

Como seria uma possibilidade para não aglutinar o mesmo produto ao gerar cotação ?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - Todas as versões

**Solução**

Ao inserir uma solicitação de compras, informando o mesmo produto, para que na cotação a ser gerada não ocorra a aglutinação do mesmo produto, no campo: "Necessidade" (C1\_DATPRF), coloque uma data diferente para cada linha,  conforme exemplo do print abaixo:

![Sc_02.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/1500002447421)

Após gerar a cotação e acessar a rotina de "Atualizar cotações", o mesmo produto será apresentado conforme print abaixo, ou seja, o mesmo produto sem aglutinação.

![Ger_02.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/360101293634)

OBSERVAÇÃO :

Caso a Data de necessidade(C1\_DATPRF) seja diferente para todos os itens da Solicitação de compras, também pode ser utilizado o parâmetro como "SIM" abaixo para que sejam aglutinados os produtos:

![im.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17733991448855)

O sistema gera as cotacões a partir das SCs, aglutinando por fornecedor e produto.Em alguns casos esta aglutinacão não pode ser feita a fim de preservar algumas informacões digitadas nas SCs tais como Dt.Necessidade,C.Contabil e C.Custo. Ao selecionar SIM, o sistema unificará a cotacão por produto apenas para facilitar a atualizacão de precos,preservando os dados originais de cada registro da cotacão gerada na gravacão.

**Detalhes sobre a aglutinação da Cotação**

Campos que diferenciam os itens de uma Solicitação de Compras para mesmo código de produto, para que não aglutinem quando é efetuado a geração da Cotação:

**C1\_FILIAL+C1\_GRADE+C1\_FORNECE+C1\_LOJA+C1\_PRODUTO+C1\_DESCRI+DTOS(C1\_DATPRF)+C1\_CC+C1\_CONTA+C1\_ITEMCTA+C1\_CLVL+C1\_FILENT**

**IMPORTANTE:** A funcionalidade de aglutinar é um facilitador no sistema de modo a otimizar a sua operação. Caso as regras atuais dessa funcionalidade não atendam as regras pontuais da sua organização. Recomenda-se realizar cotações individuais para cada solicitação de compras ao invés de aglutinar.

***Pontos de entrada envolvidos no processo :***

**MA131KEY -** <https://tdn.totvs.com/display/PROT/TUCB70_DT_PONTO_DE_ENTRADA_MA131KEY>

**MA131QSC -** <https://tdn.totvs.com/display/PROT/TUCB70_DT_PONTO_DE_ENTRADA_MA131QSC>

**Obs:** Dúvidas na utilização do ponto de entrada acione a equipe advpl.

**Observação**: este procedimento serve apenas para o processo Legado de Cotação do Protheus. Atualmente, no Novo Fluxo de Compras não temos nenhuma tratativa para não aglutinar os itens ao gerar a cotação.

***Saiba Mais :***

[MP - SIGACOM - Como aglutinar produtos na cotação com Entidades Contábeis Diferentes (MV\_COTRATP) ?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006892612)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
