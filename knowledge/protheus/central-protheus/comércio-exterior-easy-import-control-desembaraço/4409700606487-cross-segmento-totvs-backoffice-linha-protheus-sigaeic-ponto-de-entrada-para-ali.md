---
article_id: 4409700606487
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: 974f5cb18061e836d0bbcce9ca462b9436244069fb54046ca593ba9e22d6e5d2
fetched_at: '2026-06-28T22:39:50.148393+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Ponto de Entrada
  para alimentar os campos na Tabela "SF1"
type: support-article
updated_at: '2024-01-19T19:22:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409700606487-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Ponto-de-Entrada-para-alimentar-os-campos-na-Tabela-SF1
---

****![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20710806125975) Tempo aproximado para leitura: **02:00 min******

**Dúvida**Preciso de um Ponto de Entrada para alimentar os campos na Tabela "**SF1**".  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões  
  
**Solução**O ponto de entrada a ser utilizado será de acordo com a seguinte configuração:  
1)Se o parâmetro **MV\_TEM\_DI** estiver **desabilitado**:  
Execblock("**EICDI154**",.F.,.F.,"**GRAVACAO\_SF1**") e alterar a variável aCab.

2)Se o parâmetro **MV\_TEM\_DI** estiver **habilitado**:  
Execblock("**EICDI554**",.F.,.F.,"**GRAVACAO\_SF1**") e alterar a variável aCab.  
 **Saiba mais:****[PE EICDI154 - Recebimento de Importação](https://tdn.totvs.com/pages/releaseview.action?pageId=574364993)****[PE EICDI554 - Recebimento de Importação](https://tdn.totvs.com/pages/releaseview.action?pageId=244919921)**
