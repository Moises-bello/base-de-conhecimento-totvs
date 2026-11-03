---
article_id: 37787527471895
category: Financeiro - Integrações (SIGAFIN)
content_hash: fdda0fa55fa991711123b28ed7f3f1f01202a5e9992ab35429ecdc4f28f03bd8
fetched_at: '2026-06-28T22:38:18.544553+00:00'
product: protheus
section_id: 1500001539241
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINI050 - Integração
  EAI mensagem unica ACCOUNTPAYABLEDOCUMENT - Help: COMBENTI   Combinação de entidades
  repetida'
type: support-article
updated_at: '2026-01-20T12:31:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37787527471895-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINI050-Integra%C3%A7%C3%A3o-EAI-mensagem-unica-ACCOUNTPAYABLEDOCUMENT-Help-COMBENTI-Combina%C3%A7%C3%A3o-de-entidades-repetida
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37787527460503) Tempo aproximado para leitura: **00:03:00 min**  
  
**Ocorrência**  
Ao integrar um titulo do RM para o Protheus ocorre o Help: **COMBENTI**  
**Combinação de entidades repetida**  
Tabela SEV 15/01/2026 10:49:36  
Erro no Item   2  
--------------------------------------------------------------------------------  
Natureza             - EV\_NATUREZ   := 02333       
Vlr.Movim.           - EV\_VALOR     := 730.08  
Perc. Distr.         - EV\_PERC      := 100  
Rat. C.Custo         - EV\_RATEICC   := 1 < -- Invalido  
                   - AUTRATEICC   := Array  
--------------------------------------------------------------------------------  
Falha na gravação automática do Titulo!  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**  
Esse help ocorre devido o cadastro do **De/para** do alias da tabela **CTT** cadastrado repetidos, conforme um exemplo do print abaixo repetindo o centro de custo 99.99.05   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/37787567911191)  
  
**Solução**  
Acessar o configurador **SIGACFG → Ambiente → Schedule → De/Para Mensagem Única** e corrigir o cadastro do **De/Para** do alias da tabela **CTT**, pois não é permitido possuir entidades repetidas quando há rateio entre centros de custo para o mesmo centro de custo
