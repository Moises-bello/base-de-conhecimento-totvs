---
article_id: 25754847654551
category: Financeiro - Contas a Receber
content_hash: 3ccb9b5026b2ab7eeb0075c9f3806e2240a1a19d2a6d560aeb7a7f84eb09c0da
fetched_at: '2026-06-28T22:38:14.098016+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross segmentos - Backoffice Linha Protheus - SIGAFIN - FINA740 - Anexar documentos
  (Conhecimento)  na rotina Funções Contas a Receber
type: support-article
updated_at: '2024-08-19T20:38:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25754847654551-Cross-segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA740-Anexar-documentos-Conhecimento-na-rotina-Fun%C3%A7%C3%B5es-Contas-a-Receber
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25754847625623) Tempo aproximado para leitura: **00:05:00 min****Dúvida**Como anexar documentos através do botão conhecimento na rotina Funções Contas a Receber  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**No padrão para adicionar o botão **Conhecimento** na rotina **Contas a Receber (FINA040)**, precisamos utilizar o PE **FA740BRW - Adição de Itens no menu da mBrowse**, a inclusão deve ser utiliza a função **MSDOCUMENT**, conforme abaixo:   
  
**Exemplo:**

#Include "Protheus.ch"

#Include "TBICONN.ch"

  
  

User Function FA740BRW()

  

aRotina := { {"Conhecimento", "MSDOCUMENT('SE1',SE1->(RECNO()),4)", 0, 4,} }

  
  

//Validações do usuário

  

Return (aRotina)

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25759454920983)
