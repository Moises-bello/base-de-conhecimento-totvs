---
article_id: 360045565853
category: NFe - Nota Fiscal Eletrônica
content_hash: d4f28f57807aeb0829216a907564a84cedad3bdfbde9b736d47a409e2621e728
fetched_at: '2026-06-28T22:40:05.150714+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: 'Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - 590 Rejeição :
  Informado CST para emissor do Simples Nacional (CRT=1)'
type: support-article
updated_at: '2025-06-17T19:36:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045565853-Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-590-Rejei%C3%A7%C3%A3o-Informado-CST-para-emissor-do-Simples-Nacional-CRT-1
---

**Dúvida**

Como solucionar a 590 Rejeição : Informado CST para emissor do Simples Nacional (CRT=1) ?

**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - Todas as versões.

Cross Segmentos - TSS - a partir da versão 12

**Solução**

Se sua empresa for optante do **Simples Nacional** o campo ***CSOSN***deve estar preenchido;

1- Para haver o destaque o do ***CSOSN*** no XML, preencher no TES o campo  **F4\_CSOSN "Campo Cod. Sit. e deixe o campo F4\_SITTRIB Sit. trib. ICM em branco.**

**![CRT.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/13960161659287)**

2- Após isso, ***exclua a nota e gere novamente.***

3- Caso a empresa não seja emitente do simples nacional alterar o parâmetro. Acessar o módulo **Configurador (SIGACFG)**, em seguida em **Ambiente /****Cadastros / Parâmetros** clicar em editar **MV\_CODREG** =***2 ou 3***

2 - Simples Nacional - excesso de receita bruta;

![MV_CODREG_2.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32879773968535)

3 - Regime Nacional.

![MV_CODREG_3.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/32879752568215)

4 - Após isso, **exclua a nota e gere novamente.**
