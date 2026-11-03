---
article_id: 11183074820503
category: Financeiro - Novo Gestor Financeiro
content_hash: a68ea9bda898886f1031c2683003627d5e3e47d3e864dbbfce1394471b5b5e60
fetched_at: '2026-06-28T22:37:41.341389+00:00'
product: protheus
section_id: 33830415324183
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA710  - Movimentações
  apresentadas Aba Consolidado/Geral
type: support-article
updated_at: '2026-01-07T19:21:36Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11183074820503-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA710-Movimenta%C3%A7%C3%B5es-apresentadas-Aba-Consolidado-Geral
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37510958624023) Tempo aproximado para leitura: **00:08:00 min**  
  
**Dúvida**  
Quais são as movimentações apresentadas na Aba "Consolidado/Geral"?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da Release 12.1.33  
  
**Solução**  
As abas "**Consolidado/Geral**" foram desenvolvidas com o objetivo de ter um fluxo muito mais rápido e assertivo. Para isso existe a **tabela F75** que é atualizada com o saldo dos títulos, considerando todos os abatimentos vinculados, juros, descontos, valores acessórios, acréscimos e decréscimos e tudo que está vinculado ao título.   
  
Desta forma, em tempo de execução da rotina, não precisamos recalcular o saldo, deixando a rotina muito mais performática trazendo os saldos acumulados.

**Importante**  
Porém, tudo isso é calculado com base na data em que o parâmetro **MV\_TFCJOBT** e **JOB FINA711** é executado para frente e assim trará um fluxograma das entradas e saídas que entrarão no Financeiro.  
  
**Saiba mais:**  
[Movimentações Financeiras - FINA710 ABA CONSOLIDADO](https://tdn.totvs.com/pages/releaseview.action?pageId=622668231#Movimenta%C3%A7%C3%B5esFinanceirasFINA710-05.ABACONSOLIDADO)  
[Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA710 - Configuração e Funcionalidade do Novo Gestor Financeiro](https://centraldeatendimento.totvs.com/hc/pt-br/articles/7019775569047)
