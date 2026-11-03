---
article_id: 360018994491
category: Financeiro - Contas a Pagar
content_hash: 7827994189e769ead6f113a8e76b71b6bad83579d130c0d71350af185e93f4cf
fetched_at: '2026-06-28T22:38:08.439205+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - FINA340 - Compensação de PA Help
  NOCHADT
type: support-article
updated_at: '2024-01-04T15:19:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018994491-Cross-Segmentos-Backoffice-Linha-Protheus-FINA340-Compensa%C3%A7%C3%A3o-de-PA-Help-NOCHADT
---

**Dúvida**Ao efetuar uma compensação no **Contas a Pagar** o sistema retorna a mensagem *HELP*: NOCHQADT

**Ambiente**Cross Segmento - TOTVS BackOffice (Linha Protheus) - Financeiro - FINA473 - Todas as versões  
  
**Causa**Esta mensagem é apresentada devido ao **PA** ter sido incluído com cheque, aos parâmetros **F12** da rotina **FINA050** está com a seguinte configuração:  
- **Gera Cheq p/ Adiant** = Sim.  
- M**ovimento Banc Sem Cheq** = Não.

**Solução**Para solucionar essa ocorrência, existe duas opções:  
1 - Libera o cheque na **rotina Geração de Cheques** (**FINA190**) para que gere movimentação bancária e após isso será permitida a compensação.   
Dessa forma o sistema habilitará o campo **CHEQUE** na inclusão do **PA.** Assim, caso seja informado número do cheque haverá movimentação bancária e caso não seja informado, não haverá movimentação bancária.  
  
2 - Acesse o sistema com a **database** igual a data de inclusão do **PA**,- excluir o **PA** e inclui-lo com os parâmetros **F12** como:  
- **Gera Cheq p/ Adiant** = Não  
- **Movimento Banc Sem Cheq** = Sim
