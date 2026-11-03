---
article_id: 360019904352
category: ADVPL - Rotina Automática
content_hash: adbabf2fe998d0618c85edc1b0284b3c5d0c1ff64e1a0551f10fae2b2fa8f792
fetched_at: '2026-06-28T22:40:23.858720+00:00'
product: protheus
section_id: 1500001538001
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - ADVPL -  Execauto Cadastro de
  Cliente (MATA030)
type: support-article
updated_at: '2023-09-16T13:58:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019904352-Cross-Segmento-Backoffice-Linha-Protheus-ADVPL-Execauto-Cadastro-de-Cliente-MATA030
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura:**00:01:00 min  
  
Dúvida**Esta rotina deve ser usada desta maneira ou ela existe outra sintaxe?

MSExecAuto({|x,y| Mata030(x,y)},aVetor,3)

**Ambiente**Protheus – Materiais – A partir da versão 12.1.17  
  
**Solução**A Rotina mata030 com essa sintaxe funciona perfeitamente, pois foi mantido o legado MSExecAuto({|x,y| Mata030(x,y)},aVetor,3)

Mas é possível Fazer de outra forma dentro do Conceito MVC.

**[DT Novo Fonte de Cadastro de Clientes em MVC](http://tdn.totvs.com/display/PROT/DT+Novo+Fonte+de+Cadastro+de+Clientes+em+MVC)**
