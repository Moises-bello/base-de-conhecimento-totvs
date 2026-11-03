---
article_id: 8853051873431
category: Financeiro
content_hash: 96b793f8132e557db56f7aad00667452e685023dcf01d54f69a96a63eda2c6a0
fetched_at: '2026-06-28T22:38:01.194569+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN  - FATA900 Dashboard
  Financeiro  - Gráficos de Fluxo de caixa Natureza zerados
type: support-article
updated_at: '2023-08-01T12:10:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8853051873431-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FATA900-Dashboard-Financeiro-Gr%C3%A1ficos-de-Fluxo-de-caixa-Natureza-zerados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **02:00:00 min**

**Ocorrência**  
No módulo Financeiro , ao tentar abrir a rotina FATA900 Novo Dashboard Financeiro os gráficos de fluxo de caixa saem zerados.  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FATA900 -  Todas versões  
  
**Causa**  
Esse incidente ocorre devido a não existir dados nas tabelas:

**FIV** - Movimentos Diários Fluxo por Natureza Financeira

**FIW** - Movimentos Mensais Fluxo por Natureza Financeira  

**FIX** - Cabeçalho Histórico Fluxo por Natureza Financeira

**FJV** - Movimento Analítico por Natureza,  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
  
**1.**  A rotina por padrão somente irá demonstrar os valores, se as tabelas supracitadas estiverem alimentadas. Caso não esteja, deve utilizar a rotina **FINA800** para atualizar os saldos das naturezas.   
   
**2.**  Para que as tabelas sejam populadas sem a necessidade do **Recálculo (FINA800)**, deve-se alterar o parâmetro  **MV\_FINATFN=1**

**Saiba mais:**    
[Recálculo de Saldos por Natureza (FINA800 - SIGAFIN)](https://tdn.totvs.com/pages/viewpage.action?pageId=312163211)
