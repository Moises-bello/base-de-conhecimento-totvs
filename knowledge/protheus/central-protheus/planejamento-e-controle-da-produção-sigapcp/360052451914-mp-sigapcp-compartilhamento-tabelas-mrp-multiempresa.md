---
article_id: 360052451914
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 7cba47f9f8ff57f6b29d0c6e3104a5f40015d7c1ffe0112e70570edb39300f28
fetched_at: '2026-06-28T22:42:47.169049+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: MP - SIGAPCP - Compartilhamento tabelas MRP Multiempresa
type: support-article
updated_at: '2020-08-19T18:09:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052451914-MP-SIGAPCP-Compartilhamento-tabelas-MRP-Multiempresa
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:00 min**  
 **Dúvida**Quais tabelas devem ser compartilhadas para executar o **PCPA107**?  
   
 **Ambiente**Microsiga Protheus - Planejamento e Controle da Produção - Versão 12  
  
**Solução**Para utilizar o **PCPA107 -** **MRP Multiempresa**, algumas tabelas do Sistema devem ser compartilhadas via configurador **SIGACFG - Configurador**, são elas:

* **SB1 - Produto;**
* **SGI - Produto Alternativo;**
* **SOR - Movimentos do MRP;**
* **SOT - Períodos do MRP;**
* **SOU - Sugestões de transferências;**
* **SOQ - Objetos do MRP;**
* **SOS - Movimentos entre empresas MRP;**
* **SOV - Necessidades unitárias.**

**Importante**  
Não devem ser utilizados os dados da **SBZ – Indicadores** de produtos quando utilizar o conceito **MRP Multiempresa**. Verificar parâmetro **MV\_ARQPROD - O parâmetro configura se os dados de indicadores de produto serao considerados pela tabela SB1 ou se serão considerados pela da tabela SBZ.**  
  
**Saiba mais**Para mais informações sobre a rotina acesse o manual: [MRP - PCPA107](https://tdn.totvs.com/x/oq21F)
