---
article_id: 1500006350881
category: Financeiro - Baixas a Receber
content_hash: 6d45f25ef1be95cf9f79ff42298d1c4b2d6c8aada81c20cdd843471937ee2bcf
fetched_at: '2026-06-28T22:37:43.668352+00:00'
product: protheus
section_id: 33820269506967
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus  - SIGAFIN - FINA070 - Como contabilizar
  a baixa do contas a receber múltiplas naturezas com Centro de Custo
type: support-article
updated_at: '2026-05-20T19:10:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500006350881-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA070-Como-contabilizar-a-baixa-do-contas-a-receber-m%C3%BAltiplas-naturezas-com-Centro-de-Custo
---

**Dúvida**Como contabilizar a baixa do contas a receber múltiplas naturezas com Centro de Custo?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA070 - A partir da versão 11.8  
  
**Solução**Para que seja possível ratear a baixa em múltiplas naturezas e centro de custo, é importante executar os seguintes procedimentos:  
1. Criar os lançamentos padrões conforme a seguir:  
![](https://totvssuporte.zendesk.com/attachments/token/bNbKaiLlWlGHVfxkxlwOWWMwI/?name=inline1425740279.png)​  
2.    Alterar os lançamentos padrões informados a seguir. Todos os lançamentos padrões referentes a baixas e cancelamento de baixas de **contas a receber**, para utilizar a distribuição para múltipla natureza, devem conter, na obtenção do valor para o lançamento padrão **(Campo Vlr. Moeda 1 - CT5\_VLR01)**, a seguinte expressão:  
  
I**F(SE5->E5\_MULTNAT="1",SEV->EV\_VALOR,SE1->E1\_VALLIQ)**  
Lançamentos Afetados:  
![](https://totvssuporte.zendesk.com/attachments/token/cvLDUXPvMQW8QFB6CowTogm8v/?name=inline-1148728576.png)​  
3. No ambiente **Configurador**, observe os parâmetros **MV\_MULNAT e MV\_MULNATR**, que devem ter o conteúdo como T (True).  
  
**Saiba mais**

[Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Como utilizar rateio de múltiplas naturezas por Centro de Custo](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022094831-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Como-utilizar-rateio-de-m%C3%BAltiplas-naturezas-por-Centro-de-Custo)
