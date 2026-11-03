---
article_id: 1500011105641
category: Financeiro - Liquidação a Receber
content_hash: 56b2f0b9b7226c812ea571454f85df03e46ee9c20ba60a26f6dd18a79ea3f17c
fetched_at: '2026-06-28T22:37:42.255381+00:00'
product: protheus
section_id: 33830247616663
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA460 - HELP F460VLDVEN
  DATA SUPERIOR A DATA DE VENCIMENTO LIMITE
type: support-article
updated_at: '2025-07-30T20:37:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500011105641-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA460-HELP-F460VLDVEN-DATA-SUPERIOR-A-DATA-DE-VENCIMENTO-LIMITE
---

**Ocorrência**No módulo financeiro ao acessar a rotina de liquidação a receber FINA460, ao alterar o campo validade ocorre o HELP:  F460VLDVEN DATA SUPERIOR À DATA DE VENCIMENTO LIMITE

**Ambiente**Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA460 - Todas as versões  
  
**Causa**O campo **Validade**, na rotina, está vinculado à **data base do sistema**. Ao informar uma data **posterior à data base**, o sistema apresentará uma **mensagem de ajuda (help)**.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500017938502)  
  
**Solução**Para que o **Help** não seja exibido ao alterar a validade da liquidação a receber na rotina **FINA460**, é necessário atualizar a **data base do sistema**.

**Exemplo**

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500018534822)**

**Saiba mais**

**[FINA460 - Liquidação a receber - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=545236275)**
