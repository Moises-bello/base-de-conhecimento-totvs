---
article_id: 1500010473242
category: Financeiro - Contas a Receber
content_hash: 81cf7dad9cb0ac4175bc8e578e44efd748a4474177c3eb6ec7f69f046753a65c
fetched_at: '2026-06-28T22:38:12.784320+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA060 Ao efetuar uma
  transferência da carteira 0 para F protestado o campo A1_TITPROT não atualiza.
type: support-article
updated_at: '2021-05-14T18:12:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500010473242-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA060-Ao-efetuar-uma-transfer%C3%AAncia-da-carteira-0-para-F-protestado-o-campo-A1-TITPROT-n%C3%A3o-atualiza
---

**Dúvida**Ao efetuar uma transferência da **carteira 0 para F protestado** o campo **A1\_TITPROT** não atualiza?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**O padrão do Protheus ao transferir um titulo da **carteira 0 para F protestado** ou **contrário da F para  0,** o mesmo só esta alterando o campo **E1\_SITUACA**, ou seja, a situação do título.  
  
Se o mesmo pressionar F1 no campo**A1\_TITPROT**, apresenta a funcionalidade deste campo 

(números de títulos protestados de clientes).

![](https://totvssuporte.zendesk.com/attachments/token/uNYQJULBppYKzoBahlNXFjxJS/?name=inline1271676846.png)​

**Importante**No padrão esses campos não tem ligação, a não ser que haja alguma customização em seu ambiente.
