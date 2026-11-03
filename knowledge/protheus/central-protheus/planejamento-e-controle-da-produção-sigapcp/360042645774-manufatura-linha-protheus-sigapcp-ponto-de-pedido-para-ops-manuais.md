---
article_id: 360042645774
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: e623b10a598199e6053a449f8ab91f904d480747fc1fda50107401b10b314d1f
fetched_at: '2026-06-28T22:42:45.610157+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Ponto de pedido para OPs manuais
type: support-article
updated_at: '2021-06-17T14:00:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360042645774-Manufatura-Linha-Protheus-SIGAPCP-Ponto-de-pedido-para-OPs-manuais
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:05 min**  
**Dúvida**Por que ao gerar uma **OP - Ordem de Produção** manualmente através do **MATA650 - Ordens de Produção** o Sistema não está considerando o **Ponto de Pedido** dos componentes da estrutura?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
O programa **MATA650** não tem a premissa e regra de negócio em criar **OP/SC - Solicitação de Compra** para o ponto de pedido. O campo de **Ponto de Pedido** no **MATA010 - Cadastro do Produto** não influencia a quantidade de **OPIs/SCs** na geração de ordens de produção a partir do programa **MATA650**.  
  
Porém o **MATA650** identifica sim, que houve um atingimento do ponto de pedido. Quando ele identifica acontece o disparo de um *e-mail*, que é configurado no **MATA045 - M-messenger**, e informará o destinatário que o produto atingiu o ponto de pedido.  
Para a geração de ordens de produção para atender o ponto de pedido dos produtos, é utilizado o programa **MATA760** - **Op por Ponto de Pedido**.  
  
Ou seja o **MATA650** não trata ponto de pedido, mas avisa e quem recebeu o aviso, poderá ser utilizado o **MATA760**.
