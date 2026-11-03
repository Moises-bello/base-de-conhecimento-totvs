---
article_id: 360025310294
category: NFe - Nota Fiscal Eletrônica
content_hash: 1a8417729cf1c07893be5bd564d015998cae519508a91d5f09bc0f2a168c9741
fetched_at: '2026-06-28T22:40:00.157204+00:00'
product: protheus
section_id: 1500001538141
source: central-protheus
title: '    Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - Como gerar
  a mensagem do Pis e Cofins para destinatários do PR '
type: support-article
updated_at: '2021-10-08T17:09:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025310294--Cross-Segmentos-Backoffice-Protheus-Doc-Eletr%C3%B4nicos-Como-gerar-a-mensagem-do-Pis-e-Cofins-para-destinat%C3%A1rios-do-PR
---

**Dúvida**Como gerar a mensagem do Pis e Cofins para destinatários do PR ?  
  
**Ambiente**

Cross Segmentos - Backoffice Protheus - Doc. Eletrônicos - NFe - a partir da versão 12.1.25

Cross Segmentos - TSS - a partir da versão 12

**Solução**

1- Habilitar o parâmetro abaixo para gerar a mensagem do Pis e Cofins para destinatários do PR:

**MV\_DPISCOF = .T.**

2- Para sair a mensagem dos **dois** impostos no cadastro do destinatário o campo **A1\_EST = PR**

* **Mensagem gerada:**

" Conforme Lei Estadual PR 17.127/12 segue o Valor Pis / Cofins:"  
" Valor Pis R$ "   
"Valor Cofins R$ "
