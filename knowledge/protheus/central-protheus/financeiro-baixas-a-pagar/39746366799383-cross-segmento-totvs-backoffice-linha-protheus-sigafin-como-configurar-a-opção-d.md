---
article_id: 39746366799383
category: Financeiro - Baixas a Pagar
content_hash: ebbb2dce419ae5d2a03b861c0fd0817208e622fd031baaa4d3383e19e34215dd
fetched_at: '2026-06-28T22:37:24.907843+00:00'
product: protheus
section_id: 38295862957335
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Como configurar
  a opção de Rateio de Múltiplas Naturezas na Baixa de Títulos a Pagar para que se
  mantenha selecionada
type: support-article
updated_at: '2026-04-15T10:40:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39746366799383-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-Como-configurar-a-op%C3%A7%C3%A3o-de-Rateio-de-M%C3%BAltiplas-Naturezas-na-Baixa-de-T%C3%ADtulos-a-Pagar-para-que-se-mantenha-selecionada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39746366792983) Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**  
Como configurar o sistema para que, na rotina de baixa de títulos a pagar, a opção de Rateio de Múltiplas Naturezas já venha selecionada automaticamente?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/39746390900759)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as Releases  
  
**Solução:**

No padrão do sistema esta opção não é disponivel, mas pode ser utilizada ativando o ponto de entrada F080MNAT.

Para que a rotina de baixa de títulos a pagar apresente a opção de Rateio múltiplas naturezas previamente selecionada, é necessário validar se o parâmetro MV\_MULNATP está igual .T.

O ponto de entrada F080MNAT permite validação complementar se o um título baixado manualmente será rateado por múltiplas naturezas, quando o MV\_MULNATP = .T.

**Exemplo de Utilização:**

```
#include "protheus.ch"        

User Function F080MNAT()                                                                       
Local lRet := .T.

If SE2->E2_ORIGEM =='FINA050'
   lRet := .F.
EndIf

Return lRet
```
