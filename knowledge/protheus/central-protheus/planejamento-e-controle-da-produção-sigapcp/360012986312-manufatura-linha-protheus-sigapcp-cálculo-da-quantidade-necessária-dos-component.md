---
article_id: 360012986312
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 3204697ea95ab1ee8013935d91a1e990b23a2d406fda44d1a3aaafda0f621c94
fetched_at: '2026-06-28T22:42:40.947977+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Cálculo da quantidade necessária dos
  componentes da estrutura
type: support-article
updated_at: '2021-09-08T12:58:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012986312-Manufatura-Linha-Protheus-SIGAPCP-C%C3%A1lculo-da-quantidade-necess%C3%A1ria-dos-componentes-da-estrutura
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:00:55 min****Dúvida**Ao gerar a **OP - Ordem de Produção**, como o Sistema calcula a **quantidade** necessária dos componentes da **estrutura?**  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**O Sistema verifica a **quantidade** da **OP**, **divide** pela quantidade base do produto em questão e **multiplica** pelo componente a ser empenhado.  
Se gerar uma **OP intermediária** o Sistema fará novamente o cálculo, agora levando em consideração a quantidade da **OP intermediária**.  
  
**Exemplo**Vamos considerar a seguinte estrutura:  
  
Produto01 - Quantidade base = 1  
|\_\_\_\_Produto02 - Quantidade na estrutura = 12  
       |\_\_\_\_Produto03 - Quantidade na estrutura = 12  
  
Caso seja aberta uma **OP** para o Produto01 de 10 unidades, será gerado um empenho do Produto02 de 120 unidades e do Produto03 será gerado um empenho de 1440 unidades.
