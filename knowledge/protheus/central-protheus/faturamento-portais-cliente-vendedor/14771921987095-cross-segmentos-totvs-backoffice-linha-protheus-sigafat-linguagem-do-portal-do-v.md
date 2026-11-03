---
article_id: 14771921987095
category: FATURAMENTO - PORTAIS (Cliente, Vendedor)
content_hash: b1fcdd37949ce82cf510dbaf3974ee9cdf991667339fd9d1b130823e7e93959e
fetched_at: '2026-06-28T22:38:24.053215+00:00'
product: protheus
section_id: 1500001539321
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Linguagem do
  Portal do Vendedor
type: support-article
updated_at: '2023-05-23T11:56:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/14771921987095-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Linguagem-do-Portal-do-Vendedor
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Realizei a alteração da linguagem no Protheus, porém ao utilizar o Portal do vendedor a linguagem não foi alterada. Como alterar a linguagem no Portal do Vendedor?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões  
  
**Solução**A linguagem do Portal será demonstrada de acordo com o preenchimento da chave "RpoLanguage" dentro do appserver.ini do ambiente configurado.

Conforme a linguagem que for carregada nesta chave, esta será demonstrada no portal quando o usuário efetuar o acesso.

**Exemplo**: RpoLanguage = Portuguese fará com que o portal seja demonstrado na linguagem selecionada.

**Saiba mais**: [Configuração completa do Portal do Vendedor](https://tdn.totvs.com/x/Cy0aDg)
