---
article_id: 25336198209815
category: SIGAEST - CÁLCULOS
content_hash: 06e2cb286ba6729c70b79a7187e1de8cb9563ab0dd232e6a6e866e1abc788970
fetched_at: '2026-06-28T22:39:04.178868+00:00'
product: protheus
section_id: 1500001550082
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATC010 - Quantidade
  na Formação divergente da Estrutura
type: support-article
updated_at: '2024-08-01T14:39:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25336198209815-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATC010-Quantidade-na-Forma%C3%A7%C3%A3o-divergente-da-Estrutura
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25336198192407) Tempo aproximado para leitura: **00:04:12 min** **Dúvida**Por qual motivo a quantidade na rotina Formação de Preços pode ficar diferente da estrutura do produto?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**O cenário mais plausível e comum de acontecer essa diferença entre o que a rotina Formação de Preços exibe para um material em relação à quantidade que este mesmo material possui na Estrutura (PCPA200) **é quando há Indice de Perda na Estrutura (G1\_PERDA).**

Exemplo prático:

Temos uma relação simples de 1:1 entre o PA-3000 e MP-3000, com índice de perda de 10%:

![image.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25336158346647)

Aplicando a memória de Cálculo do Indice de Perda (Válido para Empenho de OP e Formação de Preços):

**Quantidade = ( Quantidade/(100 - perda))\*100**- detalhes nesta documentação: [Manufatura - Linha Protheus - SIGAPCP - Como o programa trabalha com o percentual de perda de material indicado na estrutura do produto](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028641911-Manufatura-Linha-Protheus-SIGAPCP-Como-o-programa-trabalha-com-o-percentual-de-perda-de-material-indicado-na-estrutura-do-produto?source=search)

Aplicando a realidade da nossa estrutura:

**Quantidade = (1/100 - 10) \* 100**  
**Quantidade = 0,0111111 \* 100**  
**Quantidade= 1,111111**

Ao formar o preço dele, perceba que ele aplica exatamente a memória do cálculo acima: ![Screenshot_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25336198196759)

Porém, caso o usuário queira desconsiderar o percentual da perda, o mesmo pode editar a quantidade base clicando 2x em cima do campo "Quantidade" e alterar para outra desejada, conforme sequencia prints abaixo:

![image (1).png](https://centraldeatendimento.totvs.com/hc/article_attachments/25336158348823)

![image (2).png](https://centraldeatendimento.totvs.com/hc/article_attachments/25336158350487)

![image (3).png](https://centraldeatendimento.totvs.com/hc/article_attachments/25336158351895)

Sendo assim, normalmente a diferença entre o que mostra na estrutura, e o que mostra na Formação, está ligada ao Índice de Perda vinculado à estrutura, que é considerado e realmente não pode ser ignorado na hora de sugerir a formação do preço, nem no empenho produtivo de um produto nesta situação.

Caso este não seja o seu cenário, mas enfrente uma diferença **quantitativa** entre a Estrutura e a Formação, pedimos que abra um ticket junto ao Suporte Técnico munido de todas as evidências possíveis para avaliação.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Cálculos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550082-SIGAEST-C%C3%81LCULOS)
