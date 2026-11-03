---
article_id: 360056376954
category: ADVPL - Classe e Função
content_hash: 937f292463acec43634ac56ce25ca2259a9ab8f0b5981ea36d18a78b15bc94f6
fetched_at: '2026-06-28T22:40:14.575660+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Classe FwFormView:
  Criar filtros'
type: support-article
updated_at: '2022-01-04T21:29:22Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360056376954-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Classe-FwFormView-Criar-filtros
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Existiria a opção de criar filtro usando a classe FwFormView, direto no MVC?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17  
  
**Solução**Não é possível incluir filtros de usuários dinamicamente em um modelo MVC. O mesmo é uma representação da tabela e sua carga de dados depende da lógica imputada na construção do modelo.

O desenvolvedor pode, a seu critério, incluir um filtro na carga de dados através do método SetLoadFilter  
  
**Saiba mais**  
[FWFormGridModel](https://tdn.totvs.com/display/framework/FWFormGridModel)  
[FWFormView](https://tdn.totvs.com/display/framework/FWFormView)
