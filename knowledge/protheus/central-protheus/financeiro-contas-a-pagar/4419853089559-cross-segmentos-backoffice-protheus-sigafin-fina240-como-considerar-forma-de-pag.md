---
article_id: 4419853089559
category: Financeiro - Contas a Pagar
content_hash: f2a3f743af626b3c59c087504a8c2e53c0cb8a2803fbc395f287f58995cc00f9
fetched_at: '2026-06-28T22:38:09.841249+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - BackOffice Protheus - SIGAFIN - FINA240 - Como considerar
  Forma de Pagamento (campo E2_FORMPAG)
type: support-article
updated_at: '2025-09-19T14:54:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4419853089559-Cross-Segmentos-BackOffice-Protheus-SIGAFIN-FINA240-Como-considerar-Forma-de-Pagamento-campo-E2-FORMPAG
---

**Dúvida**Como considerar Forma de Pagamento (campo E2\_FORMPAG)?  
**Ambiente**Cross Segmento - TOTVS BackOffice (Linha Protheus) - Financeiro - FINA240 - Todas as versões

**Solução**

**1 - Na montagem do borderô de pagamento**Ajustando o parâmetro **F12 *"Considera Forma de Pgto ?"  = SIM*** da rotina **FINA240** **- Borderô de Pagamentos, o** sistema fará o complemento no filtro padrão considerando o campo **E2\_FORMPAG** dos títulos a pagar**.**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4419852900887)

**2 - Na inclusão de um  QRCODE.**

FINA050 - Ao incluir um título no contas a pagar onde no cadastro do fornecedor não possui definição da sua forma de pagamento **A2\_FORMPAG** (vazio).

No momento do preenchimento das informações do título a pagar em tela na rotina FINA050, não será preenchido nenhum código de forma de pagamento no campo **E2\_FORMPAG**, pois o campo **A2\_FORMPAG** também estará vazio.

Porém, se a empresa clicar em "Outras Ações > Complemento do título > PIX"

E inserir um **QRCODE** no campo **FKF\_PAGPIX**

Ao clicar em "Confirmar" na tela de complemento do título

e clicar em "Confirmar" na tela de inclusão do título a pagar,

Automaticamente o sistema irá preencher o campo com o conteúdo

**E2\_FORMPAG** = 47  (PIX QR CODE)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/35059584803095)](https://centraldeatendimento.totvs.com/hc/article_attachments/35059584803095)

**Saiba mais**

[Borderô Pagamentos - FINA240](https://tdn.totvs.com/pages/releaseview.action?pageId=236605212)
