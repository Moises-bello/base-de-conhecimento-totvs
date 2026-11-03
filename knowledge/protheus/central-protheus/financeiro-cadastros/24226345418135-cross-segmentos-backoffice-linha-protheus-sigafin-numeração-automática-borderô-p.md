---
article_id: 24226345418135
category: Financeiro - Cadastros
content_hash: 43bc8b63e5d01785aa9a202d236e0c025b1d77b5aa45af7dcb2651b85ada78c0
fetched_at: '2026-06-28T22:37:53.143602+00:00'
product: protheus
section_id: 1500001550722
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Numeração automática
  borderô pagamento/recebimento
type: support-article
updated_at: '2025-10-28T13:07:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24226345418135-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Numera%C3%A7%C3%A3o-autom%C3%A1tica-border%C3%B4-pagamento-recebimento
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24226353223575) Tempo aproximado para leitura: **00****:02:00 min** **Dúvida**Como controlar a numeração automática dos borderôs de pagamento/recebimento?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas versões  
  
**Solução**O controle da numeração dos borderôs para o **Contas a pagar** será o **MV\_NUMBORP** e **Receber** o **MV\_NUMBORR.**

Controle de numeração dos **Borderôs - FINA240 / FINA241 / FINA060 / FINA061**   
**MV\_NUMBORR**: Número sequencial dos Borderôs de Recebimentos.

**MV\_NUMBORP**: Número sequencial dos Borderôs de Pagamentos.

Obs: Esses parâmetros devem ser configurados como exclusivos somente quando o cadastro de bancos (SA6) estiver configurado com nível de compartilhamento totalmente exclusivo. Para os demais níveis de compartilhamento da SA6, esses parâmetros devem estar configurados como compartilhados.

**Saiba mais:**

[Borderô Pagamentos - FINA240 - Financeiro - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=236605212)

[Transferências - FINA060 - Financeiro - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=271405699)

[21 - Parâmetros CNAB / SISPAG - Por Processo / Rotina / Borderôs](https://tdn.totvs.com/pages/releaseview.action?pageId=353280234)
