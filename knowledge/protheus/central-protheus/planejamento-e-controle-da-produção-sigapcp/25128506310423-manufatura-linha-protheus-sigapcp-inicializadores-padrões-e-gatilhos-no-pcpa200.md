---
article_id: 25128506310423
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 93d38b99443baa545d90d349053efd44777b78a1910b4ab3ea628c06b46bf1e0
fetched_at: '2026-06-28T22:42:43.423013+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Inicializadores padrões e gatilhos
  no PCPA200
type: support-article
updated_at: '2024-07-24T14:41:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25128506310423-Manufatura-Linha-Protheus-SIGAPCP-Inicializadores-padr%C3%B5es-e-gatilhos-no-PCPA200
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25128506266903) Tempo aproximado para leitura: **00:01:00 min** **Dúvida**Qual o comportamento quando os campos **G1\_REVINI - Revisão Inicial do Componente** ou **G1\_REVFIM  - Revisão Final do Componente** possuem inicializadores padrões ou gatilhos para seu preenchimento?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Quando o parâmetro **MV\_REVAUT - Indica se o controle de revisões será controlado automaticamente** tem o conteúdo **T** , inicializadores padrões ou gatilhos para os campos **G1\_REVINI** e **G1\_REVFIM** são ignorados e esses campos serão preenchidos de acordo com as regras do **PCPA200 - Manutenção de estruturas,** quando a manutenção da estrutura se dá por esse programa.  
Gatilhos e inicializadores padrões para preenchimento desses campos serão respeitados pelo **PCPA200** somente se o parâmetro **MV\_REVAUT** tem o conteúdo **F**.
