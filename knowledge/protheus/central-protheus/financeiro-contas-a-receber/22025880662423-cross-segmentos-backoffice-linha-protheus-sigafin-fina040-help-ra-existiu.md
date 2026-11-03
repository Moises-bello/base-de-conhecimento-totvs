---
article_id: 22025880662423
category: Financeiro - Contas a Receber
content_hash: 1fbb5cd49a29cbd610d24e3afb3de638580d82188123e9b01b4c8db562c9a87c
fetched_at: '2026-06-28T22:38:13.941435+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA040 - HELP: RA_EXISTIU'
type: support-article
updated_at: '2024-03-13T19:52:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22025880662423-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA040-HELP-RA-EXISTIU
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22025866429207) Tempo aproximado para leitura: **00:05:00** min**Ocorrência**Ao tentar gerar um título do tipo RA, o **Help: RA\_EXISTIU** é apresentado

![](https://centraldeatendimento.totvs.com/hc/article_attachments/22025880649111)  
 **Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**O Help ocorre quando o sistema localiza algum registro, que estava com os mesmos valores nos campos **Prefixo, Número, Parcela e Tipo.  
  
Importante**  
Mesmo **deletado** o **título RA**, o sistema deixa gravado as informações na **SE5**, pois ao criar um **RA**, automaticamente gera movimento bancário e quando o **Recebimento Antecipado** é excluído, o sistema cria um outro movimento na **SE5** de saída, para abater com o valor de entrada.  
  
**Solução**Para solucionar essa ocorrência, será preciso preencher um ou mais campos **(Prefixo, Numero, Parcela e Tipo)** diferentes da **Recebimento Antecipado** (**RA)** criada anteriormente.   
  
**Saiba mais**[Como incluir um Recebimento Antecipado (RA)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4410820301847-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA040-Como-incluir-um-Recebimento-Antecipado-RA)
