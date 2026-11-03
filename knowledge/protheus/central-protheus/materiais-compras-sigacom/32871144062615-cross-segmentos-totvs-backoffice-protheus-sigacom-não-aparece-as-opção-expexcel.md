---
article_id: 32871144062615
category: Materiais - Compras (SIGACOM)
content_hash: daec5756c44866541207fecb8d6f130987c81ae974000cadd2afcc11db5e267b
fetched_at: '2026-06-28T22:41:20.253160+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Não aparece as Opção
  Exp.Excel em Outras Ações das Rotinas de Compras , o que fazer?
type: support-article
updated_at: '2025-11-04T19:22:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/32871144062615-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-N%C3%A3o-aparece-as-Op%C3%A7%C3%A3o-Exp-Excel-em-Outras-A%C3%A7%C3%B5es-das-Rotinas-de-Compras-o-que-fazer
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32871166062999) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**

Não aparece a opção Exp.Excel em Outras Ações nas rotinas do Módulo Protheus Compras , o que fazer?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Compras - A partir da Release **12.1.2410.**  
  
**Solução**

Será necessário realizar a instalação do[**WebAgent**](https://tdn.totvs.com/display/tec/2.+WebApp+-+WebAgent#id-2.WebAppWebAgent-InstWindows)**,** para poder utilizar o excel nas rotinas.

O WebAgent é um serviço opcional **necessário "apenas" nas estações de trabalho**que precisem utilizar:

* Integração com o pacote [**Microsoft Office**](https://tdn.totvs.com/display/tec/SmartClient+-+Office)

Veja mais detalhes no trecho abaixo , e no Link: [TOTVS | WebAgent](https://tdn.totvs.com/display/tec/2.+WebApp+-+WebAgent#id-2.WebAppWebAgent-WebAgent)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32881400047767)

Após realizar a instalação e configuração do Webagent em seu Webapp, será exibido a opção **Exp.Excel em Outras Ações** das Rotinas, conforme exemplo abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32881400051095)

**Obs1:** O WebAgent é compatível com o **WebApp 9.0 ou superior**, **o Application Server 20.3.0.x** **(Harpia)** **ou superior**, e **Lib Protheus 20221010 ou superior.**

**Obs2:** Verifique se a opção de permissão de acesso **170 Exportar telas para Excel** esta ativada.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36103528669463)

****Saiba Mais :****

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
