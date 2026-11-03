---
article_id: 1500006526842
category: Financeiro - Baixas a Receber
content_hash: f30a3b4f20a4770b439b8286ef5bedf413d50edf3e363b1ce55526c40d6440be
fetched_at: '2026-06-28T22:37:43.763296+00:00'
product: protheus
section_id: 33820269506967
source: central-protheus
title: Cross Segmento Protheus - Backoffice Linha Protheus - SIGAFIN - FINA070 - Ao
  baixar o RA não gera movimento bancário
type: support-article
updated_at: '2026-05-20T19:08:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006526842-Cross-Segmento-Protheus-Backoffice-Linha-Protheus-SIGAFIN-FINA070-Ao-baixar-o-RA-n%C3%A3o-gera-movimento-banc%C3%A1rio
---

**Dúvida**  
Ao realizar a baixa do RA, o sistema não gera movimento bancário?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**  
Para que o RA gere movimentação, acesse a rotina FINA070 e, na tela de parâmetros (F12), configure o campo **“Gerar cheque p/ Adiantamento”** com a opção **“Não”**.

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500008665541)**

Quando o parâmetro estiver configurado como **“Sim”**, o movimento permanecerá aguardando liberação na rotina **FINA190 - Geração de Cheque.**
