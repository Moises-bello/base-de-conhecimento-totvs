---
article_id: 4418108415639
category: Configurações
content_hash: df8a37d4ef8b1b7368cd65d67107fbdc07c2fd342cb00ed8062f2c1685c12d66
fetched_at: '2026-06-28T22:46:29.895860+00:00'
product: rm
section_id: 1500000835121
source: central-rm
title: RH - RM - PTO - Considerar/desconsiderar data da demissão como dia útil
type: support-article
updated_at: '2025-09-12T13:22:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4418108415639-RH-RM-PTO-Considerar-desconsiderar-data-da-demiss%C3%A3o-como-dia-%C3%BAtil
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19409314232471) Tempo aproximado para leitura: **00****:01:00 min****Dúvida**Como considerar/desconsiderar data da demissão como dia útil?  
  
**Ambiente**RH - RH (Linha RM) - TOTVS Automação de Ponto - A partir da versão 11.80   
  
**Solução**Para considerar ou desconsiderar a data de demissão do funcionário como dia útil, siga os passos abaixo:

1. Acesse Configurações | Parametrizador | Iniciais |  Etapa 1- Cálculo,  e valide se o parâmetro "Considera a data de demissão como dia útil" está marcado:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34892254930583)

2. Acesse o espelho de ponto e realize o recálculo.

Com o parâmetro marcado a data de demissão será considerada como dia útil. No exemplo abaixo o funcionário foi demitido na data 04/12/2021, e neste dia foram geradas horas base.

![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418099268887)

Se desejar que a data de demissão não seja considerada como dia útil, basta desmarcar o parâmetro em questão, e no espelho de ponto do funcionário a data de demissão não possuirá horas bases, caso venha a trabalhar serão geradas horas extras.

![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4418099228951)

**Saiba Mais:**[Parâmetros do Cálculo](https://tdn.totvs.com/pages/viewpage.action?pageId=452719522)
