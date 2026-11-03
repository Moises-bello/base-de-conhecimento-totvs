---
article_id: 1500001572961
category: Materiais - Compras (SIGACOM)
content_hash: 27e4f5da9055477e4ec8ffc4c24298d04854cfa91ad1b3097a63f55af4a29cad
fetched_at: '2026-06-28T22:41:14.400788+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Centro de Custo e outras
  Entidades Contábeis não são levadas para o Título gerado pelo Documento de Entrada
  - MATA103
type: support-article
updated_at: '2025-03-21T14:50:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001572961-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Centro-de-Custo-e-outras-Entidades-Cont%C3%A1beis-n%C3%A3o-s%C3%A3o-levadas-para-o-T%C3%ADtulo-gerado-pelo-Documento-de-Entrada-MATA103
---

**Dúvida**Centro de Custo e outras Entidades Contábeis não são levadas para o Título gerado pelo Documento de Entrada - MATA103

**Ambiente**Protheus  – Compras – A partir da versão 12  
  
**Solução**

Pelo padrão do Protheus o campo Centro de Custo e as demais Entidades Contábeis no Titulo de Contas a Pagar, não são campos obrigatórios.

![inline1916520170.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360102606233)

Por padrão, nos títulos gerados pelo Documento de Entrada, somente os campos obrigatórios são preenchidos, dessa forma as Entidades Contábeis incluídas no Documento de Entrada não são levadas automaticamente para os campos existentes no Titulo a Pagar de um módulo para o outro pelo conceito padrão do sistema.

Na ***MATA103*** existe um ponto de entrada que pode ser utilizado para gravação das informações no título, pois complementa a gravação dos campos na SE2, cuja documentação segue abaixo:  
  
*MT100GE2 - Complementa a Gravação dos Títulos Financeiros a Pagar*  
Link: [MT100GE2 - Complementa a Gravação dos Títulos Financeiros a Pagar](http://tdn.totvs.com/pages/viewpage.action?pageId=6085781)

***Obs1:***

As informações das Entidades Contábeis da Nota Fiscal não são automaticamente transferidas para os campos do título financeiro gerado, tanto para as entidades informadas no item da NF (tabela SD1) quanto para as entidades configuradas na opção de Rateio de Centro de Custos (tabela SDE).

***Saiba Mais :***

[MT100GE2 - Complementa a Gravação dos Títulos Financeiros a Pagar](http://tdn.totvs.com/pages/viewpage.action?pageId=6085781)

[MP - SIGACOM - Pontos de entrada do Documento de Entrada - MATA103](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006469332-MP-SIGACOM-Pontos-de-entrada-do-Documento-de-Entrada-MATA103?source=search)

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000049308-Materiais-Compras-SIGACOM-)
