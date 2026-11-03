---
article_id: 4421076288791
category: PMS - Projetos
content_hash: aa0b77ee84bae2b1c3b37eeb5e0462276619859ccfafe9438490fd99277e26fa
fetched_at: '2026-06-28T22:37:15.938895+00:00'
product: protheus
section_id: 1500001539701
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAPMS - Mão de Obra para Controle
  de Custo
type: support-article
updated_at: '2024-02-26T18:19:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4421076288791-Cross-Segmentos-Backoffice-Protheus-SIGAPMS-M%C3%A3o-de-Obra-para-Controle-de-Custo
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21627932041623) Tempo aproximado para leitura: **00:03 min** **Dúvida**Como apurar e ratear o custo da mão de obra envolvida na fabricação do produto pela Integração Contábil no recálculo do custo médio?

**Ambiente**

Cross Segmentos - Backoffice Protheus - SIGAPMS - Todas as Versões

**Solução**

Para apurar e ratear o custo da mão de obra envolvida na fabricação do produto, pela Integração Contábil no recálculo do custo médio, utilize duas metodologias: 

**1. Apuração do custo da mão de obra valorizada em um único centro de custo;**

Nesse método, somente um produto pode ser integrado a cada centro de custo.

Para tanto: Cadastre um centro de custo para integração (exemplo: 10200).

1. Cadastre o produto com código iniciado pelas iniciais **MOD** somado ao centro de custos para integração, sendo que, somente um produto pode ser integrado a cada centro de custos.
2. No processamento do recálculo do custo médio, se a pergunta **Calcula MOD** está configurada com **Sim**, todo valor gerado para o centro de custos é absorvido pelo produto.

**2. Apuração do custo de mão-de-obra valorizada e rateadas no mesmo centro de custos.**

O mesmo centro de custo pode ser associado a mais de um produto, desde que os grupos contábeis sejam distintos para cada produto.

**Para tanto:**

1. Cadastre um centro de custo para integração (exemplo: 10200).
2. Cadastre um produto de mão de obra com qualquer código e relacionar no campo **CC p/ Custo** o código do centro de custo para integração. Além da informação do centro de custo, no campo **Gr. Cnt Custo**, informe também um grupo contábil para filtrar os dados.
3. No processamento do recálculo do custo médio, se a pergunta **Calcula MOD** está configurada com **Sim**, todo valor gerado para o Centro de custo e grupo de contas associado é absorvido pelo produto.

**Saiba mais em:** [Mão de Obra - Produto](https://tdn.totvs.com/x/FZOZH)
