---
article_id: 7753942435991
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: 7248fe155e798ab5457daef6fb8ccfb88ac88f1732e7f0cc8142d7233edfed2b
fetched_at: '2026-06-28T22:37:21.422615+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Centro de Custo e outras
  Entidades Contábeis não são levadas para o Título gerado pela Medição - CNTA121
type: support-article
updated_at: '2023-12-06T17:01:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/7753942435991-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Centro-de-Custo-e-outras-Entidades-Cont%C3%A1beis-n%C3%A3o-s%C3%A3o-levadas-para-o-T%C3%ADtulo-gerado-pela-Medi%C3%A7%C3%A3o-CNTA121
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19611935189783) Tempo aproximado para leitura: **00:05:00 min** **Dúvida**Centro de Custo e outras Entidades Contábeis não são levadas para o Título Financeiro gerado no Encerramento da Medição - CNTA121  
  
**Ambiente**Cross Segmentos - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão de Contratos - Todas as versões  
  
**Solução**

Pelo padrão do Protheus o campo Centro de Custo e as demais Entidades Contábeis no Titulo de Contas a Pagar/Receber, não são campos obrigatórios.

![inline1916520170.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19611935211159)

Por padrão, nos títulos gerados no Encerramento da Medição no Gestão de Contratos, somente os campos obrigatórios  por padrão são preenchidos, dessa forma as Entidades Contábeis bem como rateios de Entidades Contábeis incluídas na Medição não são levadas automaticamente para os campos existentes no Titulo a Pagar/Receber de um módulo para o outro pelo conceito padrão do sistema.

Na ***CNTA121*** existe um ponto de entrada que pode ser utilizado para gravação das informações no título, pois complementa a gravação dos campos na SE2/SE1, cuja documentação segue abaixo:

[CN121AFN - Altera informações do título financeiro no encerramento da medição](https://tdn.totvs.com/pages/viewpage.action?pageId=578632647)

***Saiba Mais:***

[CN121AFN - Altera informações do título financeiro no encerramento da medição](https://tdn.totvs.com/pages/viewpage.action?pageId=578632647)

[MP - SIGAGCT - Pontos de entrada para rotinas de Medição](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022685112-MP-SIGAGCT-Pontos-de-entrada-para-rotinas-de-Medi%C3%A7%C3%A3o?source=search)

[Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001539581)
