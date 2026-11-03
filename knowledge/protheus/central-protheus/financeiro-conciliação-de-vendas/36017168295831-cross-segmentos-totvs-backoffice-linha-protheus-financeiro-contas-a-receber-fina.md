---
article_id: 36017168295831
category: Financeiro - Conciliação de Vendas
content_hash: 79e6ca04a45323427bb30016a304f621002a95306cefc39205f1059c440314c2
fetched_at: '2026-06-28T22:37:26.297129+00:00'
product: protheus
section_id: 35058743504791
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (Linha Protheus) - Financeiro - Contas a
  Receber - FINA918 - HELP - F070VLDCH‬
type: support-article
updated_at: '2025-10-31T16:59:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36017168295831-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-Financeiro-Contas-a-Receber-FINA918-HELP-F070VLDCH
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36017168287639) Tempo aproximado para leitura: **00:10:00 min**  
  
**Ocorrência**  
No módulo Financeiro, ao tentar realizar a conciliação de pagamentos das importações via rotina **FINA918**, ocorre o **HELP F070VLDCH‬**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36017152178967)

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**  
Esse incidente ocorre, pois na rotina **FINA490, o motivo de baixa NOR - Normal,** está definido como **ESPECIE = Sim.**  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse a rotina **FINA490 - Tabela de Motivos** de Baixa em **Miscelânea -> Arquivos.**  
2. Localize o motivo de baixa **NOR** e altere o campo **ESPECIE para Não.**  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36017152181015)  
3. Saia da rotina **FINA918** ou efetue **Log-Off e** realize novamente a baixa via Conciliação.   
  
**Saiba mais**  
[FINA918 - Conciliação de Pagamentos](https://tdn.totvs.com/pages/releaseview.action?pageId=655196877)
