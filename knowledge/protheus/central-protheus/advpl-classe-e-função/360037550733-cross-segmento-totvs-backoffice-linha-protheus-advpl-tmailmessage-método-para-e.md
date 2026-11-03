---
article_id: 360037550733
category: ADVPL - Classe e Função
content_hash: 58636fbb3995ecb694c69cfc2539d68b082d768489916e24c81488a6c6e99e8b
fetched_at: '2026-06-28T22:40:18.111416+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - TMailMessage método
  para e-mail não ser classificado como SPAM
type: support-article
updated_at: '2022-06-14T17:22:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037550733-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-TMailMessage-m%C3%A9todo-para-e-mail-n%C3%A3o-ser-classificado-como-SPAM
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:01:00 min****Dúvida**Existe algum recurso para cliente ajustar na classe Classe **TMailMessage**, para que o e-mail não vá para caixa de spam?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL  – A partir da versão 11.80  
  
**Solução**Não, pois a regra de SPAM é do provedor de e-mail.  
Agora, se a causa for parâmetros  "Content-type" do anexo não foi especificado no cabeçalho , utilize o método [AddCustomHeader](https://tdn.totvs.com/display/tec/TMailMessage%3AAddCustomHeader).
