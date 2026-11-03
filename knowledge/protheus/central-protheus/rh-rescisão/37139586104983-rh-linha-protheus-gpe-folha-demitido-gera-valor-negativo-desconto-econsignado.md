---
article_id: 37139586104983
category: RH - Rescisão
content_hash: 844f86ee6710288f31d57ae99820136a4001f6eb71b1e1aac312f2744a156eea
fetched_at: '2026-06-28T22:43:49.717570+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Folha demitido gera valor negativo desconto eConsignado
type: support-article
updated_at: '2025-12-19T11:12:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37139586104983-RH-Linha-Protheus-GPE-Folha-demitido-gera-valor-negativo-desconto-eConsignado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37139602865431) Tempo aproximado para leitura: **01:30 min**  
  
**Dúvida**  
Por que folha demitido gera valor negativo desconto eConsignado?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**  
O calculo de folha demitido gera  valor negativo desconto eConsignado devido desconto eConsignado rescisão ter sido lançado manual verba origem I.

Em rescisão o desconto eConsignado deve ser gerado pela rotina lançamento valores futuros origem G, deste modo ao integrar o roteiro RES e calcular a folha do demitido, em liquido a receber fica zerado.

**Saiba Mais:**

[RH - Linha Protheus - GPE - Cálculo eConsigando em rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/32327889957271-RH-Linha-Protheus-GPE-C%C3%A1lculo-eConsigando-em-rescis%C3%A3o)
