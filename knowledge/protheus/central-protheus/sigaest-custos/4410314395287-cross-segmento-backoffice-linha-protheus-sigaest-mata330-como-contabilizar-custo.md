---
article_id: 4410314395287
category: SIGAEST - CUSTOS
content_hash: 8012ffae6a1b69a8f4d9646568d2b39bdf129027c5153f6abe7cd6368816f5b1
fetched_at: '2026-06-28T22:39:02.095663+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Como contabilizar
  custo no pedido de venda
type: support-article
updated_at: '2026-06-18T21:46:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410314395287-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-MATA330-Como-contabilizar-custo-no-pedido-de-venda
---

Para contabilizar um pedido de venda nas rotinas de Custo Médio (MATA330) ou Contabilização Off-line (MATA331) no TOTVS Protheus, é necessário criar um lançamento padrão código 678 no módulo Estoque/Custos. Após criar o lançamento, realizar o pedido de venda no módulo de Faturamento, finalizar e executar a rotina escolhida com o parâmetro "Gerar Lancto Contábil = Sim". Por fim, validar na tabela CT2 que o movimento foi contabilizado corretamente.

**Dúvida**  
Como posso contabilizar Pedido de Venda pelas rotinas de Custo Médio (MATA330) ou Contabilização Off-line (MATA331)?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

Para contabilizar uma nota de pedido de vendas, primeiro será necessário criar um lançamento padrão do código 678. Para isso, deve seguir o caminho abaixo:

Acessar o módulo de Estoque/Custos e ir em "Atualizações -> Cadastro -> Lançamentos Padronizados" e clicar em incluir:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410320132119)

OBS: O Suporte Padrão não valida regra de negócio colocado no campo CT5\_VLR01, para isso utilizamos a regra simples de apenas contabilizar o custo do produto colocando a regra "SD2->D1\_CUSTO1":

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410320141719)

Após isso, acessar o módulo de Faturamento e efetuar um pedido de venda e finalizar conforme exemplo abaixo:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410314232727)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410320167063)

Após isso, basta acessar à rotina de Custo Médio (MATA330) ou a rotina de Contabilização Offline (MATA331) e deixar o parâmetro "Gerar Lancto Contábil = Sim":

![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/41296161886743)

Após a finalização da contabilização, basta acessar à tabela CT2 e validar que o movimento do Lançamento Padrão 678 que é de pedido de vendas foram contabilizados:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4410320269591)

O LP 678 será acionado tanto através da rotina **MATA330/****MATA331/MATA038**quanto através da rotina **CTBANFS,**mas com uma diferença.  
   
Do lado de **Faturamento**, sera gerado o lote diferente do esotque, somente se for utilizado na contabilização a opção **"Contabilizar Online = sim"**, e "**Contb. Custo On-Line"**, nos parâmetros F12 da rotina de **MATA410**ao efetuar o pedido de venda, estiver configurada como “Sim”, que vai gerar o lote 008820 alem do 008840 após efetuar a contabilização.

**Saiba mais:**

[*Clique aqui e veja mais artigos sobre Custos no Estoque*](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Quais os Códigos dos Lançamentos Padronizados do Estoque?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020801392-MP-SIGAEST-Quais-os-C%C3%B3digos-dos-Lan%C3%A7amentos-Padronizados-do-Estoque-?source=search)

[*Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como Contabilizar as Movimentações Internas do Estoque?*](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4405082704791)

[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - MATA330 - Como Contabilizar Devolução de Pedido de Venda?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410249729687)
