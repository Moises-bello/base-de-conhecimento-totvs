---
article_id: 4407601190679
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: fcb0eb252cb2e12ac5ec4a94656dd2f66485426d202f8360007502f80c8d9e3e
fetched_at: '2026-06-28T22:42:41.011482+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Campo ordem de produção na solicitação
  de compra não é preenchido
type: support-article
updated_at: '2024-01-02T14:48:46Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407601190679-Manufatura-Linha-Protheus-SIGAPCP-Campo-ordem-de-produ%C3%A7%C3%A3o-na-solicita%C3%A7%C3%A3o-de-compra-n%C3%A3o-%C3%A9-preenchido
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20256925485719) Tempo aproximado para leitura: **00:01:22 min** **Dúvida**Quando o campo **C1\_OP - Ordem de Produção** na **SC - Solicitação de Compra** não é preenchido?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**As **SCs** podem ficar sem o número da **OP - Ordem de Produção**, quando as mesmas são geradas automaticamente através do **MATA650 - Ordem de Produção** e:

* Existir **lote econômico** e ele for maior que a quantidade necessária na **OP**;
* O parâmetro **Aglutina SC's?**do **F12 estiver** igual a **Aglt. Data Nece.;**
* O parâmetro **MV\_GRAVOP - Definições de quando grava a OP na SC** possui o conteúdo **4;**
* O parâmetro **MV\_GRAVOP** possui o conteúdo **1** e a quantidade da **SC** gerada não é igual a quantidade necessária, considerando o estoque avaliado menos o empenho para a essa **O****P ;**
* O parâmetro **MV\_GRAVOP** possui o conteúdo **3** e a quantidade empenhada não é igual a quantidade da **SC**, nem múltiplo deste.

**Saiba mais**  
Para mais informações sobre o parâmetro **MV\_GRAVOP**, acesse o [link](https://tdn.totvs.com/pages/viewpage.action?pageId=680239110)
