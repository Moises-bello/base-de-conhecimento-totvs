---
article_id: 18440622008983
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: de43a0dcb5bd055e9bfce2b321b1396306d93f2d6477aef052395b7fc4168271
fetched_at: '2026-06-28T22:39:51.417405+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice Linha Protheus - SIGAEIC - Execauto para
  automação da geração das Notas de Despesas na rotina "EICDI158".
type: support-article
updated_at: '2023-10-20T20:05:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18440622008983-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Execauto-para-automa%C3%A7%C3%A3o-da-gera%C3%A7%C3%A3o-das-Notas-de-Despesas-na-rotina-EICDI158
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18440574321175) Tempo aproximado para leitura: **02:00 min****Dúvida**Execauto para automação da geração das Notas de Despesas na rotina "**EICDI158 -** NF Despesas".  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – *Easy Import Control* – A partir da versão 12.1.33.  
  
**Solução**A Rotina "NF de DESPESA **(EICDI158)**" não possui execauto. A mesma executa a rotina automática do "**MATA140"**. Desta forma, a regra aplicável para todo o ERP com base no parâmetro "**MV\_PCNFE"** também deverá ser aplicada ao **SIGAEIC** visto que o parâmetro mencionado se refere à rotina de Documento de Entrada.   
Quanto a rotina **"NF de DESPESA (EICDI158)"**, o objetivo é justamente lançar notas fiscais para escrituração (para os clientes que não quiserem o fazer diretamente pelo módulo de compras ou pela rotina de documento de entrada), ou seja, através do **SIGAEIC** efetuar o lançamento das notas fiscais das despesas que possuem esse documento fiscal.   
  
**Saiba mais:**[EICDI158 - Geração de nota fiscal de despesa](https://tdn.totvs.com/pages/releaseview.action?pageId=490993846)
