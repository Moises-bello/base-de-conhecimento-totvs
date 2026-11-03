---
article_id: 13451192810775
category: RH - Rescisão
content_hash: 70c76f1f6842a84af504390ba416e384b193841230b2b07f1185df60a9d42e23
fetched_at: '2026-06-28T22:43:49.746523+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Importação via MILE rotinas de cálculo férias (GPEM030)
  e rescisão (GPEM040)
type: support-article
updated_at: '2025-09-09T21:34:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13451192810775-RH-Linha-Protheus-GPE-Importa%C3%A7%C3%A3o-via-MILE-rotinas-de-c%C3%A1lculo-f%C3%A9rias-GPEM030-e-rescis%C3%A3o-GPEM040
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34822407591447) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**É possível configurar rotinas de cálculo como Férias (GPEM030) e Rescisão (GPEM040) para importação via MILE?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da Versão 12.  
  
**Solução**

Não é possível. As rotinas de cálculo Rescisão (GPEM040) e Férias (GPEM030) embora tenham sido desenvolvidas em MVC e seguem a premissa do MILE de ser viável a importação, possuem sub processos vinculados internamente e responsáveis por validar e gerar informações diversas no momento do cálculo.  
Esses dados, como os Dias de Aviso Prévio, Dias de Férias, Dias de Férias Proporcionais, Dias de Férias Vencidas, são consistidos com outras tabelas como Período Aquisitivo, Afastamentos e são extraídos de informações vinculadas ao motor de cálculo do módulo de Gestão de Pessoal.

Com a intenção de não desvincular esses processos da rotina com o motor de cálculo, tendo em vista que o impacto sobre informações indevidas podem gerar efeitos colaterais incorrigíveis como dias de férias indevidos, rescisões complementares incompletas, cálculo de dissídio com valores errados entre outros, essas rotinas não serão executadas pelo Mile.

**Saiba mais**

<https://tdn.totvs.com/pages/releaseview.action?pageId=550315418>
