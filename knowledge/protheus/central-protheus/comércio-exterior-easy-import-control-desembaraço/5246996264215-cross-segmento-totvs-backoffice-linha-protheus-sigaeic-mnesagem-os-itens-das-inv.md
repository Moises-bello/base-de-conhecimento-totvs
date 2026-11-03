---
article_id: 5246996264215
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: 8e73c532f4b88289de8f8e9c8e2539fc217b1f3586feeff3a24e7a1025cfb7db
fetched_at: '2026-06-28T22:39:50.117291+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Mnesagem: Os
  itens das invoices não estão de acordo com o embarque. Marque novamente as invoices
  e regrave o desembaraço'
type: support-article
updated_at: '2024-07-16T14:33:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5246996264215-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Mnesagem-Os-itens-das-invoices-n%C3%A3o-est%C3%A3o-de-acordo-com-o-embarque-Marque-novamente-as-invoices-e-regrave-o-desembara%C3%A7o
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Ao tentar incluir uma nota de recebimento de importação (**EICDI154**) o sistema exibe uma mensagem "Os itens das invoices não estão de acordo com o embarque. Marque novamente as invoices e regrave o desembaraço." Como faço para que esta mensagem não seja exibida?

![DIVERGENCIA_SW8_E_SW7.PNG](https://centraldeatendimento.totvs.com/hc/article_attachments/5246664099479/DIVERGENCIA_SW8_E_SW7.PNG)  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões

**Solução**Esta mensagem ocorre porque existe uma divergência dos itens da invoice com os itens da DI na fase de desembaraço. A quantidade de itens da invoice (tabela **SW8**) está maior que o itens da DI (Tabela **SW7**).  
Será necessário filtrar os itens  da processo da tabela **SW8** e **SW7** e identificar qual(is) o(s) item(ns) que existem na invoice que não foram selecionados no fase dos itens.  
Caso a quantidade de itens da fase da invoice e dos itens da DI sejam muitas, orientamos a pedir para que o administrador do sistema faça um filtro destas informações através do processo (via APSDU, ORACLE ou SQL) e que encaminhe em uma planilha estas informações para que seja identificado a divergência.
