---
article_id: 360061550514
category: Financeiro - Caixinha
content_hash: 496067e0e2a5491654390461932e901b8cd764062a9794ebfefa2cd25209bf43
fetched_at: '2026-06-28T22:37:53.931268+00:00'
product: protheus
section_id: 1500001550702
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA560 - O sistema
  não contabiliza movimentos do caixinha, quando (EU_BAIXA=' ') com LP 572
type: support-article
updated_at: '2022-06-15T02:01:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360061550514-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA560-O-sistema-n%C3%A3o-contabiliza-movimentos-do-caixinha-quando-EU-BAIXA-com-LP-572
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**O sistema não contabiliza movimentos do caixinha, quando (EU\_BAIXA=' ') com LP 572?  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA560 - Todas as versões  
  
**Solução**Se a sua contabilização for off-line existe a pergunta 18 nos parâmetros da rotina:

![](https://totvssuporte.zendesk.com/attachments/token/adUsSYUuKkKp3uccYZDDNLiet/?name=inline708318664.png)

Que possibilita contabilizar o movimento sem estar baixado, considera o campo **EU\_DIGIT** conforme o help do campo.

**Saiba mais:**  
Segue o link quando foi efetuado a melhoria:  
[FIN0034\_LPAD\_Contabilizar\_LP\_572](https://tdn.totvs.com/display/public/PROT/FIN0034_LPAD_Contabilizar_LP_572)
