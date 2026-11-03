---
article_id: 30885730484503
category: SIGAEST - CUSTOS
content_hash: 01feeee2a4232e6f82fb519cdff992217b4bc872ff45621ec239065832e9d211
fetched_at: '2026-06-28T22:39:00.767500+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como movimentar um
  produto sem calcular custo?
type: support-article
updated_at: '2025-04-07T13:56:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30885730484503-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-movimentar-um-produto-sem-calcular-custo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30885713771799) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Como posso fazer uma movimentação no estoque sem que a mesma calcule o custo?   
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução:**

Para que um produto seja movimentado internamente sem que haja o cálculo de custo (**B2\_CM1**), é necessário que ele **NÃO** possua custo inicial nem custo histórico registrado.

Matematicamente, caso o produto já tenha um registro de custo histórico, qualquer movimentação de requisição/devolução assumirá esse custo, resultando em uma movimentação custeada. 

Por exemplo, uma movimentação interna de requisição pode ser calculada pelo campo B2\_CM1 ou inserido um custo manual conforme nossas documentações:

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como é calculado o campo D3\_CUSTO1 ao efetuar Movimentos Internos?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005527161-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-%C3%A9-calculado-o-campo-D3-CUSTO1-ao-efetuar-Movimentos-Internos)

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Acerto de Custo dos Produtos em Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057292614-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Acerto-de-Custo-dos-Produtos-em-Estoque)

**Formas de movimentação sem custo**

Um produto poderá ser movimentado sem custo nas seguintes condições:

1. **O produto nunca pode ter tido custo registrado:**  
   O produto não pode possuir nenhum histórico de custo, seja inicial ou acumulado em movimentações anteriores.
2. **Movimentação via Ponto de Entrada.**  
   Pode ser implementado um **Ponto de Entrada**  que controle essa movimentação e impeça a aplicação do custo nas operações internas. [Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Pontos de Entrada da rotina Recálculo do Custo Médio](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003970802-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Pontos-de-Entrada-da-rotina-Rec%C3%A1lculo-do-Custo-M%C3%A9dio)

**Saiba mais:**

***[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)***
