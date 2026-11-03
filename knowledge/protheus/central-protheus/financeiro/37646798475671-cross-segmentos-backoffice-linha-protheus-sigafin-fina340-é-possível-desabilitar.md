---
article_id: 37646798475671
category: Financeiro
content_hash: 001a92cc66b164d5dc08dfb8388d327bef65f37658edce9d4e23cf15418274af
fetched_at: '2026-06-28T22:38:03.000770+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA340 - É possível
  desabilitar o tipo:DIC
type: support-article
updated_at: '2026-01-13T17:45:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37646798475671-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA340-%C3%89-poss%C3%ADvel-desabilitar-o-tipo-DIC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37646798458775) Tempo aproximado para leitura: **00:10:00 min**  
  
**Dúvida**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Protheus Financeiro- Todas as versões]  
  
**Solução**  
O tipo DIC faz parte do comportamento padrão do processo de compensação entre PA sem impostos x NF com impostos ou etc..., conforme regra de cálculo do Protheus.   
  
Atualmente não existe parâmetro ou configuração que permita desabilitar a geração do tipo: DIC para esse tipo de operação.  
  
A geração do DIC ocorre porque, no momento da compensação, os impostos são calculados de forma proporcional sobre o valor compensado.

Quando há diferença entre o valor compensado e os impostos gerados, o sistema cria o tipo: DIC para manter a integridade contábil e fiscal do processo, conforme descrito na documentação oficial da TOTVS (exemplo de compensação PA sem imposto x NF com imposto).  
<https://tdn.totvs.com/pages/releaseview.action?pageId=354465728>

Caso seja necessário desconsiderar o tipo: DIC a orientação será baixar o tipo:DIC com o "tipo de baixa = DACAO" que não irá fazer movimentação bancária

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/37646798459031)](https://centraldeatendimento.totvs.com/hc/article_attachments/37646798459031)

Saiba mais:

[FIN0053\_FINA340\_COMPENSAÇÃO\_PA\_E\_NF](https://tdn.totvs.com/pages/releaseview.action?pageId=354465728)  
dsfin-17263
