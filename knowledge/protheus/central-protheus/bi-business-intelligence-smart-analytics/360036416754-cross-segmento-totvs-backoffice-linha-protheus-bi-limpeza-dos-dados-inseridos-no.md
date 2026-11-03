---
article_id: 360036416754
category: BI - Business Intelligence - Smart analytics
content_hash: e7481a723a743d073c254cd82dcb81ee1413d34b736636b9a7c3d39122a74395
fetched_at: '2026-06-28T22:37:04.182566+00:00'
product: protheus
section_id: 1500001539741
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - BI - Limpeza dos dados inseridos
  no TOTVS Smart Analytics de forma dinâmica.
type: support-article
updated_at: '2022-07-27T18:15:50Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036416754-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-BI-Limpeza-dos-dados-inseridos-no-TOTVS-Smart-Analytics-de-forma-din%C3%A2mica
---

**Dúvida**É possível limpar os dados de uma determinada tabela no TOTVS Smart Analytics?

**Ambiente**Cross Segmento - TOTVS Backoffice Linha Protheus – Smart Analytics - Todas versões  
  
**Solução****Limpeza Parametrizada dos dados:** Como efetuar a limpeza de forma dinâmica das entidades parametrizadas  
**1º-)**Acessar o console de integração de dados  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047624674/mceclip4.png)

**2º-)**Criar um agendamento para o **graph DELETE\_ALL\_PROJECT.grf  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047623934/mceclip1.png)**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048504393/mceclip0.png)

**3º-)**Adicionar um parâmetro para este agendamento:  
        **Parameter name:** ENTITIES  
        **Parameter value:** Entidades que deseja efetuar a limpeza. Devem ser informadas dividindo-as por ',':Exemplo: HL2,HL9,HJ4,HJ6,HLK

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360048504573/mceclip2.png)

**4º-)**Executar o agendamento criado.  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360047624474/mceclip3.png)

Após tal ação, basta executar a extração dos dados dentro do ERP e em seguida rodar rodar o Agent para a subida dos dados.  
  
**Saiba mais**  
[Limpeza dos dados inseridos no TOTVS Smart Analytics de forma dinâmica.](https://tdn.totvs.com/pages/releaseview.action?pageId=271653138)
