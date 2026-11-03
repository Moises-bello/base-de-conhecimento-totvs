---
article_id: 360059977613
category: RH - Soluções para error.log
content_hash: 4fbb3ddcef78f38e1d7d36a14e364aa6dfb33b3198de75c5289adacef22c29e7
fetched_at: '2026-06-28T22:44:08.783217+00:00'
product: protheus
section_id: 115003853987
source: central-protheus
title: 'RH - Linha Protheus - GPE - Ao tentar excluir um título de rescisão é gerado
  o erro: type mismatch on compare  on FPROCEXC(GPEM660.PRX)'
type: support-article
updated_at: '2025-08-22T18:19:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360059977613-RH-Linha-Protheus-GPE-Ao-tentar-excluir-um-t%C3%ADtulo-de-rescis%C3%A3o-%C3%A9-gerado-o-erro-type-mismatch-on-compare-on-FPROCEXC-GPEM660-PRX
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34378040821271)**  Tempo aproximado para leitura: **00:01:00 min**

**Ocorrência**Ao tentar excluir um título de rescisão é gerado o **error log*: type mismatch on compare  on* FPROCEXC(GPEM660.PRX),****Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - à partir da versão 12.  
  
**Causa**  
Problema na estrutura da tabela RC1.  
  
**Solução**Para solução do problema é necessário verificar a validação do campo RC1\_TPDESP e a ordem dos campos da tabela RC1, conforme padrão abaixo:  
  
![](https://totvssuporte.zendesk.com/attachments/token/6Km43Ck4o495txCzHPgDK1FGE/?name=inline-424282929.png)  
  
![](https://totvssuporte.zendesk.com/attachments/token/4zUkQxRHeRWo6qSw52BofT32w/?name=inline562013863.png)  
  
**Saiba mais**Pacote Acumulado do RH: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/115015741848>
