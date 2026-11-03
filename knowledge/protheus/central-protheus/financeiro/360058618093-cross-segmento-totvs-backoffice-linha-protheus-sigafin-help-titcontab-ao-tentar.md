---
article_id: 360058618093
category: Financeiro
content_hash: a2fae1d225097a57d57638732c5051f798b1c2d56f3c29cb8517666b304cc66f
fetched_at: '2026-06-28T22:38:01.148281+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice (Linha Protheus)  - SIGAFIN - Help: TITCONTAB
  -  Ao tentar alterar a natureza de um título'
type: support-article
updated_at: '2022-03-02T21:39:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058618093-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-Help-TITCONTAB-Ao-tentar-alterar-a-natureza-de-um-t%C3%ADtulo
---

**Ocorrência**Ao lançar documento de entrada o título gerado não permiti alterar da natureza, apresenta a mensagem - Help: TITCONTAB - Ao tentar alterar a natureza de um título

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4556149826839/mceclip0.png)  
  
**Ambiente**Cross Segmento - Backoffice Linha Protheus – Financeiro – Todas as versões. 

**Causa**Ocorre devido o campo está com conteúdo E2\_LA = Sim ( considera contabilizado)

**Solução**A mensagem ocorre devido ao campo E2\_LA = Sim (contabilizado), impossibilita a alteração da natureza no **título a pagar** gerado a partir de um documento de entrada, onde:   
  
1) Na origem do título já classificado no setor **FISCAL.**   
  
2) Títulos com origem no módulo do **Compras** sempre serão incluídos na tabela **SE2** com o campo **E2\_LA = Sim**, pois a contabilização ocorre pela nota de entrada. Logo mesmo o campo sendo aberto para alteração da natureza, não será permitida por conta dessa regra e ao tentar será emitido o  
**HELP: TITCONTAB**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4556183372695/mceclip1.png)**

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4556200450967/mceclip2.png)**

2) Quando a natureza utilizada no documento de entrada e levada para o **título a pagar**, possuir algum campo para o cálculo de imposto configurado como SIM, e conforme print abaixo, por padrão a rotina **FINA050 / FINA750** não habilitará o campo **E2\_NATUREZA** para alteração, pois títulos que possuem impostos não podem ter a natureza alterada.

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4556211295127/mceclip3.png)

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4556217063831/mceclip4.png)

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4556233264407/mceclip5.png)

Sendo assim baseado nessas análises o processo correto para correção no **título a pagar** seria a exclusão da nota de entrada e novo lançamento com a natureza correta.  
Não identificamos ponto de entrada para efetuar essa alteração em nenhuma das situações.  
  
**Saiba mais**<https://tdn.totvs.com/pages/releaseview.action?pageId=269443669>  
<https://tdn.totvs.com/display/public/PROT/FIN0015_LPAD_FLAG_LA>
