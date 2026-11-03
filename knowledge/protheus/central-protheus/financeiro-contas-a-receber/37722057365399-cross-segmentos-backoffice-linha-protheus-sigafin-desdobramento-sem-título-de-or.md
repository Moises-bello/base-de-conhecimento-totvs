---
article_id: 37722057365399
category: Financeiro - Contas a Receber
content_hash: 2d596e86feb59549611b02296ada64f4834d640c7c46ca2bbf40f5d78f05347f
fetched_at: '2026-06-28T22:38:12.609094+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Desdobramento sem título
  de origem
type: support-article
updated_at: '2026-01-16T12:53:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37722057365399-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Desdobramento-sem-t%C3%ADtulo-de-origem
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37722057360663) Tempo aproximado para leitura: 00**:05 min**  
  
**Dúvida**  
Como gerar títulos com desdobramento sem a geração do título pai, mantendo apenas os títulos desdobrados?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões.  
  
**Solução**  
Quando é realizado o desdobramento de um título, o sistema gera um título totalizador, com o valor total já baixado, e cria as parcelas correspondentes (títulos desdobrados) em aberto. Esse procedimento visa garantir a rastreabilidade das informações, especialmente em processos de cancelamento do desdobramento.

Para controlar esse comportamento, foi disponibilizado o parâmetro **MV\_NRASDSD**, responsável por definir se a inclusão de títulos via desdobramento seguirá o processo antigo ou o processo atual do sistema.

**MV\_NRASDSD com conteúdo ".T." :** O desdobramento ocorre conforme o processo antigo. Nesse cenário:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37722057361047)

**MV\_NRASDSD com conteúdo ".F." :** O desdobramento ocorre conforme o processo atual, com rastreabilidade, mantendo o título originador como totalizador. Nesse cenário:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37722057361943)

**Importante**

**Parâmetro válido para as rotinas de Contas a Pagar e Contas a Receber.**

**Saiba mais**

[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA050 - Cancelamento de Desdobramento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018602371-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA050-Cancelamento-de-Desdobramento)
